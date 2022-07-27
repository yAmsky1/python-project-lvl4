from django.test import TestCase
from django.urls import reverse

from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User
from .models import Label
from ..translations import (
    LABEL_CREATED_MESSAGE,
    LABEL_CHANGED_MESSAGE,
    LABEL_DELETED_MESSAGE,
    ERROR_LABEL_IN_USE_MESSAGE
)


HTTP200 = 200
HTTP302 = 302


class LabelsTest(TestCase):
    fixtures = [
        'users.json',
        'statuses.json',
        'tasks.json',
        'labels.json',
    ]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)

        self.status1 = Status.objects.get(pk=1)

        self.task1 = Task.objects.get(pk=1)

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)

    def test_labels_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('labels:list'))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(
            response,
            template_name='labels/labels_list.html',
        )

        tasks_list = list(response.context['labels'])
        self.assertQuerysetEqual(
            tasks_list,
            [self.label1, self.label2, self.label3],
        )

    def test_create_label(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        new_label = {
            'name': 'test_label1',
        }
        response = self.client.post(
            reverse('labels:create'),
            new_label,
            follow=True,
        )

        self.assertRedirects(response, '/labels/', status_code=HTTP302)
        self.assertContains(
            response,
            LABEL_CREATED_MESSAGE,
        )

        label = Label.objects.get(name=new_label['name'])
        self.assertEqual(4, label.id)

    def test_change_label(self):
        self.client.force_login(self.user1)
        label = self.label3
        response = self.client.get(reverse('labels:change', args=(label.id,)))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(response, template_name='form.html')
        url = reverse('labels:change', args=(label.id,))
        changed_label = {
            'name': 'changed',
        }
        response = self.client.post(url, changed_label, follow=True)

        self.assertRedirects(response, '/labels/', status_code=HTTP302)
        self.assertContains(response, LABEL_CHANGED_MESSAGE)
        new_label = Label.objects.get(name=changed_label['name'])
        self.assertEqual(label.id, new_label.id)

    def test_delete_label_with_task(self):
        self.client.force_login(self.user1)
        label = self.label1
        url = reverse('labels:delete', args=(label.pk,))
        response = self.client.post(url, follow=True)
        self.assertTrue(Label.objects.filter(pk=label.pk).exists())
        self.assertRedirects(response, '/labels/')
        self.assertContains(response, ERROR_LABEL_IN_USE_MESSAGE)

    def test_delete_label(self):
        self.client.force_login(self.user1)
        Task.objects.all().delete()
        Status.objects.all().delete()
        label = self.label2
        url = reverse('labels:delete', args=(label.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(response, template_name='delete.html')

        response = self.client.post(url, follow=True)

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=label.id)
        self.assertRedirects(response, '/labels/', status_code=HTTP302)
        self.assertContains(response, LABEL_DELETED_MESSAGE)

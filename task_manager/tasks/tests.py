from django.test import TestCase
from django.urls import reverse

from ..labels.models import Label
from .models import Task
from ..users.models import User
from ..translations import (
    TASK_CREATED_MESSAGE,
    TASK_CHANGED_MESSAGE,
    TASK_DELETED_MESSAGE,
    DELETERIGHTS_MESSAGE,
)


HTTP200 = 200
HTTP302 = 302


class TasksTests(TestCase):
    fixtures = ['users.json', 'statuses.json', 'tasks.json', 'labels.json']

    def setUp(self):
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.label3 = Label.objects.get(pk=3)

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)

    def test_tasks_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(
            response,
            template_name='tasks/tasks_list.html'
        )

        tasks_list = list(response.context['tasks'])
        self.assertQuerysetEqual(tasks_list, [self.task1, self.task2])

    def test_create_task(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(
            response,
            template_name='form.html',
        )

        new_task = {
            'name': 'task_name',
            'description': 'task_description',
            'status': 1,
            'created_by': 1,
            'executor': 1,
        }
        response = self.client.post(
            reverse('tasks:create'),
            new_task,
            follow=True,
        )

        self.assertRedirects(response, '/tasks/', status_code=HTTP302)
        self.assertContains(response, TASK_CREATED_MESSAGE)
        task = Task.objects.get(name=new_task['name'])
        self.assertEqual(task.description, 'task_description')

    def test_change_task(self):
        self.client.force_login(self.user1)
        url = reverse('tasks:change', args=(self.task1.pk,))
        changed_task = {
            'name': "new_task_name",
            'description': "new_task_description",
            'status': 2,
            'created_by': 1,
            'executor': 2,
        }
        response = self.client.post(url, changed_task, follow=True)
        self.assertRedirects(response, '/tasks/', status_code=HTTP302)
        self.assertContains(response, TASK_CHANGED_MESSAGE)
        self.assertEqual(Task.objects.get(pk=self.task1.pk), self.task1)

    def test_delete_task_without_rights(self):
        self.client.force_login(self.user1)
        url = reverse('tasks:delete', args=(self.task2.pk,))
        response = self.client.post(url, follow=True)
        self.assertTrue(Task.objects.filter(pk=self.task2.pk).exists())
        self.assertRedirects(response, '/tasks/', status_code=HTTP302)
        self.assertEqual(response.status_code, HTTP200)
        self.assertContains(response, DELETERIGHTS_MESSAGE)

    def test_delete_task(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse(
            'tasks:delete',
            args=(self.task1.pk,)
        ))
        self.assertEqual(response.status_code, HTTP200)
        self.assertTemplateUsed(response, template_name='delete.html')

        url = reverse('tasks:delete', args=(self.task1.pk,))
        response = self.client.post(url, follow=True)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=self.task1.pk)
        self.assertRedirects(response, '/tasks/', status_code=HTTP302)
        self.assertContains(response, TASK_DELETED_MESSAGE)

    def test_filter_by_status(self):
        self.client.force_login(self.user1)
        filtered_by_status = "{0}?status=2".format(reverse('tasks:list'))
        response = self.client.get(filtered_by_status)
        self.assertEqual(response.status_code, HTTP200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task2])

    def test_filter_by_executive(self):
        self.client.force_login(self.user1)
        list_filtered_by_exec = "{0}?executor=2".format(reverse('tasks:list'))
        response = self.client.get(list_filtered_by_exec)
        self.assertEqual(response.status_code, HTTP200)
        self.assertQuerysetEqual(list(response.context['tasks']), [self.task1])

    def test_filter_by_label(self):
        self.client.force_login(self.user1)
        filtered_by_label = "{0}?labels=1".format(reverse('tasks:list'))
        response = self.client.get(filtered_by_label)
        self.assertEqual(response.status_code, HTTP200)
        self.assertQuerysetEqual(
            list(response.context['tasks']),
            [self.task1, self.task2],
        )

    def test_filter_by_own_tasks(self):
        self.client.force_login(self.user2)
        filtered_by_own = "{0}?own_task=on".format(reverse('tasks:list'))
        response = self.client.get(filtered_by_own)
        self.assertEqual(response.status_code, HTTP200)
        self.assertQuerysetEqual(
            list(response.context['tasks']),
            [self.task2],
        )

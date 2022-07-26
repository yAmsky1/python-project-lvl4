from django.test import TestCase
from django.urls import reverse

from .models import Status
from ..users.models import User
from ..translations import (
    STATUS_CREATED_MESSAGE,
    STATUS_CHANGED_MESSAGE,
    STATUS_DELETED_MESSAGE,
)


STATUS_CODE_OK = 200


class TestStatuses(TestCase):
    fixtures = ["statuses.json", "users.json"]

    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)

    def test_statuses_list(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        statuses_list = list(response.context['statuses'])
        self.assertQuerysetEqual(statuses_list, [self.status1, self.status2])

    def test_statuses_list_no_login(self):
        response = self.client.get(reverse('statuses:list'))
        self.assertRedirects(response, '/login/')

    def test_create_status(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse('statuses:create'),
            {'name': 'new_status'},
            follow=True,
        )
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, STATUS_CREATED_MESSAGE)
        created_status = Status.objects.get(name='new_status')
        self.assertEquals(created_status.name, 'new_status')

    def test_change_status(self):
        self.client.force_login(self.user)
        url = reverse('statuses:change', args=(self.status1.pk,))
        response = self.client.post(url, {'name': "next_status"}, follow=True)
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, STATUS_CHANGED_MESSAGE)
        self.assertEqual(Status.objects.get(pk=self.status1.id), self.status1)

    def test_delete_status(self):
        self.client.force_login(self.user)
        url = reverse('statuses:delete', args=(self.status1.pk,))
        response = self.client.post(url, follow=True)
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=self.status1.pk)
        self.assertRedirects(response, '/statuses/')
        self.assertContains(response, STATUS_DELETED_MESSAGE)

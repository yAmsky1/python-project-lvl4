from django.test import TestCase
from django.urls import reverse

from .models import User
from ..translations import (
    USER_CREATED_MESSAGE,
    USER_CHANGED_MESSAGE,
    USER_DELETED_MESSAGE,
)


STATUS_CODE_OK = 200


class TestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)

    def test_create_user(self):
        url = reverse('users:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, template_name='form.html')
        new_user = {
            'username': "test_user_name0",
            'first_name': "Guido",
            'last_name': "van Rossum",
            'password1': "qwerasdf1",
            'password2': "qwerasdf1",
        }
        response = self.client.post(url, new_user, follow=True)
        self.assertContains(response, USER_CREATED_MESSAGE)
        self.assertRedirects(response, '/login/', status_code=302)
        created_user = User.objects.get(username=new_user['username'])
        self.assertTrue(created_user.check_password('qwerasdf1'))
        self.assertEqual(created_user.first_name, 'Guido')

    def test_users_list(self):
        response = self.client.get(reverse('users:list'))
        users_list = list(response.context['users'])
        test_user1, test_user2 = users_list

        self.assertEqual(response.status_code, 200)
        self.assertEqual(test_user1.username, 'username01')
        self.assertEqual(test_user2.first_name, 'Anton')

    def test_change_user(self):
        user = self.user1
        self.client.force_login(User.objects.get(pk=user.id))

        new_user_params = {
            'username': 'new_username',
            'first_name': 'Guido',
            'last_name': 'van Rossum',
            'password1': 'qwerasdf1',
            'password2': 'qwerasdf1'
        }
        url = reverse('users:change', args=(user.id,))
        response = self.client.post(url, data=new_user_params, follow=True)
        self.assertRedirects(response, '/users/')
        self.assertContains(response, USER_CHANGED_MESSAGE)
        changed_user = User.objects.get(username='new_username')
        self.assertTrue(changed_user.check_password, 'qwerasdf1')
        self.assertEqual('van Rossum', changed_user.last_name)

    def test_delete_user(self):
        self.client.force_login(self.user2)
        url = reverse('users:delete', args=(self.user2.id,))
        response = self.client.post(url, follow=True)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=self.user2.id)

        self.assertRedirects(response, '/users/')
        self.assertContains(response, USER_DELETED_MESSAGE)

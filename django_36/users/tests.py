from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='test_name', password='test+password',
                                                   first_name='Yurii', last_name='Yuriyovych', age=34)

    def test_model_data(self):
        self.assertEqual(self.user.username, second='test_name')
        self.assertEqual(self.user.password, second='test+password')
        self.assertEqual(self.user.first_name, second='Yurii')
        self.assertEqual(self.user.last_name, second='Yuriyovych')
        self.assertEqual(self.user.age, second=34)


class TestUsersView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(username='test_name1', password='4534534534534',
                                                   first_name='Ira', last_name='Zhuk', age=31)

    def test_users_list_view(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, second=200)
        self.assertTemplateUsed(response, template_name='users/users_list.html')
        self.assertContains(response, text='Zhuk')

    def test_users_detail_view(self):
        responce = self.client.get(reverse('users:users-detail', kwargs={'pk': self.user.pk}))
        self.assertEqual(responce.status_code, second=200)
        self.assertContains(responce, text='Zhuk')

    def test_users_create_view(self):
        responce = self.client.post('/users/create/', {
            'first_name': 'Rose',
            'last_name': 'Sterling',
            'age': 56,
            'user': self.user.id
        })
        self.assertEqual(responce.status_code, second=200)

    # i commented this, because, i dont have deleteviews in my view.py
    # def test_users_delete_view(self):
    #     responce = self.client.delete(f'/users/{self.user.pk}/delete/')
    #     self.assertEqual(responce.status_code, second=302)

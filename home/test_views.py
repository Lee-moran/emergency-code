from django.test import TestCase
from django.contrib.auth.models import User


class TestHomeViews(TestCase):
    """ Test correct rendering for home url """

    def setUp(self):
        testuser = User.objects.create_user(
            username='test_username',
            password='secret',
            email='testuser@email.com'
        )
        testuser.save()

    def test_get_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

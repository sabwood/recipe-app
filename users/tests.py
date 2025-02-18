from django.test import TestCase
from .models import User #to access User model

# Create your tests here.
class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(
            username='testusername',
            password='testpassword',
            email='test@gmail.com'
        )

    def test_username(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name

        self.assertEqual(field_label, 'username')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length

        self.assertEqual(max_length, 50)
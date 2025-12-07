from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from loginapp.models import UserProfile
from django.contrib.messages import get_messages

class CreateEmployeeViewTest(TestCase):
    def setUp(self):
        # Create an admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='adminpass'
        )
        self.client = Client()
        self.client.login(username='admin', password='adminpass')

    def test_create_employee_success(self):
        # Test successful employee creation
        response = self.client.post(reverse('cms:create_employee'), {
            'username': 'testemployee',
            'password': 'testpass123',
            'email': 'employee@test.com'
        }, follow=True)

        # Check redirect to create_employee
        self.assertRedirects(response, reverse('cms:create_employee'))

        # Check user was created
        user = User.objects.get(username='testemployee')
        self.assertEqual(user.email, 'employee@test.com')

        # Check profile role was updated to employee
        self.assertEqual(user.profile.role, 'employee')

        # Check success message
        messages = list(get_messages(response.context['request']))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Employee created successfully!')

    def test_create_employee_duplicate_username(self):
        # Create a user first
        User.objects.create_user(
            username='existinguser',
            email='existing@test.com',
            password='existingpass'
        )

        # Try to create another with same username
        response = self.client.post(reverse('cms:create_employee'), {
            'username': 'existinguser',
            'password': 'newpass123',
            'email': 'new@test.com'
        }, follow=True)

        # Check redirect to create_employee
        self.assertRedirects(response, reverse('cms:create_employee'))

        # Check no new user was created (still only one with that username)
        users = User.objects.filter(username='existinguser')
        self.assertEqual(users.count(), 1)

        # Check error message
        messages = list(get_messages(response.context['request']))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Username already taken!')

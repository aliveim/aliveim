from unittest import TestCase
from registration.forms import UserRegistrationForm


class TestUserRegistrationForm(TestCase):
    def test_register_user(self):
        data = {
            'email': 'test@email.com',
            'password1': 'password',
            'password2': 'password'
        }

        form = UserRegistrationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_register_user_passwords_mismatch(self):
        data = {
            'email': 'test@email.com',
            'password1': 'password',
            'password2': 'passworddddd'
        }

        form = UserRegistrationForm(data=data)
        self.assertFalse(form.is_valid())

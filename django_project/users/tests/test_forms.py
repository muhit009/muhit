from django.test import TestCase
from users.forms import UserRegistrationForm

class TestForms(TestCase):

    def test_user_registration_form_valid_data(self):
        form = UserRegistrationForm(data={
            'username': 'RoomKinbo',
            'email': 'bhaloachi@company.com',
            'password1': 'gamekhelbo',
            'password2': 'gamekhelbo'
        })

        self.assertTrue(form.is_valid())

    def test_user_registration_form_valid_no_data(self):
        form = UserRegistrationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
from unittest import TestCase

from accounts.forms import RegistrationForm


class TestRegistrationForm(TestCase):
    def test_registration_form(self):
        # test invalid data
        invalid_data = {
            "username": "Codeurrs",
            "password": "superuser",
            "login": "not superuser"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        valid_data = {
            "username": "Codeurrs",
            "password": "superuser",
            "login": "superuser"
        }
        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)

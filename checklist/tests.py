from django.test import TestCase
from django.urls import reverse

class DummyTests(TestCase):
    def test_dummy_pass(self):
        self.assertIs(True, True)

    def test_dummy_fail(self):
        self.assertIs(True, False)

class DummyViewTests(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_admin_page(self):
        response = self.client.get('admin/')
        print(response)
        self.assertEqual(response.status_code, 200)

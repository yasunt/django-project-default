from selenium import webdriver

from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import CustomUser


class AccountTest(TestCase):

    def setUp(self):
        # self.browser = webdriver.Firefox()
        self.username = 'test_user'
        self.password = 'testtest01'
        self.email = 'test@example.com'
        self.login_url = reverse('registration:login')

        """
    def test_login_view(self):
        login_url = reverse('/login')
        self.assertTrue(False)

    def test_logout_view(self):
        self.assertTrue(False)
        """

    def test_registration(self):
        self.user = CustomUser.objects.create_user(
            username=self.username,
            password=self.password,
            email=self.email
            )
        print(self.user)
        user = CustomUser.objects.get(username=self.username)

        self.assertEqual(user, self.user)

    def test_registration_view(self):
        pass

        """
    def test_password_reset_view(self):
        self.assertTrue(False)

    def test_mypage_view(self):
        self.assertTrue(False)
        """

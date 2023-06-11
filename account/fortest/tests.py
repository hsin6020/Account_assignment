from django.test import TestCase
from account.models import Account


class UserTestCase(TestCase):
    def setUp(self):
        account = Account.objects.create(username="testname", password="test123Password")

    def test_user_introduce_self(self):
        account = Account.objects.get(username="testname")
        self.assertEqual(account.introduce_self(), 'I am testname.')

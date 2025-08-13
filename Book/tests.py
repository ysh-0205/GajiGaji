from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import  Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        pass


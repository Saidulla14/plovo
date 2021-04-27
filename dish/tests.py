from django.test import TestCase
from rest_framework import APITestCase

# Create your tests here.
class DishApiTestCase(APITestCase):
    def get(self):
        url = 'http://http://127.0.0.1:8000/dish/'
        print(url)
        response = self.client.get(url)
        print(response.data)
        print(data)
from django.test import TestCase
from .models import Users, Todos
import pytest

# Create your tests here.


class UsersModelTestCase(TestCase):
    def setUp(self):
        self.user = Users(user_id=15, name='Helena Croonberg', username='helidorek',
                          email='hela@gmail.com', address_street='Kolorowa', address_suite='Suite 808',
                          address_city='Lipawa', address_zipcode='12345-0987', address_geo_lat=-38.1234,
                          address_geo_lng=82.1234, phone='123456 4321', website='hela.briz', company_name='Helson',
                          company_catchPhrase='lorem ipsum, lotem ipsum, lorem ipsum es dolor',
                          company_bs='csfgvbthstg sdre')

    def test_user_creation(self):
        self.user.save()
        self.assertIsNotNone(self.user.user_id)


class TodosModelTestCase(TestCase):
    def setUp(self):
        self.todos = Todos(todos_id=356, user_id=15, title='lorem ipsum, dos eres', completed='True')

    def test_todos_creation(self):
        self.todos.save()
        self.assertIsNotNone(self.todos.todos_id)

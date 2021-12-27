from django.db import models
import requests


# Create your models here.


class Users(models.Model):
    user_id = models.IntegerField(default=0)
    name = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    email = models.EmailField(max_length=254)
    address_street = models.CharField(max_length=120)
    address_suite = models.CharField(max_length=120)
    address_city = models.CharField(max_length=120)
    address_zipcode = models.CharField(max_length=120)
    address_geo_lat = models.DecimalField(decimal_places=4, max_digits=15)
    address_geo_lng = models.DecimalField(decimal_places=4, max_digits=15)
    phone = models.CharField(max_length=120)
    website = models.URLField(max_length=200)
    company_name = models.CharField(max_length=120)
    company_catchPhrase = models.TextField()
    company_bs = models.CharField(max_length=1024)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.users_response = []
        self.data = {}

    def get_users_from_api(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.request("GET", url)
        self.users_response = response.json()
        return self.users_response

    def save_response(self, data):
        users, created = Users.objects.get_or_create(user_id=data['user_id'], defaults=data)
        users.save()
        return created

    def get_users_to_db(self):
        response = self.get_users_from_api()
        counter = 0
        for i in response:
            self.data['user_id'] = i['id']
            self.data['name'] = i['name']
            self.data['username'] = i['username']
            self.data['email'] = i['email']
            self.data['address_street'] = i['address']['street']
            self.data['address_suite'] = i['address']['suite']
            self.data['address_city'] = i['address']['city']
            self.data['address_zipcode'] = i['address']['zipcode']
            self.data['address_geo_lat'] = i['address']['geo']['lat']
            self.data['address_geo_lng'] = i['address']['geo']['lng']
            self.data['phone'] = i['phone']
            self.data['website'] = i['website']
            self.data['company_name'] = i['company']['name']
            self.data['company_catchPhrase'] = i['company']['catchPhrase']
            self.data['company_bs'] = i['company']['bs']
            if self.save_response(self.data):
                counter += 1
        return counter, len(self.data)

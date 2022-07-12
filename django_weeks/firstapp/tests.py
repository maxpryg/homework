import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from firstapp.models import Store
from firstapp.serializers import StoreSerializer


class GetStoresOpenEndpointTest(APITestCase):
    """ Test openendpoint GET method """

    def setUp(self):
        Store.objects.create(
            first_name='store1',
            description='this is store number 1',
            rating=50,
        )

        Store.objects.create(
            first_name='store2',
            description='this is store number 2',
            rating=50,
        )

        Store.objects.create(
            first_name='store13,
            description='this is store number 3',
            rating=50,
        )

    def test_get_all_stores(self):
        response = self.client.get(reverse('DriverView-list'))
        # get data from db
        stores = Stores.objects.all()
        serializer = StoreSerializer(stores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

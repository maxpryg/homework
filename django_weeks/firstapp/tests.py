import json

from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase

from firstapp.models import Store
from firstapp.serializers import StoreSerializer


class StoreEndpointTest(APITestCase):
    """ StoreViewSet tests """

    def setUp(self):
        self.store1 = Store.objects.create(
            name='store1',
            description='this is store number 1',
            rating=50,
        )

        self.store2 = Store.objects.create(
            name='store2',
            description='this is store number 2',
            rating=50,
        )

        self.store3 = Store.objects.create(
            name='store13',
            description='this is store number 3',
            rating=50,
        )

    def test_get_all_stores(self):
        response = self.client.get(reverse('stores-list'))
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_store(self):
        response = self.client.get(
            reverse('stores-detail', kwargs={'pk': self.store1.pk}))
        store = Store.objects.get(pk=self.store1.pk)
        serializer = StoreSerializer(store)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_store(self):
        response = self.client.get(
            reverse('stores-detail', kwargs={'pk': 10000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserStoreGetEndpointTest(APITestCase):
    """ UserStoreViewSet tests for GET method """
    def setUp(self):
        self.user1 = User.objects.create(
            username='user1',
            password='pass'
        )

        self.store1 = Store.objects.create(
            name='store1',
            description='this is store number 1',
            rating=50,
            owner=self.user1
        )

        self.store2 = Store.objects.create(
            name='store2',
            description='this is store number 2',
            rating=50,
            owner=self.user1
        )

        self.store3 = Store.objects.create(
            name='store13',
            description='this is store number 3',
            rating=50,
        )

    def test_anonymous_cannot_get_stores_list(self):
        response = self.client.get(reverse("my_stores-list"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_anonymous_cannot_get_single_store(self):
        response = self.client.get(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_user_get_stores(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse("my_stores-list"))
        self.assertEqual(len(response.data), self.user1.stores.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_get_valid_single_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_get_invalid_single_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse("my_stores-detail",
                                           kwargs={'pk': 10000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UserStorePostEndpointTest(APITestCase):
    """ UserStoreViewSet tests for POST method """
    def setUp(self):
        self.user1 = User.objects.create(
            username='user1',
            password='pass'
        )

        self.payload = {
            'name': 'store1',
            'description': 'this is store number 1',
            'rating': 50,
            'owner': self.user1.id
        }

    def test_anonymous_cannot_create_store(self):
        response = self.client.post(reverse("my_stores-list"),
                                    data=json.dumps(self.payload),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_create_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.post(reverse("my_stores-list"),
                                    data=json.dumps(self.payload),
                                    content_type='application/json'
                                    )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class UserStorePutPatchDeleteEndpointsTest(APITestCase):
    """ UserStoreViewSet tests for PUT and PATCH methods """
    def setUp(self):
        self.user1 = User.objects.create(
            username='user1',
            password='pass'
        )

        self.store1 = Store.objects.create(
            name='store1',
            description='this is store number 1',
            rating=50,
            owner=self.user1
        )

        self.partial_payload = {
            'description': 'this store changed its description',
        }

        self.payload = {
                    'name': 'new store name',
                    'description': 'new store descritption',
                    'rating': 50,
                    'owner': self.user1.id
                }

    def test_anonymous_cannot_partially_update_store(self):
        response = self.client.patch(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}),
                                   data=json.dumps(self.partial_payload),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_partially_update_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}),
                                   data=json.dumps(self.partial_payload),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_cannot_update_store(self):
        response = self.client.put(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}),
                                   data=json.dumps(self.payload),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_update_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.put(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}),
                                   data=json.dumps(self.payload),
                                   content_type='application/json'
                                   )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_cannot_delete_store(self):
        response = self.client.delete(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_authenticated_can_delete_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.delete(reverse("my_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AdminStoreGetEndpointTest(APITestCase):
    """ AdminStoreViewSet tests for GET method """
    def setUp(self):
        self.user1 = User.objects.create(
            username='user1',
            password='pass'
        )

        self.admin = User.objects.create(
            username='adminuser',
            password='pass',
            is_staff=True
        )

        self.store1 = Store.objects.create(
            name='store1',
            description='this is store number 1',
            rating=50,
            owner=self.user1
        )

        self.store2 = Store.objects.create(
            name='store2',
            description='this is store number 2',
            rating=50,
            owner=self.user1
        )

        self.store3 = Store.objects.create(
            name='store13',
            description='this is store number 3',
            rating=50,
        )

    def test_anonymous_cannot_get_admin_stores_list(self):
        response = self.client.get(reverse("admin_stores-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_cannot_get_admin_stores_list(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse("admin_stores-list"))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_can_get_admin_stores(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse("admin_stores-list"))
        self.assertEqual(len(response.data), Store.objects.count())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anonymous_cannot_get_single_admin_store(self):
        response = self.client.get(reverse("admin_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authorized_cannot_get_single_admin_store(self):
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(reverse("admin_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_user_can_get_valid_single_admin_store(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse("admin_stores-detail",
                                           kwargs={'pk': self.store1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_user_get_invalid_single_admin_store(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(reverse("admin_stores-detail",
                                           kwargs={'pk': 10000}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

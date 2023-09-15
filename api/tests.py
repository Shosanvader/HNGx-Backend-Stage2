import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.views import status
from .models import Person
from .serializers import PersonSerializer

# initialize the APIClient app
client = APIClient()

class CreateNewPersonTest(TestCase):
    """ Test module for inserting a new person """

    def setUp(self):
        self.valid_payload = {
            'name': 'Mark Essien'
        }
        self.invalid_payload = {
            'name': ''
        }

    def test_create_valid_person(self):
        response = client.post(
            reverse('person-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_person(self):
        response = client.post(
            reverse('person-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class GetSinglePersonTest(TestCase):
    """ Test module for getting a single person """

    def setUp(self):
        self.mark = Person.objects.create(name='Mark Essien')

    def test_get_valid_single_person(self):
        response = client.get(reverse('person-detail', kwargs={'pk': self.mark.pk}))
        person = Person.objects.get(pk=self.mark.pk)
        serializer = PersonSerializer(person)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_person(self):
        response = client.get(reverse('person-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class UpdateSinglePersonTest(TestCase):
    """ Test module for updating an existing person record """

    def setUp(self):
        self.mark = Person.objects.create(name='Mark Essien')
        self.valid_payload = {
            'name': 'Mark Updated',
        }
        self.invalid_payload = {
            'name': '',
        }

    def test_valid_update_person(self):
        response = client.put(
            reverse('person-detail', kwargs={'pk': self.mark.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_person(self):
        response = client.put(
            reverse('person-detail', kwargs={'pk': self.mark.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSinglePersonTest(TestCase):
    """ Test module for deleting an existing person record """

    def setUp(self):
        self.mark = Person.objects.create(name='Mark Essien')

    def test_valid_delete_person(self):
        response = client.delete(reverse('person-detail', kwargs={'pk': self.mark.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_person(self):
        response = client.delete(reverse('person-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


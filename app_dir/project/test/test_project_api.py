from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from faker import Factory
from app_dir.factories import ProjectFactory, UserFactory

faker = Factory.create()


class ProjectApiTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.project = ProjectFactory()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.namespace = 'project_api'
        self.body = {
            'name': faker.word(),
            'description': faker.text()
        }
        self.create_url = reverse(self.namespace + ':create')
        self.list_url = reverse(self.namespace + ':list')
        self.update_url = reverse(self.namespace + ':update', kwargs={'pk': self.project.id})

    def test_create_project_api(self):
        response = self.client.post(self.create_url, self.body, format='json')
        self.assertEqual(201, response.status_code)

    def test_list_projects_api_without_parameters(self):
        response = self.client.get(self.list_url)
        self.assertContains(response, self.project)

    def test_listing_project_api_with_parameters(self):
        response = self.client.get(self.list_url + '?page_size=10&q=' + self.project.name)
        self.assertContains(response, self.project)

    def test_update_project_api(self):
        response = self.client.put(self.update_url, self.body)
        self.assertEqual(200, response.status_code)

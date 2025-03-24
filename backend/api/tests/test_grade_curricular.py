from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import GradeCurricular
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

User = get_user_model()

class GradeCurricularModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descricao da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )

    def test_grade_curricular_str(self):
        self.assertEqual(str(self.grade), 'Grade 1 (2025/1)')


class GradeCurricularViewSetTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username='pedro.af200',
            email='pedro.af200@gmail.com',
            password='password123',
            first_name='Pedro',
            last_name='Almeida',
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        self.client.force_authenticate(user=self.user)

        google_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImVlMTkzZDQ2NDdhYjRhMzU4NWFhOWIyYjNiNDg0YTg3YWE2OGJiNDIiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIxODY3MDM2MzA3ODAtdWdnNXFnMHNpcWw2NjZ0bnUzcTN0bHQxcGwyOWZvMnAuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIxODY3MDM2MzA3ODAtdWdnNXFnMHNpcWw2NjZ0bnUzcTN0bHQxcGwyOWZvMnAuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDc2NjQ3MzIwNzExNDU1NjQwMDkiLCJlbWFpbCI6InBlZHJvLmFmMjAwQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYmYiOjE3NDI3Njc0MjEsIm5hbWUiOiJQZWRybyBBbG1laWRhIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0pmc2Q1QmR1OXJmazc1NXdvUEpma2EtaG9HNF9OaVNlZHhBblA2eEZhbURuam9NZz1zOTYtYyIsImdpdmVuX25hbWUiOiJQZWRybyIsImZhbWlseV9uYW1lIjoiQWxtZWlkYSIsImlhdCI6MTc0Mjc2NzcyMSwiZXhwIjoxNzQyNzcxMzIxLCJqdGkiOiI1ZWVjYWViMjU2OWFhZTMyM2ZjYjRmMDI4ZDcyY2RhNjkwMGViY2I1In0.op_vFO4p2togCob0D0BlGvz3DvifqBPmUwpoNIUXHUTRMqXKAAvJL5tB3sOWqP1oEut9skelPNMJn-O_ppLLNZh-SbZmDclnGz4t9I7cDSWnTVQpsuAROrTS46RIgtgGDsBrCwL13Am4qFGc1YWiwK_Nha-dBaKfSf5E9G6aZ44NTLcp97dJcrdyTpidQX4CazxTteX5Rg2e7XqShBkjccqX8S0h5XrDaHPU_MyfQ74gSdta6IEdLKiIcKyq3EyC753AxJ2cP1JIUJltwyXTvA-T78EiKaOk35cA611_0PRBLrmmv_fVmoOpUURtLAEURos5jd532sTCZAWTKatilw"

        response = self.client.post('/api/google-login/', data={"token": google_token})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()

        self.access_token = response_data['access']
        self.refresh_token = response_data['refresh']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_create_grade_curricular(self):
        url = reverse('gradecurricular-list')
        data = {
            'nome': 'New Grade',
            'descricao': 'Description of the new grade',
            'semestre_vigencia': '2025.1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GradeCurricular.objects.count(), 1)
        self.assertEqual(GradeCurricular.objects.get().nome, 'New Grade')

    def test_read_grade_curricular(self):
        grade = GradeCurricular.objects.create(nome='New Grade', descricao='Description', semestre_vigencia='2025.1', usuario=self.user)
        url = reverse('gradecurricular-detail', args=[grade.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'New Grade')

    def test_update_grade_curricular(self):
        grade = GradeCurricular.objects.create(nome='New Grade', descricao='Description', semestre_vigencia='2025.1', usuario=self.user)
        url = reverse('gradecurricular-detail', args=[grade.id])
        data = {
            'nome': 'Updated Grade',
            'descricao': 'Updated description',
            'semestre_vigencia': '2025.2'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        grade.refresh_from_db()
        self.assertEqual(grade.nome, 'Updated Grade')
        self.assertEqual(grade.descricao, 'Updated description')

    def test_delete_grade_curricular(self):
        grade = GradeCurricular.objects.create(nome='New Grade', descricao='Description', semestre_vigencia='2025.1', usuario=self.user)
        url = reverse('gradecurricular-detail', args=[grade.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GradeCurricular.objects.count(), 0)

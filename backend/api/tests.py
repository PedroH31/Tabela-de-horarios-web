# api/tests.py
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import GradeCurricular, ComponenteCurricular, Horario, Alocacao
from rest_framework_simplejwt.tokens import RefreshToken
from unittest.mock import patch

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.name, 'Test User')
        self.assertFalse(self.user.is_superuser)
        self.assertFalse(self.user.is_staff)

class GradeCurricularModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descrição da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )

    def test_grade_creation(self):
        self.assertEqual(self.grade.nome, 'Grade 1')
        self.assertEqual(self.grade.usuario, self.user)
        self.assertEqual(str(self.grade), 'Grade 1 (2025/1)')

class ComponenteCurricularModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descrição da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.componente = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP101',
            nome='Componente 1',
            ch_teorica=60,
            ch_pratica=40
        )

    def test_componente_creation(self):
        self.assertEqual(self.componente.codigo, 'COMP101')
        self.assertEqual(self.componente.grade_curricular, self.grade)
        self.assertEqual(str(self.componente), 'COMP101 - Componente 1')

class HorarioModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descrição da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.horario = Horario.objects.create(
            nome='Horario 1',
            semestre='2025/1',
            grade_curricular=self.grade,
            usuario=self.user
        )

    def test_horario_creation(self):
        self.assertEqual(self.horario.nome, 'Horario 1')
        self.assertEqual(self.horario.usuario, self.user)
        self.assertEqual(str(self.horario), 'Horario 1 (2025/1)')

class AlocacaoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descrição da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.horario = Horario.objects.create(
            nome='Horario 1',
            semestre='2025/1',
            grade_curricular=self.grade,
            usuario=self.user
        )
        self.alocacao = Alocacao.objects.create(
            usuario=self.user,
            horario=self.horario,
            nome='Alocação 1',
            tipo=1
        )

    def test_alocacao_creation(self):
        self.assertEqual(self.alocacao.nome, 'Alocação 1')
        self.assertEqual(self.alocacao.usuario, self.user)
        self.assertEqual(str(self.alocacao), 'Alocação 1 - Turmas Fixas')

class GradeCurricularViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_grade_curricular(self):
        url = reverse('gradecurricular-list')
        data = {
            'nome': 'New Grade',
            'descricao': 'Description',
            'semestre_vigencia': '2025.1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(GradeCurricular.objects.count(), 1)
        grade = GradeCurricular.objects.get()
        self.assertEqual(grade.nome, 'New Grade')
        self.assertEqual(grade.usuario, self.user)

    def test_retrieve_grade_curricular(self):
        grade = GradeCurricular.objects.create(
            nome='Test Grade',
            descricao='Test Description',
            semestre_vigencia='2025.1',
            usuario=self.user
        )
        url = reverse('gradecurricular-detail', args=[grade.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'Test Grade')

    def test_update_grade_curricular(self):
        grade = GradeCurricular.objects.create(
            nome='Test Grade',
            descricao='Test Description',
            semestre_vigencia='2025.1',
            usuario=self.user
        )
        url = reverse('gradecurricular-detail', args=[grade.id])
        data = {
            'nome': 'Updated Grade',
            'descricao': 'Updated Description',
            'semestre_vigencia': '2025.2'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        grade.refresh_from_db()
        self.assertEqual(grade.nome, 'Updated Grade')

    def test_delete_grade_curricular(self):
        grade = GradeCurricular.objects.create(
            nome='Test Grade',
            descricao='Test Description',
            semestre_vigencia='2025.1',
            usuario=self.user
        )
        url = reverse('gradecurricular-detail', args=[grade.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(GradeCurricular.objects.count(), 0)

class ComponenteCurricularViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            name='Test User',
            password='testpass123'
        )
        self.grade = GradeCurricular.objects.create(
            nome='Test Grade',
            descricao='Test Description',
            semestre_vigencia='2025.1',
            usuario=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_create_componente_curricular(self):
        url = reverse('componentecurricular-list')
        data = {
            'grade_curricular': self.grade.id,
            'codigo': 'COMP101',
            'nome': 'Componente 1',
            'ch_teorica': 60,
            'ch_pratica': 40
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ComponenteCurricular.objects.count(), 1)
        componente = ComponenteCurricular.objects.get()
        self.assertEqual(componente.codigo, 'COMP101')

    def test_retrieve_componente_curricular(self):
        componente = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP101',
            nome='Componente 1',
            ch_teorica=60,
            ch_pratica=40
        )
        url = reverse('componentecurricular-detail', args=[componente.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['codigo'], 'COMP101')

class GoogleLoginTests(APITestCase):
    @patch('google.oauth2.id_token.verify_oauth2_token')
    def test_google_login(self, mock_verify):
        mock_verify.return_value = {
            'email': 'test@example.com',
            'name': 'Test User',
            'picture': 'http://example.com/pic.jpg'
        }
        
        response = self.client.post(reverse('google-login'), {
            'token': 'mock-google-token'
        }, format='json')
        
        self.assertEqual(response.status_code, 200)
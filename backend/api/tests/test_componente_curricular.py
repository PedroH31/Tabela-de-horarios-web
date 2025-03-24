from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from ..models import GradeCurricular, ComponenteCurricular

User = get_user_model()

class ComponenteCurricularModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descricao da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.componente = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP001',
            nome='Componente 1',
            abreviatura='COMP1',
            descricao='Descricao do Componente 1',
            periodo_diurno=True,
            periodo_noturno=False,
            ch_teorica=30,
            ch_pratica=20
        )

    def test_componente_curricular_str(self):
        self.assertEqual(str(self.componente), 'COMP001 - Componente 1')

class ComponenteCurricularViewSetTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', username='Test User', password='password')
        self.grade = GradeCurricular.objects.create(nome='New Grade', descricao='Description', semestre_vigencia='2025.1', usuario=self.user)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_componente_curricular(self):
        url = reverse('componentecurricular-list')
        data = {
            'grade_curricular': self.grade.id,
            'codigo': 'COMP001',
            'nome': 'New Component',
            'abreviatura': 'NC',
            'descricao': 'Description of the new component',
            'periodo_diurno': True,
            'periodo_noturno': False,
            'ch_teorica': 30,
            'ch_pratica': 20
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ComponenteCurricular.objects.count(), 1)
        self.assertEqual(ComponenteCurricular.objects.get().nome, 'New Component')

    def test_read_componente_curricular(self):
        component = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP001',
            nome='New Component',
            abreviatura='NC',
            descricao='Description',
            periodo_diurno=True,
            periodo_noturno=False,
            ch_teorica=30,
            ch_pratica=20
        )
        url = reverse('componentecurricular-detail', args=[component.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], 'New Component')

    def test_update_componente_curricular(self):
        component = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP001',
            nome='New Component',
            abreviatura='NC',
            descricao='Description',
            periodo_diurno=True,
            periodo_noturno=False,
            ch_teorica=30,
            ch_pratica=20
        )
        url = reverse('componentecurricular-detail', args=[component.id])
        data = {
            'grade_curricular': self.grade.id,
            'codigo': 'COMP002',
            'nome': 'Updated Component',
            'abreviatura': 'UC',
            'descricao': 'Updated description',
            'periodo_diurno': False,
            'periodo_noturno': True,
            'ch_teorica': 40,
            'ch_pratica': 25
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        component.refresh_from_db()
        self.assertEqual(component.codigo, 'COMP002')
        self.assertEqual(component.nome, 'Updated Component')
        self.assertEqual(component.descricao, 'Updated description')

    def test_delete_componente_curricular(self):
        component = ComponenteCurricular.objects.create(
            grade_curricular=self.grade,
            codigo='COMP001',
            nome='New Component',
            abreviatura='NC',
            descricao='Description',
            periodo_diurno=True,
            periodo_noturno=False,
            ch_teorica=30,
            ch_pratica=20
        )
        url = reverse('componentecurricular-detail', args=[component.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ComponenteCurricular.objects.count(), 0)

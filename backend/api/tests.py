from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import GradeCurricular, ComponenteCurricular, Horario, Alocacao

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

class HorarioModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descricao da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.horario = Horario.objects.create(
            nome='Horario 1',
            descricao='Descricao do Horario 1',
            semestre='2025/1',
            grade_curricular=self.grade,
            usuario=self.user
        )

    def test_horario_str(self):
        self.assertEqual(str(self.horario), 'Horario 1 (2025/1)')

class AlocacaoModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.grade = GradeCurricular.objects.create(
            nome='Grade 1',
            descricao='Descricao da Grade 1',
            semestre_vigencia='2025/1',
            usuario=self.user
        )
        self.horario = Horario.objects.create(
            nome='Horario 1',
            descricao='Descricao do Horario 1',
            semestre='2025/1',
            grade_curricular=self.grade,
            usuario=self.user
        )
        self.alocacao = Alocacao.objects.create(
            usuario=self.user,
            horario=self.horario,
            nome='Alocacao 1',
            descricao='Descricao da Alocacao 1',
            tipo=1,
            parametros={'param1': 'value1'},
            alocacao={'aloc1': 'value1'}
        )

    def test_alocacao_str(self):
        self.assertEqual(str(self.alocacao), 'Alocacao 1 - Turmas Fixas')
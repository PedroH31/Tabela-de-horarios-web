from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Alocacao, GradeCurricular, Horario

User = get_user_model()

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

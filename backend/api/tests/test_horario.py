from django.test import TestCase
from django.contrib.auth import get_user_model
from ..models import Horario, GradeCurricular

User = get_user_model()

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
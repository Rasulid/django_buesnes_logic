from django.db import models


class Case(models.Model):
    """Дело на сайте - Набор материалов по конкретному делу"""

    name = models.CharField("Названия дела", max_length=255)

    class Meta:
        db_table = 'case'

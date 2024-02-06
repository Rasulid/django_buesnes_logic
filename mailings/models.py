from django.db import models


class CommonMailingList(models.Model):
    """Рассылка на обшие материалы с сайта"""

    email = models.EmailField("Email подписчика")

    class Meta:
        db_table = 'common_mailing_list'


class CaseMailingList(models.Model):
    """Рассылка на материалы колнкретного дела"""

    email = models.EmailField("Email подписчика")
    case = models.ForeignKey(to='casies.Case', verbose_name="Дело", on_delete=models.CASCADE)

    class Meta:
        db_table = 'case_mailing_list'

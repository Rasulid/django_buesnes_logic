from django.conf import settings

from casies.models import Case
from mailings.Mailchimp_servises import add_mailchimp_email_with_tag
from mailings.models import CommonMailingList, CaseMailingList


def add_email_to_common_mailchimp_list(email: str) -> None:
    add_mailchimp_email_with_tag(audience_id=settings.MAILCHIMP_COMMON_LIST_ID,
                                 email=email,
                                 tag='COMMON TAG')

    CommonMailingList.objects.get_or_create(email=email)


def add_email_to_case_mailchimp_list(email: str, case: str) -> None:
    case = Case.objects.get(pk=case)
    case_tag = f'Case {case.name}'

    add_mailchimp_email_with_tag(audience_id=settings.MAILCHIMP_CASE_LIST_ID,
                                 email=email,
                                 tag=case_tag)

    CaseMailingList.objects.get_or_create(email=email, case=case)

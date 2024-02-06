from optparse import Option

from django.conf import settings
from mailchimp3 import MailChimp


def _get_mailchimp_client() -> MailChimp:
    """Возвращет клиент API для раьоты с Mailchimp"""
    return MailChimp(
        mc_api=settings.MAILCHIMP_API_KEY,
        mc_user=settings.MAILCHIMP_USERNAME)


def _add_email_to_mailchimp_audience(audience_id: str, email: str) -> None:
    """Добавляет email в Mailchimp аудиенсию с идинтификатором audience_id"""

    _get_mailchimp_client().lists.members.create(audience_id, {
        'email_address': email,
        'status': 'subscribed'
    })


def _get_mailchimp_subscriber_hash(email: str) -> Option[str]:
    """Возвращает идентификатор email а в Mailchimp или None"""
    members = _get_mailchimp_client() \
        .search_members \
        .get(query=email,
             fields='exact_matches.members.id') \
        .get('exact_matches').get('members')

    if not members:
        return None
    return members[0].get('id')


def _add_mailchimp_tag(audience_id: str, subscriber_hash: str, tag: str) -> None:
    """Добавляет Тег для имейда с идентмфикатором subscriber_hash в audience_id"""

    _get_mailchimp_client().lists.members.tags.update(
        list_id=audience_id,
        subscriber_hash=subscriber_hash,
        data={'tags': [{'name': tag, 'status': 'active'}]}
    )


def add_mailchimp_email_with_tag(audience_id: str, email: str, tag: str) -> None:
    """Добавляет Mailchimp email v audience_id"""
    _add_email_to_mailchimp_audience(audience_id=audience_id, email=email)
    _add_mailchimp_tag(audience_id=audience_id,
                       subscriber_hash=_get_mailchimp_subscriber_hash(email=email),
                       tag=tag)

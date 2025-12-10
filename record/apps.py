from django.apps import AppConfig


class RecordConfig(AppConfig):
    """
    Provides primary key type for record app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'record'

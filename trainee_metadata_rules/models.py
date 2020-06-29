from django.conf import settings

if settings.APP_NAME == 'trainee_metadata_rules':
    from .tests import models

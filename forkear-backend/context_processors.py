
from django.conf import settings # import the settings file

def app_name(request):
    return {'APP_NAME': settings.APP_NAME}

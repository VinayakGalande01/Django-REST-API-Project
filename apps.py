# Import the AppConfig class from Django's application module
from django.apps import AppConfig

# Define a configuration class for the Django app
class ApiConfig(AppConfig):
    """
    Configuration class for the 'api' Django application.
    This class is used to configure settings specific to the app.
    """
    
    # Specifies the default field type for auto-generated primary keys
    default_auto_field = 'django.db.models.BigAutoField'

    # Name of the Django app
    name = 'api'

from django.db import models
class Service(models.Model):
    service_icon = models.CharField(max_length = 50)
    service_title = models.CharField(max_length = 50)
    service_des = models.TextField()  # These 3 fields will be converted into table later, so name carefully
    # When migration will be done, it will automatically create a key named id and it will also set auto increment
    # Now goto settings.py and in Installed apps section add this app named service.


from django.db import models

from ipnsite import settings


class ModelBase(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Area(ModelBase):
    name = models.CharField(max_length=100)

    def short_name(self):
        return self.name


class Department(ModelBase):
    name = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)


class Profiles(ModelBase):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    login = models.BooleanField(default=False)
    permission = models.SmallIntegerField(default=1, null=True, blank=True)
    image = models.ImageField(upload_to=settings.PROFILE_IMAGE, null=True, blank=True)


class PublicationType(ModelBase):
    name = models.CharField(max_length=50)


class AddressedTo(ModelBase):
    name = models.CharField(max_length=50)


class Publications(ModelBase):
    profile = models.ForeignKey(Profiles, on_delete=models.CASCADE)  # Who make the publication
    tittle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.ForeignKey(PublicationType, on_delete=models.CASCADE)
    addressed_to = models.ForeignKey(AddressedTo, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.PUBLISHED_IMAGES, null=True, blank=True)
    file = models.FileField(upload_to=settings.PUBLISHED_DOCUMENTS, null=True, blank=True)
    revision = models.BooleanField(default=False, null=True, blank=True)
    edition = models.BooleanField(default=False, null=True, blank=True)




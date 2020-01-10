import os

from django.db import models
from ipnsite import settings


class ModelBase(models.Model):
    update_at = models.DateField(auto_now=True)
    create_at = models.DateField(auto_now=True)

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
    role = models.SmallIntegerField(default=1, null=True, blank=True)
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
    file = models.FileField(upload_to=settings.PUBLISHED_DOCUMENTS, null=True, blank=True)
    file_name = models.CharField(max_length=50, null=True, blank=True)
    reviewed = models.BooleanField(default=False, null=True, blank=True)
    published = models.BooleanField(default=False, null=True, blank=True)
    visible = models.BooleanField(default=True, blank=True, null=True)
    urgent = models.BooleanField(default=False, blank=True, null=True)
    approved = models.BooleanField(default=False, blank=True, null=True)

    def type_upper(self):
        return self.type.name.upper()

    def address_to_upper(self):
        return self.addressed_to.name.upper()


class Images(ModelBase):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=settings.PUBLISHED_IMAGES)
    publication = models.ForeignKey(Publications, on_delete=models.CASCADE, null=True, blank=True)

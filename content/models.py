from django.db import models

from django.template.defaultfilters import slugify

class HomeText(models.Model):
    """ Model for the admin-editable home page text, both below and above the fold
    """
    date = models.DateField()
    above_fold = models.TextField()
    below_fold = models.TextField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class PracticeArea(models.Model):
    """Model for the practice areas displayed on the main page
    """
    title = models.CharField(max_length = 255)
    image = models.ImageField(upload_to="images", null=True, blank=True)
    sub_area_1 = models.CharField(max_length = 255)
    sub_area_2 = models.CharField(max_length = 255)
    sub_area_3 = models.CharField(max_length = 255)
    sub_area_4 = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.title

class AboutText(models.Model):
    """ Model for the about text on About page
    """
    about_text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class Attorney(models.Model):
    """ Model for the attorneys on the Attorney page
    """

    name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    about = models.TextField()

    def __unicode__(self):
        return self.name

class AttorneyText(models.Model):
    """Model for the text on the Attorney page
    """
    
    text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class PracticeText(models.Model):
    """ Model for the text on Practice page
    """
    practice_text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class ResourceText(models.Model):
    """ Model for the text on Resource page
    """
    resource_text = models.TextField()
    date = models.DateField()

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)

class ContactText(models.Model):
    """ Model for the contact information on Contact page
    """
    contact_text = models.TextField()
    date = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    class Meta:
        ordering = ['-date']
        get_latest_by = "date"

    def __unicode__(self):
        return str(self.date)
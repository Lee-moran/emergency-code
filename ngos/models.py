from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """ Category Model """
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text='format: required, max_length=100',
    )
    friendly_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        max_length=100,
        null=False,
        unique=True,
        blank=False,
        verbose_name='Category slug',
        help_text='format: max_length=100'
    )

    class Meta:
        """ Meta class for the Category model """
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        """ String representation of Category model """
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    # expects as parameters the string we want to slugify
    # in this case, the category name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class NonGovernmentOrg(models.Model):
    """ NonGovernmentOrg Model """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200,
        null=False,
        unique=False,
        blank=False,
        help_text='format: required, max_length=200'
    )
    friendly_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    slug = models.SlugField(
        max_length=200,
        null=False,
        unique=True,
        blank=False,
        verbose_name='NGO slug',
        help_text='format: required, max_length=200'
    )
    is_featured = models.BooleanField(
        default=False,
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False,
        help_text='format: reqd, max_length=2000'
    )
    website = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        help_text='format: reqd, max_length=150'
    )
    image_url = models.URLField(
        max_length=1000,
        null=True,
        blank=True
    )
    image = models.ImageField(
        null=False,
        blank=False
    )

    class Meta:
        """ Meta class for NonGovernmentOrg model """
        verbose_name = 'NonGovernmentOrganization'
        verbose_name_plural = 'NGOs'
        ordering = ['name']

    def __str__(self):
        """ String representation of the NonGovernmentOrg model """
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    # expects as parameters the string we want to slugify
    # in this case, the NGO name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

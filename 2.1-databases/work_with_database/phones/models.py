from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    price = models.FloatField(default=0.00)
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200, unique=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)



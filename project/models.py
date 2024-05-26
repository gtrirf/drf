from django.db import models


class CategorySigns(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name


class RoadSings(models.Model):
    category = models.ForeignKey(CategorySigns, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.FileField(upload_to='videos', blank=True, null=True)
    audio = models.FileField(upload_to='audios', blank=True, null=True)
    document = models.FileField(upload_to='documents', blank=True, null=True)

    class Meta:
        db_table = 'road_signs'

    def __str__(self):
        return f'{self.category.name} | {self.name}'

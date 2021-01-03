from django.db import models
from django.urls import reverse
#model 안에서는 reverse쓰지만 class형 view안에서 field값으로 쓸때는 reverselazy 
# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : "+self.site_name+", 주소 : "+self.url

    def get_absolute_url(self):
        return reverse('detail',args=[str(self.id)])

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FilmesFav(models.Model):
  cartazPath = models.ImageField()
  imagePath = models.ImageField()
  title = models.CharField(max_length=100)
  genre = models.CharField(max_length=100)
  begin_date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.id);

  class Meta:
    db_table = 'favmovies'

from django.db import models
# use django's default user model
from django.contrib.auth.models import User

# Product Class 

class Product(models.Model):
    title = models.CharField(max_length=100)
    url = models.TextField(max_length=100)
    body = models.TextField(max_length=10000)
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1) # default = 1
    # foreign key points to the id of another model, in this case the user who made it
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) # if user is deleted, also delete this product

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:75]

    def pub_date_prettify(self):
        return self.pub_date.strftime('%b %e %Y')


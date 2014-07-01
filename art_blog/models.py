from django.db import models

class Article(models.Model):
    title=models.CharField(max_length=25)
    text=models.TextField(blank=True)
    pub_date=models.DateTimeField('date_art')
    def __unicode__(self):
        return self.title
    class Meta:
        ordering=['pub_date']

class Comment(models.Model):
    article=models.ForeignKey(Article)
    comment=models.TextField(blank=True)
    com_date=models.DateTimeField('date_com')
    class Meta:
        ordering=['-com_date']

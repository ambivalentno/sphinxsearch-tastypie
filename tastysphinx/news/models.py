from django.db import models


class Article(models.Model):
    """Article that stores news info. Have only 1 PaperIssue"""

    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField(max_length=255)
    author = models.ManyToManyField('Author')
    issue = models.ForeignKey('PaperIssue')

    def __unicode__(self):
        return self.slug


class Author(models.Model):
    """Author of articles"""

    name = models.CharField(max_length=255)
    resume = models.TextField()
    slug = models.SlugField(max_length=255)

    def __unicode__(self):
        return self.slug


class PaperIssue(models.Model):
    """An issue of a paper. A single article occurs here."""
    date = models.DateTimeField(auto_now_add=True)
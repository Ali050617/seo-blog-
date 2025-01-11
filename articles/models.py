from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    description = models.TextField()
    bod = models.DateField()
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='authors/')

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='article_images/')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('articles:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    comment_text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

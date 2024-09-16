
from django.db import models
from django.db.models import UniqueConstraint, Q


class Author(models.Model):
    name = models.CharField(max_length=100)


class Publisher(models.Model):
    name = models.CharField(max_length=75)
    registered_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    published_date = models.DateField()
    registered = models.BooleanField(null=True)
    managed = models.BooleanField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Исправлено с authors на author
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books', null=True)  # Исправлено с publisher_id

    def __str__(self):
        return f"{self.title} написано {self.author.name}"

    class Meta:
        db_table = 'Book'
        ordering = ['published_date']
        get_latest_by = 'published_date'
        unique_together = ('title', 'author')
        indexes = [models.Index(fields=('title', 'author'),
                                name='title_auth_index')]

        constraints = [UniqueConstraint(fields=['title'],
                                        condition=Q(registered=True),
                                        name='unique_book_registered')]

        verbose_name = 'fiction book'  # Человекочитаемое имя модели
        verbose_name_plural = 'fiction books'  # Человекочитаемое множественное число имени модели

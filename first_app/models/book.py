from django.db import models
from django.db.models import UniqueConstraint, Q


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    registered = models.BooleanField(null=True)
    managed = models.BooleanField(null=True)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} написано {self.author}"

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

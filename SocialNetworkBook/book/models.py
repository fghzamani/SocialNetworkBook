from django.db import models
from user.models import Profile
from django.utils import timezone


# Create your models here.

class Book(models.Model):
    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب ها"

    STATUS_CHOICE = [('F', 'Free'), ('B', 'Borrowed'), ('D', 'Deprecated')]
    title = models.CharField('book title', max_length=150)
    author = models.CharField('author', max_length=100, blank=True)
    publish_year = models.DateTimeField('publish_year', null=True)
    image = models.ImageField(upload_to='books/', blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='', related_name='owner')
    liked = models.ManyToManyField(Profile, blank=True, related_name='likes')
    created = models.DateTimeField('release_year', null=True, auto_now_add=True)
    updated = models.DateTimeField('update time', auto_now=True, null=True)
    book_info = models.TextField('book information', null=True, blank=True)
    status = models.CharField('status', max_length=1, choices=STATUS_CHOICE, default='F')

    def change(self):
        """
        changes the status of book
        """

        if self.status == 'F':
            self.status = 'B'

        else:
            self.status = 'F'
        self.save()

        return self.status

    def get_publish_year(self):
        return self.publish_year.year

    def __str__(self):
        return f'title:{self.title}'


class Comment(models.Model):
    class Meta:
        ordering = ('created',)  # ascending
        # ordering = '-created'  #descending

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comment_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Like(models.Model):
    LIKE_CHOICE = [('L', 'like'), ('d', 'dislike')]
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='like_owner')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.CharField(choices=LIKE_CHOICE, max_length=3)

    def toggle(self):
        if self.like == 'L':
            self.like = 'D'
        else:
            self.like = 'L'
        self.save()

# ####______________________________مثال خانم قانعی_____________________
# class Task(models.Model):
#     subtasks = models.ManyToManyField('self',
#                                       through='book.models.Dependency',
#                                       symmetrical=False,
#                                       through_fields=('supertask', 'subtask'),
#                                       related_name='supertasks')
#
#
# class Dependency(models.Model):
#     supertask = models.ForeignKey(Task, related_name='dependencies_as_supertask')
#     subtask = models.ForeignKey(Task, related_name='dependencies_as_subtask')

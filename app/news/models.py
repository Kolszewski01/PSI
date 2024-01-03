from django.db import models
from user.models import User
class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"News: {self.title}, Posted on: {formatted_datetime}"


class Comment(models.Model):
    news = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Comment by {self.user} on '{self.news.title}' at {formatted_datetime}"


class Report(models.Model):
    news = models.ForeignKey(News, related_name='reports', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        formatted_datetime = self.datetime.strftime('%Y-%m-%d %H:%M:%S')
        return f"Report by {self.user} on '{self.news.title}' at {formatted_datetime}"


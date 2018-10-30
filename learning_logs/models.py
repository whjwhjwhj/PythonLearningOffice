from django.db import models

# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
class Entry(models.Model):
    """学到的某个主题的具体知识"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def _str_(self):
        """返回模型的字符串"""
        return self.text[:50] + '........'

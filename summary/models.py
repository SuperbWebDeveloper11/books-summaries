from django.db import models
from django.urls import reverse


class Summary(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='summaries', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('summary:summary_detail', kwargs={'pk': self.pk})
                     
    class Meta:
        ordering = ['-created']


from django.db import models
from django.utils.text import slugify


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=600)
    long_description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma separated, e.g. Python, ROS2, C++")
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    video_embed = models.TextField(blank=True, null=True, help_text="Paste YouTube embed iframe here")
    date_completed = models.DateField(blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    order = models.PositiveIntegerField(default=0, help_text="Display order, lower numbers first")

    class Meta:
        ordering = ['order', '-date_completed']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(',')]

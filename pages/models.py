from django.core.validators import FileExtensionValidator
from django.db import models


class Resume(models.Model):
    file = models.FileField(
        upload_to='resume/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"Resume ({self.uploaded_at:%Y-%m-%d %H:%M})"

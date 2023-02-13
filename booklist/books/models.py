from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    writer=models.CharField(max_length=110,default='' )
    publication_date = models.DateField()
    #price = models.DecimalField(max_digits=5, decimal_places=2)
    pdf = models.FileField(upload_to='pdfs/', default='', null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.pdf.delete(save=False)
        super().delete(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        if self.pk:
            original = Book.objects.get(pk=self.pk)
            if original.pdf and original.pdf != self.pdf:
                original.pdf.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




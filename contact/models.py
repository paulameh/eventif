from django.db import models


class Contacts(models.Model):
    name = models.CharField('nome', max_length=150)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=30)
    message = models.CharField('message', max_length=1200)
    # created_at = models.DateTimeField('criado em', auto_now_add=True)
    # answer = models.CharField('answer', max_length=1200)
    # answered_at = models.DateTimeField('respondido em')
    
    class Meta:
        verbose_name_plural = 'contactares'
        verbose_name = 'contactar'
        ordering = ('--created_at',)

    def __str__(self):
        return self.name
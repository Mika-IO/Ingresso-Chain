from django.db import models
from django.contrib.auth.models import User
import uuid
class Event(models.Model):
    """
        Campanha de venda de ingressos para um evento
    """
    owner = models.ForeignKey(User)
    name = models.CharField('nome do evento', max_length=100)
    address = models.TextField('endereço do evento', max_length=255)
    latitude = models.DecimalField(blank=True, null=True, max_digits=9, decimal_places=6)
    longitute = models.DecimalField(blank=True, null=True,  max_digits=9, decimal_places=6)
    ticket_number = models.IntegerField('numero de ingressos')
    banner = models.ImageField('banner')

    class Meta:
        db_table = 'event'
        verbose_name_plural = 'eventos'
        verbose_name = 'evento'

    def __str__(self):
        return str("evento")


class Ticket(models.Model):
    """
        Ingresso de um evento
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, null=False, on_delete=models.CASCADE, verbose_name='evento')

    class Meta:
        db_table = 'ticket'
        verbose_name_plural = 'ingressos'
        verbose_name = 'ingresso'

    def __str__(self):
        return str("ingresso")
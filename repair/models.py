from django.db import models
from django.urls import reverse


class ApplicationForPrinter(models.Model):
    CHOICES = (
        ('Kartrijiň reňki gutardy', 'Kartrijiň reňki gutardy'),
        ('Printer solak çap edýär', 'Printer solak çap edýär'),
        ('Printer hapa çap edýär', 'Printer hapa çap edýär'),
        ('Printer işlemeýär', 'Printer işlemeýär'),
        ('Telefon işlemeýar', 'Telefon işlemeýar'),
        ('Içerki tor işlemeýär', 'Içerki tor işlemeýär'),
        ('Internet işlemeýär', 'Internet işlemeýär'),
        ('Kompýuter işlemeýär', 'Kompýuter işlemeýär'),
        ('Programma gurnamak', 'Programma gurnamak'),
        ('Programma işlemeýär', 'Programma işlemeýär'),
        ('Kompýuterde näsazlyklar bar', 'Kompýuterde näsazlyklar bar'),
        ('Başga mesele', 'Başga mesele'),
    )
    name = models.CharField(verbose_name='Ady we Familiýasy', max_length=100)
    cabinet = models.IntegerField(verbose_name='Iş otagynyň belgisi')
    phone_number = models.CharField(max_length=12, verbose_name='Iş telefon belgisi')
    problem = models.CharField(verbose_name='Meselesi', max_length=100, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Senesi')
    note = models.TextField(verbose_name='Bellik', max_length=500, blank=True, null=True)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return f'{self.cabinet} - {self.phone_number}'

    class Meta:
        verbose_name = 'Zaýawka'
        verbose_name_plural = 'Zaýawkalar'

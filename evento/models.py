from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.db.models import Q

class EventoManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(detalhes__icontains=query) |
                         Q(local__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=200)
    cidade = models.CharField('Cidade', max_length=200)
    provincia = models.CharField('Provincia', max_length=100)
    codigo_postal = models.CharField('Codigo Postal', max_length=5)

    def __str__(self):
        return '%s %s %s %s' %( self.rua, self.cidade, self.provincia, self.codigo_postal)

class Evento(models.Model):
    title = models.CharField('Titulo',max_length=200)
    image = models.ImageField('Imagem', upload_to="media/images/evento", blank=True)
    detalhes = models.TextField('Detalhes', blank=False)
    local = models.CharField('Local', max_length=200)
    start_dia = models.DateTimeField('Inicio dia e hora')
    end_dia = models.DateTimeField('Fim dia e hora')
    pub_data = models.DateTimeField('Publicado', auto_now_add=True)
    tags = TaggableManager()
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    objects = EventoManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('start_dia',)

    # Retorna true se o evento for hoje
    def today(self):
        today = timezone.now().date()
        date = self.start_dia #.strftime("%Y-%m-%d")
        if date.day == today.day and date.month == today.month and date.year == today.year:
            return True

    # Retorna true se o evento ainda estiver a ocorrer
    def happening(self):
        today = timezone.now()
        date = self.start_dia
        if date.year >= today.year:
            if today.month == date.month and self.end_dia.month >= today.month:
                if date.day < today.day and self.end_dia.day >= today.day:
                    return True
            elif today.month > date.month and self.end_dia.month >= today.month:
                if self.end_dia.day > today.day and self.end_dia.day >= today.day:
                    return True


    #Retorna true se o evento ainda nao aconteceu
    def future(self):
        today = timezone.now()
        date = self.start_dia

        if date.year >= today.year:
            if date.month > today.month:
                return True
            elif date.month == today.month:
                if date.day > today.day:
                    return True

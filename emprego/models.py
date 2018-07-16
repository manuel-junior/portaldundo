import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

from django.db.models import Q

class EmpregoManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(title__icontains=query) |
                         Q(text__icontains=query) |
                         Q(empresa__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=200, db_index=True)
    slug = models.SlugField('Slug', max_length=200, db_index=True, unique=True)

    icons = (
        ('<i class="fas fa-laptop"></i>', 'Informática e Telecomunicações'),
        ('<i class="fas fa-futbol"></i>', 'Desporto e Fitness'),
        ('<i class="fas fa-medkit"></i>', 'Saúde e Beleza'),
        ('<i class="fas fa-wrench"></i>', 'Reparação e Manutenção'),
        ('<i class="fas fa-shopping-basket"></i>', 'Assistente de Loja e Caixa'),
        ('<i class="fas fa-leaf"></i>', 'Agricultura e Jardinagem'),
        ('<i class="far fa-chart-bar"></i>', 'Finanças e Contabilidade'),
        ('<i class="fas fa-lock"></i>', 'Segurança e Vigilância'),
        ('<i class="fas fa-user-graduate"></i>', 'Formação e Educação'),
        ('<i class="fas fa-hotel"></i>', 'Restauração, Hotelaria e Turismo'),
        ('<i class="fas fa-people-carry"></i>', 'Construção'),
        ('<i class="fas fa-store"></i>', 'Comercial'),
        ('<i class="far fa-calendar-alt"></i>', 'Publicidade e Eventos'),
        ('<i class="fas fa-broom"></i>', 'Domésticos e Limpezas'),
        ('<i class="fas fa-car"></i>', 'Transportes e Logística'),
        ('Outros', 'Outros'),
    )
    icon = models.CharField(
        max_length=40,
        choices=icons,
        default='Outros',
    )

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('emprego:list_by_categoria', args=[self.slug])

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=200)
    city = models.CharField('Cidade',max_length=200)
    province = models.CharField('Provincia',max_length=100)
    code = models.CharField('Codigo Postal',max_length=5)

    def __str__(self):
        return self.city

class Emprego(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=250)
    text = models.TextField('Detalhes')
    empresa = models.CharField('Nome da Entidade', max_length=100)
    image = models.ImageField('Imagem', upload_to="media/images", blank=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name="Endereco")
    pub_data = models.DateTimeField('Publicado')
    disponivel = models.BooleanField(default=True)

    objects = EmpregoManager()

    class Meta:
        ordering = ('pub_data',)
        verbose_name = 'emprego'
        verbose_name_plural = 'empregos'

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_data <= now

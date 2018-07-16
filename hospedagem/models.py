from django.db import models
from django.db.models import Q
from django.urls import reverse

class HospedagemManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(nome__icontains=query) |
                         Q(detalhes__icontains=query) |
                         Q(slug__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
         return reverse('hospedagem:list_by_categoria', args=[self.slug])

class Hospedagem(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='hospedagens', on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField('Imagem', upload_to="media/hospedagens/imagens", blank=True)
    image_2 = models.ImageField('Imagem', upload_to="media/hospedagens/imagens", blank=True)
    image_3 = models.ImageField('Imagem', upload_to="media/hospedagens/imagens", blank=True)
    detalhes = models.TextField('Detalhes', blank=True)
    telefone = models.CharField("Telefone", max_length=15)
    alt_telefone = models.CharField("Alternativo", max_length=15, blank=True)
    email = models.EmailField("Email")
    url = models.URLField('Web Site', blank=True)
    endereco = models.CharField("Endereco", max_length=100)
    criado = models.DateTimeField(auto_now_add=True)

    objects = HospedagemManager()

    class Meta:
        ordering = ('-criado',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('hospedagem:hospedagem_detalhe', args=[self.id, self.slug])
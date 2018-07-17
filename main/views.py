from django.views.generic import TemplateView

from django.shortcuts import get_object_or_404, render


from apixu.client import ApixuClient, ApixuException
from requests.exceptions import ConnectionError

api_key = '32a43af57f694c51a6a14531180502'


def Inicio(request):
    #source https://github.com/apixu/apixu-python#apixu-client
    client = ApixuClient(api_key)
    temperatura = Temperatura()
    try:
        current = client.getCurrentWeather(q = 'Dundo, Lunda Norte, Angola')
        estado = str(current['current']['condition']['text'])

        if estado == "Partly cloudy":
            estado = 'Parcialmente Nublado'

        elif estado == "Cloudy":
            estado = "Nublado"

        elif estado == "Clear" or estado == "Daily sunny":
            estado = "Ceu limpo"

        elif estado == "Patchy rain possible":
            estado = "Possibilidade de chuva pontiaguda"

        elif estado == "Moderate or heavy rain shower":
            estado = "Aguaceiros fortes"

        elif estado == "Light rain shower":
            estado = "Aguaceiros"

        elif estado == "Thundery outbreaks possible":
            estado = "Possíveis surtos de tempestade"

        elif estado == "Torrential rain shower":
            estado = "Chuva torrencial"
        elif estado == "Patchy light rain with thunder":
            estado = "Possibilidade de chuva leve com trovão"
        elif estado == "Patchy light drizzle":
            estado = "Chuva ardente"

        elif estado =="Mist":
            estado = "Neblina"

        elif estado =="Sunny":
            estado = "Ensolarado"

        temperatura.temp_atual = int(current['current']['temp_c'])
        temperatura.estado = estado
        temperatura.localidade = current['location']['name']
        temperatura.image = current['current']['condition']['icon']

    except ConnectionError as e:
        temperatura = None
        print(e)

    c = {
        'temperatura': temperatura,
    }

    return render(request, "main.html", c)


class SobreView(TemplateView):
    template_name = "sobre_dundo.html"

class PatrimonioView(TemplateView):
    template_name = "patrimonio.html"

class ServicoView(TemplateView):
    template_name = "servicos.html"

class RestauranteView(TemplateView):
    template_name = "restaurante.html"

class NoticiaView(TemplateView):
    template_name = "noticia.html"


# ---------- Contacto ----------------#
#   imports for sending email
from django.shortcuts import redirect
from django.contrib import messages
from .forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


def contacto(request):
    form = ContactForm

    if request.method == 'POST':
        form = form(data=request.POST)

        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            form_content = form.cleaned_data['content']

            template = get_template('contact_template.txt')

            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                'Submisão de novo contacto',
                content,
                'Portal da Cidade do Dundo<hi@weedinglovely.com>',
                ['benhackone@gmail.com'],
                headers={'Reply-To': contact_email}
            )
            email.send()
            messages.success(request, 'Email enviado. Obrigado por nos contactar')
            return redirect('/contacto')

        else:
            messages.error(request, 'Formulário invalido')

    return render(request, 'contacto.html', {'form': form})

class Temperatura:
    estado = ""
    localidade = ""
    temp_atual = ""
    image = ""
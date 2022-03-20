
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contato
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def render_contatos(contatos, request, nome):
    paginator = Paginator(contatos, 4)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, f'contatos/{nome}.html', {
        'contatos': contatos
    })


def home(request):
    contatos = Contato.objects.order_by('id').filter(mostrar=True)
    return render_contatos(contatos, request, 'home')


def busca(request):

    termo = request.GET.get('termo')
    campos = Concat('nome', Value(' '), 'sobrenome')
    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo de pesquisa não pode ser vazio.'
        )
        return redirect('home')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        mostrar=True,)
    return render_contatos(contatos, request, 'busca')


def ver_contato(request, contato_id):

    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

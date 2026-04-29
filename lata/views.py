from django.shortcuts import render, redirect, get_object_or_404
from .models import Lata
from .forms import LataForm 

def listar_latas(request):

    latas = Lata.objects.all()

    nome = request.GET.get('nome')

    if nome:

        latas = latas.filter(
            nome__icontains=nome
        )

    marca = request.GET.get('marca')

    if marca:

        latas = latas.filter(
            marca__nome_marca__icontains=marca
        )


    portugal = request.GET.get('portugal')

    if portugal == 'sim':

        latas = latas.filter(
            disponivel_portugal=True
        )
        

    descontinuada = request.GET.get(
        'descontinuada'
    )

    if descontinuada == 'sim':

        latas = latas.filter(
            descontinuada=True
        )

    return render(
        request,
        'listar.html',
        {
            'latas': latas
        }
    )



def adicionar_lata(request):
    if request.method == 'POST':
        form = LataForm(request.POST, request.FILES)  # 👈 AQUI

        if form.is_valid():
            form.save()
            return redirect('listar_latas')
    else:
        form = LataForm()

    return render(
        request,
        'form.html',
        {
            'form': form,
            'titulo': 'Adicionar Lata'
        }
    )



def editar_lata(request, id):

    lata = get_object_or_404(
        Lata,
        id_lata=id
    )

    form = LataForm(
        request.POST or None,
        instance=lata
    )

    if form.is_valid():

        form.save()

        return redirect('listar_latas')

    return render(
        request,
        'form.html',
        {
            'form': form,
            'titulo': 'Editar Lata'
        }
    )



def apagar_lata(request, id):

    lata = get_object_or_404(
        Lata,
        id_lata=id
    )

    if request.method == 'POST':

        lata.delete()

        return redirect('listar_latas')

    return render(
        request,
        'apagar.html',
        {
            'lata': lata
        }
    )



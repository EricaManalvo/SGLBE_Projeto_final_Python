from urllib import request

from django.shortcuts import render, redirect, get_object_or_404

import lata
from .models import Lata
from .forms import LataForm 
from django.http import HttpResponse
from openpyxl import Workbook
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required


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

@login_required
def adicionar_lata(request):
    if request.method == 'POST':
        form = LataForm(request.POST, request.FILES) 

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


@login_required
def editar_lata(request, id):

    lata = get_object_or_404(
        Lata,
        id_lata=id
    )

    form = LataForm(
        request.POST or None,
        request.FILES or None,
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


@login_required
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

@login_required
def exportar_excel(request):
    latas = Lata.objects.all()

    wb = Workbook()
    ws = wb.active
    ws.title = "Latas"

    ws.append([
        "ID",
        "Nome",
        "Marca",
        "Tamanho",
        "Disponível Portugal",
        "Descontinuada",
        "Notas",
        "Imagem"
    ])

    for lata in latas:
        ws.append([
            lata.id_lata,
            lata.nome,
            lata.marca.nome_marca,
            lata.tamanho.tamanho,
            "Sim" if lata.disponivel_portugal else "Não",
            "Sim" if lata.descontinuada else "Não",
            lata.notas,
            lata.imagem.url if lata.imagem else ""
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="latas.xlsx"'

    wb.save(response)
    return response

@login_required
def exportar_pdf(request):
    latas = Lata.objects.all()

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="latas.pdf"'

    p = canvas.Canvas(response)

    y = 800

    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, y, "Lista de Latas")
    y -= 40

    p.setFont("Helvetica", 10)

    for lata in latas:

        if y < 120:
            p.showPage()
            y = 800
            p.setFont("Helvetica-Bold", 16)
            p.drawString(100, y, "Lista de Latas")
            y -= 40
            p.setFont("Helvetica", 10)

        p.drawString(100, y, f"ID: {lata.id_lata}")
        p.drawString(100, y - 15, f"Nome: {lata.nome}")
        p.drawString(100, y - 30, f"Marca: {lata.marca.nome_marca}")
        p.drawString(100, y - 45, f"Tamanho: {lata.tamanho.tamanho}")
        p.drawString(100, y - 60, f"Portugal: {'Sim' if lata.disponivel_portugal else 'Não'}")
        p.drawString(100, y - 75, f"Descontinuada: {'Sim' if lata.descontinuada else 'Não'}")
        p.drawString(100, y - 90, f"Notas: {lata.notas}")

        y -= 120

    p.save()
    return response


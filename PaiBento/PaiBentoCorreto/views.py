from django.shortcuts import render
from django.http import HttpResponse
from .models import PbFile


def home(request):

    produtos = PbFile.objects.first()

    return render(request, 'site/tela_principal.html', {'produtos': produtos})


def tela_cadastro(request):

    if request.method == "GET":

        return render(request, 'site/tela_cadastro.html')
    elif request.method == "POST":
        file = request.FILES.get("my_file")
        texto = request.POST.get("texto_certo")

        mf = PbFile(title="minha_imagem", arq=file, texto=texto)
        mf.save()

        print(file)

        return HttpResponse('teste')

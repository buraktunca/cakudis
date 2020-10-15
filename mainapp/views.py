from django.shortcuts import render
from .models import Soru,Cevaplar
from .forms import SoruForm,CevapForm
from django.shortcuts import redirect
# Create your views here.

def mainpage(request):
    sorular=Soru.objects.all()
    content={"sorular":sorular}
    return render(request,"mainpage.html",content)

def soru(request,pk):
    sorular=Soru.objects.get(pk=pk)
    cevaplar=Cevaplar.objects.filter(soru=sorular)
    if request.method == 'POST':
        form = CevapForm(request.POST, request.FILES)
        if form.is_valid():
            cevaplayan=request.POST["cevaplayan"]
            cevap=request.POST["cevap"]
            try:
                image=request.FILES["image"]
            except:
                image=""
            cevap=Cevaplar(soru=sorular,cevaplayan=cevaplayan,image=image,cevap=cevap)
            cevap.save()
            sorular.status="Cevaplandı"
            return redirect('soru', pk=pk)
    else:
        form = CevapForm()
    content={"sorular":sorular,"form":form,"cevaplar":cevaplar}
    return render(request,"soru.html",content)




def newsoru(request):
    sorular=Soru.objects.all()
    if request.method == 'POST':
        form = SoruForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = SoruForm()

    content={"form":form}

    return render(request,"newsoru.html",content)

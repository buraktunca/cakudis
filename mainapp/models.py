from django.db import models

# Create your models here.

sorustatus= [
    ("Cevaplanmadı","Cevaplanmadı"),
    ("Cevaplandı","Cevaplandı"),
]


soruchoices = [
        ("Ders ile ilgili bir soru", 'Ders ile ilgili bir soru'),
        ("Danışman hoca ile ilgili bir soru", 'Danışman hoca ile ilgili bir soru'),
        ("UBİS/ALMS ile ilgili bir soru", 'UBİS/ALMS ile ilgili bir soru'),
        ("Diğer", 'Diğer'),
    ]

class Soru(models.Model):
    soran=models.CharField(max_length=230)
    sorutarihi=models.DateTimeField(auto_now_add=True)
    soru=models.TextField()
    sorukonu= models.CharField(max_length=200,choices=soruchoices,default="Ders ile ilgili bir soru")
    image=models.ImageField(upload_to="Sorular",blank=True,null=True)
    sorustatus= models.CharField(max_length=200,choices=sorustatus,default="Cevaplanmadı")

    class Meta:
        ordering = ['-sorutarihi']

class Cevaplar(models.Model):
    soru=models.ForeignKey(Soru,on_delete=models.CASCADE,null=True)
    cevaptarihi=models.DateTimeField(auto_now_add=True)
    cevaplayan=models.CharField(max_length=230)
    cevap=models.TextField()
    image=models.ImageField(upload_to="Cevaplar",blank=True,null=True)

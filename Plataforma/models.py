from django.db import models

CATEGORIA_CHOICES = {
    
    
    
    
}



class Filmes(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    descricao = models.TextField(verbose_name='Descrição', max_length=1000)
    cartaz = models.ImageField(upload_to='cartazes/')
    
    def __str__(self):
        return self.nome
    
    
 
class Series(models.Model):
    nome = models.CharField(verbose_name='Nome', max_length=50)
    lista_de_episodios = models.ForeignKey()
    def __str__(self):
        return self.nome
    

class Episodios_Serie(models.Model):
    nome = models.CharField(verbose_name='Nome do Episódio', max_length=50)
    def __str__(self):
        return self.nome
class Temporadas_Serie(models.Model):
    pass
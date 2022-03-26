from django.db import models

# Create your models here.
class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30, blank = True, null = True)
    data_cadastro = models.DateField()
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length = 30)
    data_emprestimo = models.DateTimeField()
    data_devolução = models.DateTimeField()
    tempo_duracao = models.DateField()

    class Meta:
        verbose_name = 'Livro'
    
    def __str__(self):
        return self.nome
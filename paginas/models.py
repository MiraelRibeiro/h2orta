from django.db import models

class TabelasDadosUsuario(models.Model):
    id_user = models.OneToOneField('auth.User', on_delete=models.PROTECT, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=False)
    cidade = models.CharField(max_length=255, blank=True, null=False)
    estado = models.CharField(max_length=255, blank=True, null=False)
    pais = models.CharField(max_length=255, blank=True, null=False)
    cep = models.CharField(max_length=12, blank=True, null=False)

    class Meta:
        db_table = 'dados_usuario'


class DadosEstufa(models.Model):
    modelo = models.CharField(max_length=50, blank=True, null=False)
    valor = models.CharField(max_length=50, blank=True, null=False)
    slots = models.CharField(max_length=2, blank=True)
    fileiras = models.CharField(max_length=2, blank=True)
    itensInclusos = models.CharField(max_length=255, blank=True)
    bombaAgua = models.BooleanField()
    tamanhoCM = models.CharField(max_length=10, blank=True)
    estrutura = models.CharField(max_length=20, blank=True)
    imagem = models.CharField(max_length=255, blank=True, null=False)    
    referencia = models.CharField(max_length=2, blank=True)

    class Meta:
        db_table = 'dados_estufa'

   

class EnderecosDeEntrega(models.Model):
    id_user = models.ForeignKey('auth.User', models.DO_NOTHING)
    nome = models.CharField(max_length=255, blank=True, null=False)
    rua = models.CharField(max_length=255, blank=True)
    casa = models.CharField(max_length=10, blank=True)
    cep = models.CharField(max_length=12, blank=True)
    bairro = models.CharField(max_length=255, blank=True)    
    cidade = models.CharField(max_length=255, blank=True, null=False)
    estado = models.CharField(max_length=255, blank=True, null=False)
    pais = models.CharField(max_length=255, blank=True, null=False)

    class Meta:
        db_table = 'dados_entrega'


class TabelasDadosCompra(models.Model):
    id_user = models.ForeignKey('auth.User', models.DO_NOTHING, null=True)
    id_produto = models.ForeignKey(DadosEstufa, models.DO_NOTHING)
    id_entrega = models.ForeignKey(EnderecosDeEntrega, models.DO_NOTHING)
    dataCompra = models.DateField(auto_now=True)
    lembrarDados = models.BooleanField()

    class Meta:
        db_table = 'dados_compra'
from django.forms import ModelForm
from .models import TabelasDadosCompra, TabelasDadosUsuario, EnderecosDeEntrega, DadosEstufa
from django import forms

class PostFormCadastro(forms.ModelForm):
    class Meta:
        model = TabelasDadosUsuario
        fields = '__all__'

class PostFormDadosEstufa(forms.ModelForm):
    class Meta:
        model = DadosEstufa
        fields = '__all__'

class PostFormEnderecosDeEntrega(forms.ModelForm):
    class Meta:
        model = EnderecosDeEntrega
        fields = '__all__'


class PostFormCompra(forms.ModelForm):
    class Meta:
        model = TabelasDadosCompra
        fields = '__all__'
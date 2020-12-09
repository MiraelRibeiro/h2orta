from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import TabelasDadosCompra, TabelasDadosUsuario, DadosEstufa, EnderecosDeEntrega
from .forms import PostFormCadastro
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .backend import MyBackend
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def home(request):    
    return render(request, 'paginas/home.html')

@login_required(login_url='/login/')
def escolhaProduto(request, id):
    normal = DadosEstufa.objects.get(referencia=id, estrutura='Normal')
    media = DadosEstufa.objects.get(referencia=id, estrutura='Média')
    grande = DadosEstufa.objects.get(referencia=id, estrutura='Grande')
    context = {'normal': normal, 'media': media, 'grande':grande}
    return render(request, 'paginas/escolhaProduto.html', context)


def do_login(request):
    if request.method == 'POST':
        if MyBackend.checkUser(username=request.POST['username']) == False:
            messages.warning(request, 'Usuario não existente', extra_tags='warning')
            # Evento back usuario incorreto
        else:
            if MyBackend.checkPassword(username=request.POST['username'], password=request.POST['password']) == False:
                messages.warning(request, 'Senha incorreta', extra_tags='danger')
                # Evento back senha incorreta
        user = MyBackend.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            return render(request, 'paginas/login.html')
    else:
        return render(request, 'paginas/login.html')

def criarConta(request):
    form_user = UserCreationForm()
    form = PostFormCadastro()

    if(request.method == 'POST'):

        form = PostFormCadastro(request.POST)
        form_user = UserCreationForm(request.POST)

        if(form_user.is_valid()):
            form_user.save()

            User.objects.filter(username=request.POST['username']).update(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
            
            try:
                id_User = User.objects.get(username = request.POST['username'])
                cpf = request.POST['cpf']
                cidade = request.POST['cidade']
                estado = request.POST['estado']
                pais = request.POST['pais']
                cep = request.POST['cep']

                dados_usuario = TabelasDadosUsuario(id_user = id_User, cpf= cpf, cidade= cidade, estado=estado, pais=pais, cep=cep)
                dados_usuario.save()

                messages.success(request, "Cadastro Efetuado com Sucesso", extra_tags='success')
                return redirect('/login/')

            except:
                messages.warning(request, "Erro ao efetuar cadastro", extra_tags='warning')
                return render(request, 'paginas/criar_conta.html', {'form': form})            

        else:
            for erro, msg in form_user.errors.items():
                messages.error(request, msg, extra_tags='danger')
            return render(request, 'paginas/criar_conta.html', {'form': form})

    elif(request.method == 'GET'):
        return render(request, 'paginas/criar_conta.html', {'form': form})


    
@login_required(login_url='/login/')
def comprar(request, id):
    form = EnderecosDeEntrega()

    if(request.method == 'POST'):

        form = EnderecosDeEntrega(request.POST)
        # try:     
        print(request.POST)      
        nome = request.POST['nome']
        rua = request.POST['rua']
        casa = request.POST['casa']
        cep = request.POST['cep']
        bairro = request.POST['bairro']
        cidade = request.POST['cidade']
        estado = request.POST['estado']
        pais = request.POST['pais'] 
        produto = DadosEstufa.objects.get(pk=id)
        lembrarFunc = lambda lembrar: True if lembrar == 'on' else False

        dados_entrega = EnderecosDeEntrega(id_user = request.user, nome= nome, rua= rua, casa= casa, cep=cep, bairro= bairro, cidade= cidade, estado=estado, pais=pais)
        dados_entrega.save()
        
        dados_compra = TabelasDadosCompra(id_user= request.user, id_produto=produto, id_entrega= dados_entrega, lembrarDados=lembrarFunc(request.POST['lembrar']))
        dados_compra.save()

        messages.success(request, "Compra feita com Sucesso. Confira os dados no seu Email cadastrado.", extra_tags='success')
        return redirect('../visualizacao/'+ str (dados_compra.pk))

        # except:
        #     messages.warning(request, "Erro ao inserir dados", extra_tags='warning')
        #     return render(request, 'paginas/comprar.html', {'form': form})

    else:
        estufa = DadosEstufa.objects.get(id=id)  
        context = {'dados': estufa}  
        return render(request, 'paginas/comprar.html', context)
        

@login_required(login_url='/login/')
def dadosFinais(request, id):
    compra = TabelasDadosCompra.objects.get(pk=id)
    context = {'compra': compra}
    return render(request, 'paginas/visualizacaoCompra.html', context)

@login_required(login_url='/login/')
def do_logout(request):
    logout(request)
    return redirect('../home/')

@login_required(login_url='/login/')
def delete_user(request):
    instance = TabelasDadosUsuario.objects.get(id_user=request.user.pk)
    instance.delete()
    
    instance = User.objects.get(pk=request.user.pk)
    instance.delete()
    
    return redirect('../home/')

@login_required(login_url='/login/')
def alterar_senha(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso')
            return redirect('/home')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'paginas/alterarSenha.html', {'form': form})

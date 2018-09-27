from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Annonser, Brukerinformasjon, Utviklere, Søknader, Emne, Annonse_emne
from .forms import UserForm, AnnonseForm, AddinfoForm, UtviklerForm, SøknadForm, SortForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    annonser = Annonser.objects.all().order_by('-dato')[:4]
    utviklere = Utviklere.objects.all().order_by('-dato')[:4]


    if not request.user.is_authenticated():
        return render(request, 'index_gjest.html', {'annonser':annonser, 'utviklere':utviklere})
    else:

        return render(request, 'index.html', {'annonser':annonser, 'utviklere':utviklere})

def ny_annonse(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html', )
    else:
        form = AnnonseForm(request.POST or None)
        if form.is_valid():
            annonse = form.save(commit=False)
            annonse.user = request.user
            annonse.save()
            annonser = Annonser.objects.all().order_by('-dato')[:10]
            return redirect('/')

    context = {
        "form": form,
    }
    return render(request, 'ny_annonse.html', context)

def annonser(request):
    if not request.user.is_authenticated():
        annonser = Annonser.objects.all().order_by('-dato')
        paginator = Paginator(annonser, 10)

        page = request.GET.get('page')

        try:
            annonse = paginator.page(page)

        except PageNotAnInteger:
            # Deliver first page
            annonse = paginator.page(1)

        except EmptyPage:
            annonse = paginator.page(paginator.num_pages)

        return render(request, 'annonser_gjest.html', {'annonse': annonse}, )

    else:
        form = SortForm(request.POST or None)
        if form.is_valid():
            filter = form.cleaned_data['sorter']
            liste = []
            for i in filter:
                print(i)

            annonser = Annonser.objects.filter(tags__icontains=filter)
            paginator = Paginator(annonser, 10)

            page = request.GET.get('page')

            try:
                annonse = paginator.page(page)

            except PageNotAnInteger:
                #Deliver first page
                annonse = paginator.page(1)

            except EmptyPage:
                annonse = paginator.page(paginator.num_pages)

            return render(request, 'annonser.html', {'annonse': annonse,'form':form} )
        else:
            annonser = Annonser.objects.all().order_by('-dato')
            paginator = Paginator(annonser, 10)

            page = request.GET.get('page')

            try:
                annonse = paginator.page(page)

            except PageNotAnInteger:
                # Deliver first page
                annonse = paginator.page(1)

            except EmptyPage:
                annonse = paginator.page(paginator.num_pages)

            return render(request, 'annonser.html', {'annonse': annonse, 'form':form}, )


def spesifikk_annonse(request, annonser_id):
    if not request.user.is_authenticated():
        annonse = get_object_or_404(Annonser, pk=annonser_id)

        return render(request, 'spesifikk_annonse_gjest.html', {'annonse': annonse})
    else:

        annonse = get_object_or_404(Annonser, pk=annonser_id)

        return render(request, 'spesifikk_annonse.html', {'annonse':annonse})
def min_profil(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html')
    else:
        info = User.objects.filter(username=request.user.username)
        extrainfo = Brukerinformasjon.objects.filter(user=request.user)
        annonser = Annonser.objects.filter(user=request.user).order_by('-dato')
        søknader = Søknader.objects.filter(søker=request.user)

        return render(request, 'min_profil.html', {'info':info, 'extrainfo':extrainfo, 'annonser':annonser, 'søknader':søknader})

def mine_annonser(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html')
    else:
        annonse = Annonser.objects.filter(user=request.user).order_by('-dato')

        return render(request, 'mine_annonser.html', {'annonse':annonse})



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                annonser = Annonser.objects.all().order_by('-dato')[:10]
                return render(request, 'index.html', {'annonser': annonser})
            else:
                return render(request, 'account/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'account/login.html', {'error_message': 'Invalid login'})
    return render(request, 'account/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                annonser = Annonser.objects.all().order_by('-dato')[:10]
                return render(request, 'index.html', {'annonser': annonser})
    context = {
        "form": form,
    }
    return render(request, 'account/signup.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'logged_out.html', {})

def rediger_profil(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html')
    else:
        form = AddinfoForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user

            data.save()


            info = User.objects.filter(username=request.user.username)
            extrainfo = Brukerinformasjon.objects.filter(user=request.user)


            return render(request, 'min_profil.html', {'info':info, 'extrainfo':extrainfo})


        else:
            return render(request, 'rediger_profil.html', {'form':form})

def ny_utvikler(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html', )
    else:
        form = UtviklerForm(request.POST or None)
        if form.is_valid():
            utvikler = form.save(commit=False)
            utvikler.user = request.user
            utvikler.save()
            annonser = Annonser.objects.all().order_by('-dato')[:10]
            return redirect('/')

    context = {
        "form": form,
    }
    return render(request, 'ny_utvikler.html', context)

def utviklere(request):
    if not request.user.is_authenticated():
        utviklere = Utviklere.objects.all().order_by('-dato')
        paginator = Paginator(utviklere, 10)

        page = request.GET.get('page')

        try:
            utviklere = paginator.page(page)

        except PageNotAnInteger:
            # Deliver first page
            utviklere = paginator.page(1)

        except EmptyPage:
            utviklere = paginator.page(paginator.num_pages)

        return render(request, 'utviklere_gjest.html', {'utviklere': utviklere}, )

    else:

        utviklere = Utviklere.objects.all().order_by('-dato')
        paginator = Paginator(utviklere, 10)

        page = request.GET.get('page')

        try:
            utviklere = paginator.page(page)

        except PageNotAnInteger:
            # Deliver first page
            utviklere = paginator.page(1)

        except EmptyPage:
            utviklere = paginator.page(paginator.num_pages)

        return render(request, 'utviklere.html', {'utviklere': utviklere}, )

def spesifikk_utviklere(request, utviklere_id):
    if not request.user.is_authenticated():
        utvikler = get_object_or_404(Utviklere, pk=utviklere_id)

        return render(request, 'spesifikk_utvikler_gjest.html', {'utvikler': utvikler})
    else:

        utvikler = get_object_or_404(Utviklere, pk=utviklere_id)

        return render(request, 'spesifikk_utvikler.html', {'utvikler': utvikler})

def slett_annonse(request, annonser_id):
    annonse_slett = Annonser.objects.get(pk=annonser_id)
    annonse_slett.delete()
    annonse = Annonser.objects.filter(user=request.user)

    return render(request, 'mine_annonser.html', {'annonse':annonse})

def søknad(request, annonser_id):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html', )
    else:
        form = SøknadForm(request.POST or None)
        if form.is_valid():
            søknad_skjema = form.save(commit=False)
            søknad_skjema.søker = request.user
            søknad_skjema.annonse = get_object_or_404(Annonser, pk=annonser_id)

            søknad_skjema.save()

            annonser = Annonser.objects.all().order_by('-dato')[:10]
            return render(request, 'index.html', {'annonser': annonser})
        context = {
            "form": form,
        }
        return render(request, 'søknad.html', context)

def søknader(request, søknader_id):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html', )
    else:
        vis_søknader = Søknader.objects.filter(annonse=søknader_id)

        return render(request, 'spesifikk_søknad.html', {'vis_søknader':vis_søknader})

def mine_søknader(request):
    if not request.user.is_authenticated():
        return render(request, 'account/login.html', )
    else:
        søknader = Søknader.objects.filter(søker=request.user)

        return render(request,'mine_søknader.html',{'søknader':søknader})
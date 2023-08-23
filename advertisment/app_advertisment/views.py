from django.shortcuts import render, redirect
from .models import Advertisement
from django.contrib.auth.decorators import login_required
from .forms import AdvertisementForm
from django.urls import reverse,reverse_lazy


def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'adv/index.html', context)

def top_sellers(request):
    return render(request, 'adv/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main_page')
            return redirect(url)
    else:
        form = AdvertisementForm()

    form = AdvertisementForm()
    context = {'form': form}
    return render(request, 'adv/advertisement_post.html', context)

def register(request):
    return render(request, 'auth/register.html')

def login(request):
    return render(request, 'auth/login.html')

def profile(request):
    return render(request, 'auth/profile.html')
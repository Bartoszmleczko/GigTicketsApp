from django.shortcuts import render
from django.template import RequestContext
from zespol import models as z
from zespol.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views.generic import DetailView
from zespol.forms import SignUpForm,ProfileForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User, PermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied

@login_required
def index(request):
    if request.user.is_authenticated:
        username = request.user.username
    concert_list = Concert.objects.all().order_by('date')[:5:1]
    return render(request,'homepage.html',{'lista' : concert_list,'username':username})

@login_required
def club_details(request, club_id):
    club = Club.objects.get(pk = club_id)
    concerts = club.concert_set.all()
    return render(request,'club_details.html',{'concerts': concerts,'club':club})

@login_required
def band_details(request,band_id):
    band = Band.objects.get(pk=band_id)
    concerts = band.concert_set.all()
    return render(request,'band_details.html',{'concerts':concerts,'band':band})


class ConcertDetail(DetailView,LoginRequiredMixin):
    model = Concert
    template_name = 'concert_detail.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(username=self.request.user)
        context['suggested'] = Concert.objects.all().order_by('date')[:3:1]

        user =  User.objects.get(username=self.request.user)
        return context


@login_required
def thanks(request,concert_id):
    ticket = Ticket.objects.create(profile=request.user.profile,concert_id=concert_id)
    concert = Concert.objects.get(pk=concert_id)
    concert.normal_tickets -= 1
    concert.save()
    print(ticket)
    return redirect(index)


@login_required
def delete(request, ticket_id):
    ticket = Ticket.objects.get(pk = ticket_id)
    if ticket.is_bought == False:
        concert = ticket.concert
        concert.normal_tickets +=1
        concert.save()
        ticket.delete()
    return redirect(cart)

@login_required
def buy(request, ticket_id):
    ticket = Ticket.objects.get(pk = ticket_id)
    is_bought = ticket.is_bought
    ticket.is_bought = True
    ticket.save()
    return redirect(cart)


class PostDelete(DeleteView,LoginRequiredMixin,PermissionsMixin):
    model = Ticket
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = User.objects.get(username=self.request.user)
        context['suggested'] = Concert.objects.all().order_by('date')[:3:1]
        user = self.request.user
        tickets = user.profile.ticket_set
        user =  User.objects.get(username=self.request.user)
        return context

class PermissionMixin(object):

        def get_object(self, *args, **kwargs):
            obj = self.get_object(*args, **kwargs)


            if not obj.created_by == self.request.user:
                raise PermissionDenied()
            else:

                return obj

@login_required
def deleteall(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.all().filter(profile=request.user.profile)

    for ticket in tickets:
        if ticket.is_bought == False:
            concert = ticket.concert
            concert.normal_tickets += 1
            concert.save()
            ticket.delete()
    return redirect(cart)

@login_required
def buyall(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.all().filter(profile=request.user.profile)

    for ticket in tickets:
        ticket.is_bought=True
        ticket.save()
    return redirect(cart)
@login_required
def cart(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.all().filter(profile=request.user.profile)

    sum = 0

    for price in tickets:
        if price.is_bought == False:
            sum += price.concert.ticket_price

    return render(request,'cart.html',{'tickets': tickets,'total_price':sum})

@login_required
def bands(request):
    band_list = Band.objects.all()
    return render(request,'bands.html',{'bands':band_list})

@login_required
def concerts(request):
    concert_list = Concert.objects.all()
    return render(request,'concerts.html',{'concerts':concert_list})

@login_required
def clubs(request):
    club_list  = Club.objects.all()
    return render(request,'clubs.html',{'clubs': club_list})

@login_required
def profile(request):
    profile = request.user.profile
    tickets = Ticket.objects.all().filter(profile=request.user.profile)
    return render(request,'profile.html',{'profile':profile,'tickets':tickets})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.profile.first_name=form.cleaned_data.get('first_name').strip()
            user.profile.last_name=form.cleaned_data.get('last_name').strip()
            user.profile.email=form.cleaned_data.get('email').strip()
            user.save()

            raw_password = form.cleaned_data.get('password1').strip()


            return redirect('/accounts/login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def update_profile(request):
    suggested = Concert.objects.all().order_by('date')[:3:1]
    if(request.method == 'POST'):
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(profile)
    else:
        profile_form  = ProfileForm(instance=request.user.profile)
        return render(request,'profile_update.html',{'profile_form':profile_form,'suggested': suggested})
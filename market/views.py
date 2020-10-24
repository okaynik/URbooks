from django.utils import timezone
from .models import Item
from django.shortcuts import render, get_object_or_404
from .forms import ItemForm#, CustomUserCreationForm#, UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.core.exceptions import ValidationError
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

User = get_user_model()

def register(request):
    context = {}
    form = CustomUserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
            return render(request, 'market/post_list.html', {'items': items})
    context['form']=form
    return render(request,'market/register.html')

# def login_request(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {email}")
#                 return redirect('/')
#             else:
#                 messages.error(request, "Invalid username or password1.")
#         else:
#             messages.error(request, "Invalid username or password2.")
#     form = AuthenticationForm()
#     return render(request, 'market/login.html', {'form':form})

def image_view(request):
	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('success')
	else:
		form = ItemForm()
		return render(request, 'image_form.html', {'form' : form})

def success(request):
	return HttpResponse('successfully uploaded')

def post_list(request):
    items = Item.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'market/post_list.html', {'items': items})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'market/item_detail.html', {'item': item})

def item_new(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.created_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm()
    return render(request, 'market/item_edit.html', {'form': form})

def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.created_date = timezone.now()
            item.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=post)
    return render(request, 'market/item_edit.html', {'form': form})
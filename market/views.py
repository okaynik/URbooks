from django.utils import timezone
from .models import Item
from django.shortcuts import render, get_object_or_404
from .forms import ItemForm
from django.shortcuts import redirect

# Create your views here.
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
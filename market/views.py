from django.shortcuts import render
from django.utils import timezone
from .models import Item
from django.shortcuts import render, get_object_or_404

# Create your views here.
def image_view(request):
	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)

		if form.is_valid():
			form.save
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
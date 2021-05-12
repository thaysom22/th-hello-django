from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()  # Django auto generates id for each item
    context = {
        "items": items
    }
    return render(request, "todo/todo_list.html", context)


def add_item(request):
    # determine whether request to add url is POST (same syntax as flask)
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

        # OLD WAY OF EXECUTING POST FUNCTIONALITY #
        # get data from form (flask syntax is request.form.get)
        # name = request.POST.get("item_name")
        # done = "done" in request.POST  # OR request.POST.get("done")
        
        # use Model class to create a new item
        # Item.objects.create(name=name, done=done)
        
        # return GET redirect to get_todo_list URL  
        # return redirect("get_todo_list")

    # GET #
    # create instance of ItemForm class and include empty form in context
    form = ItemForm()
    context = {
        'form': form
    }

    return render(request, "todo/add_item.html", context)


def edit_item(request, item_id):
    """
    item_id is parameter attached to 'edit/' url
    """
    # first, get item data from db
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        # get data from form and update Item instance
        form = ItemForm(request.POST, instance=item) 
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')

    # GET #        
    form = ItemForm(instance=item)  # pass item from db as instance kwarg to prepopulate form
    context = {
        'form': form
    }

    return render(request, "todo/edit_item.html", context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()

    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    
    return redirect('get_todo_list')
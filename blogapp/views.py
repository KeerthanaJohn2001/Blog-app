from django.shortcuts import render, redirect
from blogapp.forms import BlogForm
from blogapp.models import Blog

def emp(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
         try: 
            form.save()
            return redirect('/show')
         except:
             pass
    else:
        form = BlogForm()
    return render(request, 'index.html', {'form': form})
def show(request):
    dblogs = Blog.objects.all()
    return render(request, "show.html", {'dblogs': dblogs})
def edit(request, id):
    dblog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'dblog': dblog})
def update(request, id):
    dblog = Blog.objects.get(id=id)
    form = BlogForm(request.POST, instance=dblog)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'dblog': dblog})
def destroy(request, id):
    dblog = Blog.objects.get(id=id)
    dblog.delete()
    return redirect('/show')

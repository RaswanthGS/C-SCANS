from unicodedata import name
from django.shortcuts import redirect, render
from .models import Contact
from .forms import PostForm

def main(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/')
    else:
        form = PostForm()

        
    context = {
        'forms':form
    }
    return render(request, 'blog/main.html', context)


def app(request):
    return render(request, 'blog/appoinment.html')

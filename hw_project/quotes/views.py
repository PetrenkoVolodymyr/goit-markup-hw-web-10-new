from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

from .models import Author, Tag, Quote
from .forms import TagForm, AuthorForm

def main(request, page = 1):
    quotes = Quote.objects.all()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
   
    return render(request,'quotes/index.html', context={'quotes':quotes_on_page})

def detail(request, quote_id):
    author = get_object_or_404(Author, pk=quote_id)
    return render(request, 'quotes/detail.html', {"author": author})

def tags(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    quotes = Quote.objects.filter(tags=tag)
    return render(request, 'quotes/tags.html', context={"quotes": quotes, "tag": tag})

def addtag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/addtag.html', {'form': form})

    return render(request, 'quotes/addtag.html', {'form': TagForm()})


def addauthor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:root')
        else:
            return render(request, 'quotes/addauthor.html', {'form': form})

    return render(request, 'quotes/addauthor.html', {'form': AuthorForm()})



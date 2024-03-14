import random
from django.shortcuts import render, HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
from markdown2 import Markdown

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Page title", widget=forms.TextInput(attrs={'class': 'form-control col-md-8 col-lg-8'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control col-md-8 col-lg-8', 'rows': 10}))
    edit = forms.BooleanField(initial=False, widget=forms.HiddenInput(), required=False)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def search(request):
    value = request.GET.get('q', '')
    entry_page = util.get_entry(value)
    if entry_page is not None:
        return HttpResponseRedirect(reverse("entry", kwargs={'entry': value}))
    else:
        sub_string_entries = [entry for entry in util.list_entries() if value.upper() in entry.upper()]
        return render(request, "encyclopedia/index.html", {
            "entries": sub_string_entries,
            "search": True,
            "value": value
        })


def new_page(request):
    form = NewEntryForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        if util.get_entry(title) is None or form.cleaned_data["edit"]:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("entry", kwargs={'entry': title}))
        else:
            return render(request, "encyclopedia/newPage.html", {
                "form": form,
                "existing": True,
                "entry": title
            })
    return render(request, "encyclopedia/newPage.html", {
        "form": form,
        "existing": False
    })    

def edit(request, entry):
    entry_page = util.get_entry(entry)
    if entry_page is None:
        return render(request, "encyclopedia/error.html", {
            "entryTitle": entry    
        })
    else:
        form = NewEntryForm(initial={'title': entry, 'content': entry_page, 'edit': True})
        return render(request, "encyclopedia/newPage.html", {
            "form": form,
            "edit": True,
            "entryTitle": entry
        })        

def random_page(request):
    random_entry = random.choice(util.list_entries())
    return HttpResponseRedirect(reverse("entry", kwargs={'entry': random_entry}))

def entry(request, entry):
    markdowner = Markdown()
    entry_page = util.get_entry(entry)
    if entry_page is None:
        return render(request, "encyclopedia/error.html", {
            "entryTitle": entry    
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entry_page),
            "entryTitle": entry
        })
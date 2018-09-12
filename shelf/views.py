from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from .models import Treasure, File_Treasure
from .forms import TreasureForm, File_TreasureForm
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('treasure_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def treasure_list(request):
    treasures = Treasure.objects.all()
    return render(request, 'shelf/treasure_list.html', {'treasures': treasures})

def treasure_detail(request, pk):
    treasure = Treasure.objects.get(id=pk)
    return render(request, 'shelf/treasure_detail.html', {'treasure': treasure})

def treasure_create(request):
    if request.method == 'POST':
         form = TreasureForm(request.POST)
         if form.is_valid():
            treasure = form.save()
            return redirect('treasure_detail', pk=treasure.pk)
    else:
        form = TreasureForm()
    return render(request, 'shelf/treasure_form.html', {'form': form})

def treasure_edit(request, pk):
    treasure = Treasure.objects.get(pk=pk)
    if request.method == "POST":
        form = TreasureForm(request.POST, instance=treasure)
        if form.is_valid():
            treasure = form.save()
            return redirect('treasure_detail', pk=treasure.pk)
    else:
        form = TreasureForm(instance=treasure)
    return render(request, 'shelf/treasure_form.html', {'form': form})


def treasure_delete(request, pk):
    Treasure.objects.get(id=pk).delete()
    return redirect('treasure_list')

def file_treasure_detail(request, pk):
    file_treasure = File_Treasure.objects.get(id=pk)
    return render(request, 'shelf/file_treasure_detail.html', {'file_treasure': file_treasure})

def file_treasure_list(request):
    file_treasures = FileTreasure.objects.all()
    return render(request, 'shelf/treasure_list.html', {'file_treasures': file_treasures})


def file_treasure_create(request):
    if request.method == 'POST':
         form = File_TreasureForm(request.POST, request.FILES)
         if form.is_valid():
            file_treasure = form.save()
            return redirect('file_treasure_detail', pk=file_treasure.pk)
    else:
        form = File_TreasureForm()
    return render(request, 'shelf/file_treasure_form.html', {'form': form})
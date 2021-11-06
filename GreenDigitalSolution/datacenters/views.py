from django import forms
from django.core import paginator
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import DataCenterForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



import datacenters

from .models import DataCenter

@login_required
def HardManager(request):

    search = request.GET.get('search')

    if search:
        datacenters = DataCenter.objects.filter(titulo__icontains=search)
    else:    

        datacenters_list = DataCenter.objects.all().order_by('-created_at')

        paginator = Paginator(datacenters_list, 3)

        page = request.GET.get('page')

        datacenters = paginator.get_page(page)

    return render(request, 'datacenters/equips.html', {'datacenters': datacenters})

@login_required
def DataCenterView(request, id):
    datacenter = get_object_or_404(DataCenter, pk=id)
    return render(request, 'datacenters/dataEquip.html', {'datacenter': datacenter})

@login_required
def NewEquip(request):
    kami = DataCenterForm()
    if request.method == 'POST':
        form = DataCenterForm(request.POST)

        if form.is_valid():
            datacenter = form.save(commit=True)
            datacenter.save()
            return redirect('/')

    else:                  
        form = DataCenterForm()
        return render(request, 'datacenters/newEquip.html', {'form': form})

@login_required
def editDataCenter(request, id):
    datacenter = get_object_or_404(DataCenter, pk=id)
    form = DataCenterForm(instance=datacenter)

    if request.method == 'POST':
        form = DataCenterForm(request.POST, instance=datacenter)
        if form.is_valid():
            datacenter.save()
            return redirect('/')
        else:
            return render(request, 'datacenters/editDataCenter.html', {'form': form, 'datacenter': datacenter})
    else:
        return render(request, 'datacenters/editDataCenter.html', {'form': form, 'datacenter': datacenter})

@login_required
def deleteDataCenter(request, id):
    datacenter = get_object_or_404(DataCenter, pk=id)
    datacenter.delete()

    messages.info(request, 'Dispositivo deletado com sucesso.')

    return redirect('/')

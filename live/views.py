from django.shortcuts import render
from django.views.generic import ListView
from .models import *
import json

# Create your views here.

class InfoList(ListView):
    model=Info
    template_name="index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["qs_json"]=json.dumps(list(Info.objects.values()))
        return context
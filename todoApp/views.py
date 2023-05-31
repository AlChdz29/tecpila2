from django.shortcuts import redirect
import uuid


def index(request):
    return redirect('/todos')
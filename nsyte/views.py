from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# @login_required
def mainpage(request):
    return render(request, "base.html")
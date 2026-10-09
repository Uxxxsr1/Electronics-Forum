from django.shortcuts import render

# Create your views here.

# render main page
def index_html(request):
    return render(request, 'main/index.html')

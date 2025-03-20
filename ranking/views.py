from django.shortcuts import render

# Create your views here.
def ranking_list(request):
    return render(request, 'ranking/ranking_list.html')
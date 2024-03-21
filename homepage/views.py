from django.shortcuts import render

# Create your views here.
def homepage(request):
    """
    Display all events
    """

    return render(request, 'base.html',   
    )
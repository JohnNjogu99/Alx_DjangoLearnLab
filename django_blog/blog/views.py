from django.shortcuts import render

def home(request):
    # Render the template blog/index.html when someone visits this view
    return render(request, 'blog/index.html')

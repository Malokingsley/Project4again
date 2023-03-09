from django.shortcuts import render

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# Add new view

def toolbox_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'toolboxes/index.html'
  )

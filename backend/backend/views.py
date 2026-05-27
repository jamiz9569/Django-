from django.http import HttpResponse
"""
# http is a module in Django that provides classes and functions for handling HTTP requests and responses.  
# HttpResponse is a class that represents an HTTP response. It is used to send data back to the client in response to an HTTP request.
# In this case, we are using it to send a simple "Hello, World!" message back to the client when they access the home view.

"""
from django.shortcuts import render
"""
shortcut is a module in Django that provides functions for rendering templates and handling HTTP requests.
render is a function that takes an HTTP request and a template name, and returns an HttpResponse
"""
def home(request):
   # return HttpResponse("this is the home page.")
    return render(request, 'website/index.html') 

def about(request):
    
    return render(request, 'website/index_1.html')

def contact(request):
    return render(request, 'website/index_2.html')

# route is defined in urls.py file, we will create a url pattern for each view function and map it to the corresponding URL.



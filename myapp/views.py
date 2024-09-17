from django.shortcuts import render

# Create your views here.
def setcookes(request):
    respose= render(request,'myapp/getcookies.html')
    respose.set_cookie('name','ankit')
    return respose
def getcookes(request):
    name=request.COOKIES['name']
    return render(request,'myapp/getcookies.html',{'fm':name})



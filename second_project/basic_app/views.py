from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict={'text':'Hello This is custom Filter','number':100}
    return render(request,'basic_app/index.html',context=my_dict)

def other(request):
    return render(request,'basic_app/others.html')

def urltemplate(request):
    return render(request,'basic_app/url_template.html')

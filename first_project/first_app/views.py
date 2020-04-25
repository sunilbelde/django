from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import User,AccessRecord,WebPage,Topic
from . import forms
from first_app.forms import NewUserForm
# Create your views here.

def index(request):
    my_dict={'inserted_data':'This is inserted data from view.py'}
    return render(request,'first_app/index.html',context=my_dict)
def test(request):
    return HttpResponse('Test Call')

def table(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request,'first_app/index_table.html',context=date_dict)


def form_name_view(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            print("Validated")
            print("Name :"+form.cleaned_data['name'])
            print("Email :"+form.cleaned_data['email'])
            print("Text :"+form.cleaned_data['text'])


    return render(request,'first_app/forms.html',{'form':form})

def user_view(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {"users":user_list}
    return render(request,'first_app/users.html',context=user_dict)

def add_user(request):
    form= NewUserForm()

    if request.method == 'POST':
        form=NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return user_view(request)

        else:
            raise forms.ValidationError("Error Occured")
    return render(request,'first_app/add_user.html',{'form':form})

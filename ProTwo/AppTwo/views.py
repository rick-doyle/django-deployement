from django.shortcuts import render

from django.http import HttpResponse

from AppTwo.models import User
from AppTwo.form import NewUserForm



def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    '''
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request,'AppTwo/users.html',context = user_dict)
    '''
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("INVALID FORM ")

    return render(request,'AppTwo/users.html',{'form':form})




# Create your views here.

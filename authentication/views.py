from django.shortcuts import render,redirect
from authentication.models import CustomUser,UserForm
# Create your views here.
def all_users(request):
    content=CustomUser.objects.all()
    return render(request,'user/all_users.html',{"content":content})
def add_user(request,id=0):
    if request.method == "GET":
        if id==0:
            form = UserForm()
            submit = "Add"
        else:
            user = CustomUser.objects.get(pk=id)
            form = UserForm(instance=user)
            submit = "Update"
        context = {'form': form,
                   'submit': submit}
        return render(request, 'user/add_user.html', context)
    else:
        if id==0:
            form = UserForm(request.POST)
        else:
            user = CustomUser.objects.get(pk=id)
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('/users/all_users/')
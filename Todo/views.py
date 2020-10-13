# views.py->internal working
from django.shortcuts import render,redirect
from .models import  Todo
from datetime import date
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# ***************************************************************************************************************
#LOGIN PAGE
# ***************************************************************************************************************
def index(request):
    context = {}
    return render(request, 'login.html',context);

# ***************************************************************************************************************
# hOME PAGE
# ***************************************************************************************************************
@login_required(login_url='/register')
def home(request):
    print(request.user)
   #all data in the database
    if request.method== "POST":
        allData = []
        # data = Todo.objects.values()
        data=Todo.objects.filter(name=request.user)
        for cat in data:
            allData.append(cat)

    # all data in the database
    if request.method == "GET":
        allData = []
        sortacc = request.GET.get('sortacc')

        if(sortacc=='Status'):
            data = Todo.objects.filter(name=request.user).order_by("status")
            for cat in data:
                allData.append(cat)
            params = {'allData': allData}
            return render(request, 'home.html', params)

        if (sortacc == 'Labels'):
            data = Todo.objects.filter(name = request.user).order_by("labels")
            for cat in data:
                allData.append(cat)
            params = {'allData': allData}
            return render(request, 'home.html', params)

        if (sortacc == 'Priority'):
            data = Todo.objects.filter(name = request.user).order_by("priority")
            for cat in data:
                allData.append(cat)
            params = {'allData': allData}
            return render(request, 'home.html', params)

        if (sortacc == 'Date'):
            data = Todo.objects.filter(name=request.user).order_by("date1")
            for cat in data:
                print(cat)
                allData.append(cat)
            params = {'allData': allData}
            return render(request, 'home.html', params)


    # appply filters according to date,label,status,priority
    if request.method == "GET":
        a=date.today()
        date1 = request.GET.get('date1',a)
        label = request.GET.get('label','')
        status = request.GET.get('status','')
        priority = request.GET.get('priority','')
        allData=[]
        d = Todo.objects.filter(status=status, labels=label, priority=priority,date1=date1,name=request.user)
        for d1 in d:
            allData.append(d1)
        params = {'allData': allData}
        return render(request, 'home.html', params)

    params = {'allData': allData}
    return render(request, 'home.html',params)

# ***************************************************************************************************************
# REGISTER PAGE
# ***************************************************************************************************************
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # add data to the database
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account created for'+user)
    context = {'form': form}
    return render(request, 'register.html',context)

# ***************************************************************************************************************
# TODOPAGE
# ***************************************************************************************************************
@login_required(login_url='/register')
def todo(request):
    # on login validation is applied
    params={}

    # add data to the todo list....
    if request.method == "GET":
        task = request.GET.get('task','')
        date1 = request.GET.get('date1','')
        label = request.GET.get('label','')
        status = request.GET.get('status','')
        priority = request.GET.get('priority','')
        if((task!="") and (date1!="") and (label!="") and (status!="") and (priority!="")):
            todo = Todo(task=task,date1=date1,labels=label,status=status,priority=priority,name=request.user)
            todo.save()

        allData = []
        data = Todo.objects.filter(name=request.user).order_by("date1")
        for cat in data:
             allData.append(cat)

        params = {'allData': allData}

    return render(request, 'todo.html',params)


# ***************************************************************************************************************
# delete from database
# ***************************************************************************************************************
@login_required(login_url='/register')
def todo_delete(request,task_id):
    Todo.objects.get(task_id=task_id).delete()
    return redirect('/todo')

# ***************************************************************************************************************
# LOGOUT
# ***************************************************************************************************************
@login_required(login_url='/register')
def logoutuser(request):
    logout(request)
    return redirect("/")

# ***************************************************************************************************************
# AUTHENTICATION
# ***************************************************************************************************************
def login1(request):
    if request.method == "POST":
        username = request.POST.get('name1')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/todo')
            else:
                print("auth failed")
                return redirect('/register')

# ***************************************************************************************************************
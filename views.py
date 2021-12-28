from django.shortcuts import render
from .models import  user_register_table,birth_register_table,death_register_table,marriage_register_table,divorce_register_table,madrasa_register_table,family_register_table
from .models import accounts_table
def index(request):
    return render(request,"index.html")

def user_signup(request):
    return render(request,"user_signup.html")

def user_signup_save(request):
    if request.method=="POST":
        a=user_register_table()
        a.name=request.POST.get("name")
        a.address=request.POST.get("address")
        a.gender=request.POST.get("gender")
        a.email=request.POST.get("email")
        a.phone=request.POST.get("phn")
        a.username=request.POST.get("uname")
        a.password=request.POST.get("pswd")
        a.save()
        return render(request,"login.html")
def login(request):
    return render(request,"login.html")

def login_save(request):
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get("pass")
        if(user_register_table.objects.filter(username=username,password=password).exists()):
            user=user_register_table.objects.get(username=username,password=password)
            request.session['user_name']=user.username
            request.session['user_id']=user.id
            return render(request,"user_home.html")
        elif(username=="admin" and password=="admin"):
            return render(request,"admin_home.html")


def family_register(request):
    return render(request,"family_register.html")

def birth_register(request):
    return render(request,"birth_register.html")

def birth_reg_save(request):
    if request.method=="POST":
        b=birth_register_table()
        b.childname=request.POST.get("cname")
        b.gender=request.POST.get("gender")
        b.birthdate=request.POST.get("bdate")
        b.birthplace=request.POST.get("bplace")
        b.mothername=request.POST.get("mname")
        b.fathername=request.POST.get("fname")
        b.address=request.POST.get("address")
        b.pmc=request.POST.get("pmc")
        b.save()
        return render(request,"user_home.html")

def death_register(request):
    return render(request,"death_register.html")

def death_reg_save(request):
    if request.method=="POST":
        c=death_register_table()
        c.name=request.POST.get("name")
        c.gender=request.POST.get("gender")
        c.age=request.POST.get("age")
        c.deathdate=request.POST.get("ddate")
        c.deathplace=request.POST.get("dplace")
        c.address=request.POST.get("address")
        c.pmc=request.POST.get("pmc")
        c.save()
        return render(request,"user_home.html")
def  marriage_register(request):
    return render(request,"marriage_register.html")

def marriage_reg_save(request):
    if request.method=="POST":
        d=marriage_register_table()
        d.husbandname=request.POST.get("hname")
        d.hdob=request.POST.get("bhdate")
        d.hage=request.POST.get("hage")
        d.wifename=request.POST.get("wname")
        d.wdob=request.POST.get("bwdate")
        d.wage=request.POST.get("wage")
        d.marriagedate=request.POST.get("mdate")
        d.marriageplace=request.POST.get("mplace")
        d.husbandname=request.POST.get("hname")
        d.save()
        return render(request,"user_home.html")

def divorce_register(request):
    return render(request,"divorce_register.html")


def divorce_reg_save(request):
    if request.method=="POST":
        e=divorce_register_table()
        e.husbandname=request.POST.get("hname")
        e.hage=request.POST.get("hage")
        e.wifename=request.POST.get("wname")
        e.wage=request.POST.get("wage")
        e.marriagedate=request.POST.get("mdate")
        e.reason=request.POST.get("resn")
        e.save()
        return render(request,"user_home.html")
def logout(request):
    return render(request,"index.html")

def madrasa_register(request):
    return render(request,"madrasa_register.html")

def madrasa_reg_save(request):
    if request.method=="POST":
        f=madrasa_register_table()
        f.childname=request.POST.get("cname")
        f.gender=request.POST.get("gender")
        f.classs=request.POST.get("cls")
        f.birthdate=request.POST.get("bdate")
        f.parentname=request.POST.get("pname")
        f.address=request.POST.get("address")
        f.save()
        return render(request,"user_home.html")

def family_reg_save(request):
    if request.method=="POST":
        g=family_register_table()
        g.name=request.POST.get("name")
        g.address=request.POST.get("address")
        g.pmc=request.POST.get("pmc")
        g.totalmembers=request.POST.get("tmem")
        g.save()
        return render(request,"user_home.html")

def admin_view_family(request):
    obj1=family_register_table.objects.all()
    return render(request,"admin_view_family.html",{'fdata':obj1})

def admin_view_birthdetail(request):
    obj2=birth_register_table.objects.all()
    return render(request,"admin_view_birthdetail.html",{'birthdata':obj2})


def admin_view_deathdetail(request):
    obj3=death_register_table.objects.all()
    return render(request,"admin_view_deathdetail.html",{'deathdata':obj3})

def admin_view_mrgedetail(request):
    obj4=marriage_register_table.objects.all()
    return render(request,"admin_view_mrgedetail.html",{'mrgedata':obj4})

def admin_view_divorcedetail(request):
    obj5=divorce_register_table.objects.all()
    return render(request,"admin_view_divorcedetail.html",{'dvdata':obj5})

def admin_view_madrasadetail(request):
    obj6=madrasa_register_table.objects.all()
    return render(request,"admin_view_madrasadetail.html",{'mddata':obj6})

def admin_view_accounts(request):
    obj7=accounts_table.objects.all()
    return render(request,"admin_view_accounts.html",{'acdata':obj7})


# Create your views here.

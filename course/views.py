from dataclasses import dataclass
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from .models import login as log,college as cg,course as cs,user as us,mail as ml,fees as fe,registration as re,prospectus as pro

# Create your views here.
def index(request):
    msg=request.GET.get("msg","")
    return render(request,"index.html",{"msg":msg})

def userhome(request):
    msg=request.GET.get("msg","")
    return render(request,"userhome.html",{"msg":msg})

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def courses(request):
    return render(request,"courses.html")

def teacher(request):
    return render(request,"teacher.html")

def adminhome(request):
    msg=request.GET.get("msg","")
    return render(request,"adminhome.html",{"msg":msg})

def privacy(request):
    return render(request,"privacy.html")

def change(request):
    if request.POST:
        oldpsw=request.POST["oldpsw"]
        newpsw=request.POST["newpsw"]
        id=request.session['id']
        log.objects.filter(logid=id,password=oldpsw).update(password=newpsw)
        if(request.session.get('role', ' ')=="admin"):
           response=redirect("/adminhome?msg=Password updated successfully")
           return response
        elif(request.session.get('role', ' ')=="user"):
           response=redirect("/userhome?msg=Password updated successfully")
           return response

def login(request):
     if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            datac = log.objects.filter(username=username, password=password).count()
            if datac==1:
                data=log.objects.get(username=username, password=password)
                if data.role=="admin":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/adminhome?msg=welcome admin')
                    return response
                elif data.role=="user":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/userhome?msg=Welcome user')
                    return response
                else :
                    response = redirect('/index?msg=invalid access')
                    return response


            else:
                response = redirect('/index?msg=invalid username or password')
                return response
               
        except:
            response = redirect('/index?msg=something went wrong')
            return response
     else:
        response = redirect('/index?msg=exception occured')
        return response

def reg(request):
    if request.POST:
      username=request.POST["username"]
      address=request.POST["address"]
      phoneno=request.POST["phoneno"]
      date=request.POST["date"]
      photo=request.FILES["photo"]
      qualification=request.POST["qualification"]
      password=request.POST["password"]
    
      log.objects.create(username=username,password=password,role="user")
      datal=log.objects.last()
      us.objects.create(login=datal,username=username,address=address,phoneno=phoneno,date=date,photo=photo,qualification=qualification)
      response = redirect('/index?msg=Registration successfull')
      return response
    else:
        response = redirect("/index?msg=Registration failed")
        return response

def logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index?id=logout")
        return response
    except:
        response = redirect("/index?id=logout")
        return response

def adminhead(request):
    return render(request,"adminhead.html")

def addcollege(request):
    msg=request.GET.get("msg","")
    return render(request,"addcollege.html",{"msg":msg})

def college(request):
    if request.POST:
        name=request.POST["name"]
        phoneno=request.POST["phoneno"]
        email=request.POST["email"]
        address=request.POST["address"]
        location=request.POST["location"]
        year=request.POST["year"]
        logo=request.FILES["logo"]
        photo=request.FILES["photo"]
        cg.objects.create(name=name,phoneno=phoneno,email=email,address=address,location=location,year=year,logo=logo,photo=photo)
        response=redirect("/addcollege?msg=New college added successfully")
        return response
    else:
        response=redirect("/addcollege?msg=Operation failed")
        return response

def collegelist(request):
    msg=request.GET.get("msg","")
    datac=cg.objects.all()
    return render(request,"collegelist.html",{"datac":datac,"msg":msg})

def deletecollege(request):
    id=request.POST["cid"]
    cg.objects.filter(collegeid=id).delete()
    response = redirect("/collegelist?msg=College deleted successfully")
    return response

def editcollege(request):
    id=request.POST["cid"]
    name=request.POST["name"]
    address=request.POST["address"]
    phoneno=request.POST["phoneno"]
    location=request.POST["location"]
    email=request.POST["email"]
    cg.objects.filter(collegeid=id).update(name=name,address=address,phoneno=phoneno,location=location,email=email)
    response = redirect("/collegelist?msg=Updated Successfully")
    return response

def addcourse(request):
    msg=request.GET.get("msg","")
    data=cg.objects.all()
    return render(request,"addcourse.html",{"data":data,"msg":msg})

def course(request):
    if request.POST:
        college=request.POST["college"]
        name=request.POST["name"]
        seats=request.POST["seats"]
        datag=cg.objects.get(collegeid=college)
        cs.objects.create(college=datag,name=name,seats=seats)
        response=redirect("/addcourse?msg=New Course Added successfully")
        return response
    else:
        response=redirect("/addcourse?msg=Operation Failed")
        return response

def courselist(request):
    msg=request.GET.get("msg","")
    datac=cs.objects.all()
    return render(request,"courselist.html",{"datac":datac,"msg":msg})

def deletecourse(request):
    id=request.POST["csid"]
    cs.objects.filter(courseid=id).delete()
    response = redirect("/courselist?msg=Course deleted successfully")
    return response

def editcourse(request):
    id=request.POST["ceid"]
    name=request.POST["name"]
    seats=request.POST["seats"]
    cs.objects.filter(courseid=id).update(name=name,seats=seats)
    response = redirect("/courselist?msg=Updated Successfully")
    return response

def viewmail(request):
    datal=ml.objects.all()
    return render(request,"viewmail.html",{"datal":datal})

def userchange(request):
    return render(request,"userchange.html")

def colleges(request):
    datac=cg.objects.all()
    return render(request,"colleges.html",{"datac":datac})

def usrcourse(request):
    datac=cs.objects.all()
    return render(request,"usrcourse.html",{"datac":datac})

def mail(request):
    msg=request.GET.get("msg","")
    return render(request,"mail.html",{"msg":msg})

def email(request):
    if request.POST:
        username=request.POST["username"]
        subject=request.POST["subject"]
        mail=request.POST["mail"]
        ml.objects.create(username=username,subject=subject,mail=mail)
        response=redirect("/mail?msg=Submitted Successfully")
        return response
    else:
        response=redirect("/mail?msg=operation failed")
        return response

def profile(request):
    msg=request.GET.get("msg","")
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datapf=us.objects.filter(login=datal).all()
    return render(request,"profile.html",{"datapf":datapf,"msg":msg})

def editprofile(request):
    id=request.POST["userid"]
    username=request.POST["username"]
    address=request.POST["address"]
    phoneno=request.POST["phoneno"]
    qualification=request.POST["qualification"]
    us.objects.filter(userid=id).update(username=username,address=address,phoneno=phoneno,qualification=qualification)
    response = redirect("/profile?msg=Updated Successfully")
    return response

def addfee(request):
    msg=request.GET.get("msg","")
    data=cs.objects.all()
    return render(request,"addfee.html",{"data":data,"msg":msg})

def fee(request):
    if request.POST:
        batch=request.POST["batch"]
        course=request.POST["course"]
        fee=request.POST["fee"]
        datac=cs.objects.get(courseid=course)
        fe.objects.create(batch=batch,course=datac,fee=fee)
        response=redirect("/addfee?msg=Successfully added")
        return response
    else:
        response=redirect("/addfee?msg=operation failed")
        return response

def feelist(request):
    msg=request.GET.get("msg","")
    dataf=fe.objects.all()
    return render(request,"feelist.html",{"msg":msg,"dataf":dataf})

def editfee(request):
    id=request.POST["fid"]
    fee=request.POST["fee"]
    fe.objects.filter(feesid=id).update(fee=fee)
    response=redirect("/feelist?msg=Edited successfully")
    return response

def deletefee(request):
    id=request.POST["fid"]
    fe.objects.filter(feesid=id).delete()
    response = redirect("/feelist?msg=Fee details deleted successfully")
    return response

def apply(request):
    msg=request.GET.get("msg","")
    datad=cg.objects.all()
    return render(request,"apply.html",{"datad":datad,"msg":msg})

def app(request):
    if request.POST:
        name=request.POST["name"]
        college=request.POST["college"]
        course=request.POST["course"]
        date=request.POST["date"]
        document=request.POST["document"]
        datag=cg.objects.get(collegeid=college)
        datac=cs.objects.get(courseid=course)
        id=request.session["id"]
        datal=log.objects.get(logid=id)
        datau=us.objects.get(login=datal)
        re.objects.create(user=datau,name=name,college=datag,course=datac,date=date,document=document,status="waiting")
        response= redirect("/apply?msg=Application submitted successfully")
        return response
    else:
        response=redirect("/apply?msg=operation failed")
        return response

def getcor(request):
    course=request.GET["course"]
    dtdata=cg.objects.get(collegeid=course)

    data=cs.objects.filter(college=dtdata).all()
    ret="<option value=''>--course--</option>"
    for d in data:
        ret+="<option value='"+str(d.courseid)+"'>"+d.name+"</option>"
    return HttpResponse(ret)

def application(request):
    msg=request.GET.get("msg","")
    datar=re.objects.filter(status="waiting").all()
    return render(request,"application.html",{"datar":datar,"msg":msg})

def admission(request):
    logid=request.session["id"]
    userid=us.objects.get(login=logid)
    datan=re.objects.filter(user=userid.userid)
    return render(request,"admission.html",{"datan":datan})

def students(request):
    msg=request.GET.get("msg","")
    data=us.objects.all()
    return render(request,"students.html",{"data":data,"msg":msg})

def deleteuser(request):
    id=request.POST["userid"]
    user = us.objects.get(userid=id)
    logid = str(user.login.logid)
    us.objects.filter(userid=id).delete()
    log.objects.filter(logid=logid).delete()
    response = redirect("/students?msg=Deleted Successfully")
    return response

def addprospectus(request):
    msg=request.GET.get("msg","")
    return render(request,"addprospectus.html",{"msg":msg})

def prospectus(request):
    if request.POST:
        name=request.POST["name"]
        prospectus=request.FILES["prospectus"]
        pro.objects.create(name=name,prospectus=prospectus)
        response=redirect("/addprospectus?msg=Prospectus saved successfully")
        return response
    else:
        response=redirect("/addprospectus?msg=Operation failed")
        return response

def prospectuslist(request):
    msg=request.GET.get("msg","")
    data=pro.objects.all()
    return render(request,"prospectuslist.html",{"data":data,"msg":msg})

def deleteprospectus(request):
    id=request.POST["proid"]
    pro.objects.filter(prospectusid=id).delete()
    response = redirect("/prospectuslist?msg=Prospectus deleted successfully")
    return response

def downpros(request):
    msg=request.GET.get("msg","")
    data=pro.objects.all()
    return render(request,"downpros.html",{"msg":msg,"data":data})

def approvereg(request):
   id=request.POST["aid"]
   re.objects.filter(registrationid=id).update(status="approved")
   response=redirect("/application?msg=Admission approved")
   return response

def rejectreg(request):
   id=request.POST["rid"]
   re.objects.filter(registrationid=id).update(status="rejected")
   response=redirect("/application?msg=Admission rejected")
   return response
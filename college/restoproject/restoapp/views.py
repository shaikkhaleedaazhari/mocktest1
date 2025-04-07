from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponseRedirect
from  .models import *
from django.core.mail import send_mail
import datetime
from django.core.exceptions import ObjectDoesNotExist

def home(request):
	return render(request,'home.html')

def index(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def service(request):
	return render(request,'service.html')

def menu(request):
    bdata = breakfast.objects.all()  
    ldata = lunch.objects.all()      
    ddata = dinner.objects.all()  

    context = {
        'bdata': bdata,
        'ldata': ldata,
        'ddata': ddata,
    }
    return render(request, 'menu.html', context)

def team(request):
	return render(request,'team.html')

def testimonial(request):
	return render(request,'testimonial.html')

def contact(request):
	if request.method=='POST':
		name=request.POST['text1']
		email=request.POST['text2']
		phone=request.POST['text3']
		#password=request.POST['text4']
		message=request.POST['text4']

		user=contacts(username=name,useremail=email,userphone=phone,message=message)
		user.save()
		return render(request,'index.html')
	else:
		return render(request,'contact.html')

def register(request):
	if request.method=='POST':
		fname=request.POST['text1']
		lname=request.POST['text2']
		email=request.POST['text3']
		phone=request.POST['text4']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		user=registers(userfname=fname,userlname=lname,userpassword=password,useremail=email,userphone=phone)
		user.save()
		subject = 'welcome to '
		message = f'Hi {fname}, thank you for registering in our sight. your user username: {email} and  password: {password}.'
		email_from = settings.EMAIL_HOST_USER 
		recipient_list = [email, ] 
		send_mail( subject, message, email_from, recipient_list ) 
		return render(request,'index.html')
	else:
		return render(request,'register.html')

def login(request):
	if request.method=='POST':
		email=request.POST['text3']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=registers.objects.filter(useremail=email,userpassword=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.userfname
				return render(request,'index.html',{'success':'logged in'})
		else:
			return render(request,'login.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'login.html')

def hlogin(request):
	if request.method=='POST':
		email=request.POST['text3']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		check=registers.objects.filter(useremail=email,userpassword=password)
		if check:
			for x in check:
				request.session['myid']=x.id
				request.session['myname']=x.userfname
				return render(request,'hotel/index.html',{'success':'logged in'})
		else:
			return render(request,'hotel/login.html',{'error':'invalid emailid / password'})
	else:
		return render(request,'hotel/login.html')

def logout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/')
	else:
		return redirect('/hotel_index')

def hlogout(request):
	if request.session.has_key('myid'):
		del request.session['myid']
		del request.session['myname']
		return redirect('/home')
	else:
		return redirect('/hotel_index')

def booking(request):
	if request.session.has_key('myid'):
        	uid = request.session['myid']
        	select = request.POST['text4']
        	date = datetime.datetime.now().date()
        	time = datetime.datetime.now().time()
        	message = request.POST['text7']

        	user = registers.objects.get(id=uid,)
        	book = bookers(uid=user, select=select, date=date, time=time, message=message)
        	book.save()
        	fname = user.userfname  # Assuming the field name in 'registers' model
        	email = user.useremail
        	subject = 'welcome to '
        	message = f'Hi {fname}, thank you for registering in our sight. your date: {date} and  time: {time}.'
        	email_from = settings.EMAIL_HOST_USER 
        	recipient_list = [email, ] 
        	send_mail( subject, message, email_from, recipient_list )
        	

        	return redirect('/index')
	else:
        	return render(request, 'login.html')

#def cart(request):
	#return render(request,'cart.html');

def hindex(request):
	return render(request,'hotel/index.html')

def habout(request):
	return render(request,'hotel/about.html')

def hservice(request):
	return render(request,'hotel/service.html')

def hteam(request):
	return render(request,'hotel/team.html')

def htestimonial(request):
	return render(request,'hotel/testimonial.html')

def hbooking(request):
	if request.session.has_key('myid'):
        
        	uid  = request.session['myid']
        	chein = datetime.datetime.now().date()
        	cheout = datetime.datetime.now().date()
        	adult= request.POST['text3']
        	child= request.POST['text4']
        	room= request.POST['text5']
        	req= request.POST['text6']

        	user = registers.objects.get(id=uid)

        	book = rbookers(uid=user, chein=chein, cheout=cheout, adult=adult, child=child,room=room,req=req)
        	book.save()
        	fname = user.userfname  # Assuming the field name in 'registers' model
        	email = user.useremail
        	subject = 'welcome to '
        	message = f'Hi {fname}, thank you for booking in our hotel. your chekin date: {chein} and  time: {cheout}.'
        	email_from = settings.EMAIL_HOST_USER 
        	recipient_list = [email, ] 
        	send_mail( subject, message, email_from, recipient_list )
        	return redirect('/hotel_index')
	else:
        	return render(request, 'login.html')



def hcontact(request):
	return render(request,'hotel/contact.html')

def hroom(request):
	return render(request,'hotel/room.html')

def hcart(request):
	return render(request,'hotel/cart.html')
###############################################################################################

def aindex(request):
	return render(request,'admin/index.html')
def asignin(request):
	return render(request,'admin/signin.html')

def asignup(request):
	if request.method=='POST':
		fname=request.POST['text1']
		lname=request.POST['text2']
		email=request.POST['text3']
		phone=request.POST['text4']
		password=request.POST['text5']
		#hashpass=hashlib.md5(password.encode('utf8')).hexdigest()

		user=aregisters(userfname=fname,userlname=lname,userpassword=password,useremail=email,userphone=phone)
		user.save()
		return render(request,'admin/index.html')
	else:	
		return render(request,'admin/signup.html')

def asignout(request):
	return render(request,'admin/signout.html')

def table(request):
	return render(request,'admin/tables.html')

def achart(request):
	return render(request,'admin/chart.html')

def payment(request):
	return render(request,'payment/index.html')
###################################################################
def binput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=breakfast(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def btableupdate(request):
    if request.method == 'POST':
        iname = request.POST.get('text1')
        price = request.POST.get('text2')
        image = request.FILES.get('text7')
        tid = request.GET.get('tid')

        item = breakfast.objects.get(id=tid)
        item.itemname = iname
        item.price = price

        if image: 
            item.image = image

        item.save()
        return render(request, 'admin/btable.html', {'bdata': breakfast.objects.all()})
    else:
        tid = request.GET.get('tid')
        admin = breakfast.objects.filter(id=tid)
        return render(request, 'admin/bupdate.html', {'newdata2': admin})


def btabledelete(request):
	tid=request.GET['tid']
	tdata=breakfast.objects.filter(id=tid).delete()
	return redirect('/btable/')


def btable(request):
	idata=breakfast.objects.all()
	return render(request,'admin/btable.html',{'bdata':idata})
##########################################################################

def linput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=lunch(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def ltableupdate(request):
	if request.method == 'POST':
		iname = request.POST.get('text1')
		price = request.POST.get('text2')
		image = request.FILES.get('text7')
		tid = request.GET.get('tid')

		item = lunch.objects.get(id=tid)
		item.itemname = iname
		item.price = price

		if image: 
			item.image = image

		item.save()
		return render(request, 'admin/ltable.html', {'ldata': lunch.objects.all()})
	else:
		tid = request.GET.get('tid')
		admin = lunch.objects.filter(id=tid)
		return render(request, 'admin/lupdate.html', {'newdata3': admin})	

def ltabledelete(request):
	tid=request.GET['tid']
	tdata=lunch.objects.filter(id=tid).delete()
	return redirect('/ltable/')

def ltable(request):
	cdata=lunch.objects.all()
	return render(request,'admin/ltable.html',{'ldata':cdata})

###############################################################################

def dinput(request):
	if request.method=='POST':
		iname=request.POST['text1']
		price=request.POST['text2']  
		image=request.FILES['text7']

		add=dinner(price=price,itemname=iname,image=image)
		add.save()
		return render(request,'admin/index.html')
	else:
		return render(request,'admin/input.html')

def dtableupdate(request):
	if request.method == 'POST':
		iname = request.POST.get('text1')
		price = request.POST.get('text2')
		image = request.FILES.get('text7')
		tid = request.GET.get('tid')

		item = dinner.objects.get(id=tid)
		item.itemname = iname
		item.price = price

		if image: 
			item.image = image

		item.save()
		return render(request, 'admin/dtable.html', {'ddata': dinner.objects.all()})
	else:
		tid = request.GET.get('tid')
		admin = dinner.objects.filter(id=tid)
		return render(request, 'admin/dupdate.html', {'newdata4': admin})	

def dtabledelete(request):
	tid=request.GET['tid']
	tdata=dinner.objects.filter(id=tid).delete()
	return redirect('/dtable/')

def dtable(request):
	gdata=dinner.objects.all()
	return render(request,'admin/dtable.html',{'ddata':gdata})
##############################################################################

'''def addtocart(request):
	if request.method=='POST':
		tid=request.GET['tid']
		uid=request.session['myid']
		qty=request.POST['text1']
		item=breakfast.objects.filter(id=tid)
		for x in item:
			price=x.price
		totalamount=int(price)*int(qty)
		user=registers.objects.get(id=uid)
		item1=breakfast.objects.get(id=tid)
		check=addcart.objects.filter(tid=item1,uid=user)
		data=addcart.objects.filter(uid=uid)
		total=0
		for x in data:
			price=x.totalamount
			total=int(price)+total
		if check:
			return render(request,'cart.html',{"error":"the product is already in the cart",'cdata':data,"total":total})
		else:
			addcart=addcart(tid=item1,uid=user,totalamount=totalamount,quantity=qty)
			addcart.save()
			data=addcart.objects.filter(uid=uid,status="pending")
			
			return render(request, "cart.html",{'cdata':data,"total":total})
	else:
		tid=request.GET['tid']
		data=lunch.objects.filter(id=tid)
		return render(request,'cart.html',{'bdata':data})'''

def cart(request):		
		return render(request, "cart1.html")
	

from django.urls import path
from restoapp import views



urlpatterns=[   

				path('',views.home),
				path('index',views.index),
				path('about',views.about),
				path('service',views.service),
				path('menu',views.menu),
				path('booking',views.booking),
				path('team',views.team),
				path('testimonial',views.testimonial),
				path('contact',views.contact),
				path('login',views.login),
				path('register',views.register),
				path('logout',views.logout),
			
				path('hotel_index',views.hindex),
				path('hotel_login',views.hlogin),
				path('hotel_about',views.habout),
				path('hotel_service',views.hservice),
				path('hotel_room',views.hroom),
				path('hotel_booking',views.hbooking),
				path('hotel_team',views.hteam),
				path('hotel_testimonial',views.htestimonial),
				path('hotel_contact',views.hcontact),
				path('payment',views.payment),
				
				path('aindex/',views.aindex),
             	path('asignin/',views.asignin),
             	path('asignup/',views.asignup),
            	path('asignout/',views.asignout),
             	path('table/',views.table),
             	path('achart/',views.achart),
             	path('input/',views.binput),
             	path('binput/',views.binput),
             	path('linput/',views.linput),
             	path('dinput/',views.dinput),
             	path('btable/',views.btable),
             	path('ltable/',views.ltable),
             	path('dtable/',views.dtable),
             	path('btableupdate/',views.btableupdate),
             	path('btabledelete/',views.btabledelete),
             	path('ltableupdate/',views.ltableupdate),
             	path('ltabledelete/',views.ltabledelete),
             	path('dtableupdate/',views.dtableupdate),
             	path('dtabledelete/',views.dtabledelete),
             	path('cart',views.cart),





]


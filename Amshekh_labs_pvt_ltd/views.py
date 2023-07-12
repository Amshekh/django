from asyncio import events
from django.http import HttpResponse, HttpResponseRedirect # Redirect will send you to another webpage after task is finished at current page.
from django.shortcuts import render, redirect # you can either use this redirect function or above HttpResponseRedirect
from .forms import usersForm # Here .forms is what we created forms.py and in that class usersForm which we are importing.
from service.models import Service

def homePage(request):
    servicesData = Service.objects.all() # We get all records by sevice.objects.all()
    #for a in servicesData:
    #    print(a)  # using for loop we now print all Service Object | If we print(a.service_icon)  we get name of  entry we have given earlier for service_icon
    
    data = {
            'servicesDta': servicesData
    }
    return render(request, "Index.html", data)

def first_django_webpage(request):
    data = {                        # we are using variable of type dictionary
            'title': 'First Sample Page',
            'clist': ['Open source software order', 'Proprietary software software order', 'Custom made hybrid software order'],
            'numbers': [10, 20, 30, 40, 50], # Notice : How we will display numbers declared in list
            'client_details': [
                {'orderno': '754198','cname': 'Phoneix ltd', 'contact': '+1949678211', 'type': 'Proprietary', 'ecost': '500,000 usd', 'edelivery': '45 days'},
                {'orderno': '754199','cname': 'Super Services ltd', 'contact': '+1626698247', 'type': 'Open Source', 'ecost': '250,000 usd', 'edelivery': '50 days'},
                {'orderno': '754200','cname': 'Digicard Inc', 'contact': '+1510628371', 'type': 'Custom/Hybrid', 'ecost': '350,000 usd', 'edelivery': '55 days'},

        ]
    }
    return render(request, "first_django_webpage.html", data) # render function will now require 3 parameters


def submitForm(request):  # when we have given in <form> tag  action="{% url 'submitForm' %}" in userForm.html
    try:
        if request.method=="POST":
            # n1 = int(request.POST['num1'])  # method 1 to fetch value of num1 and assign it to n1 variable
            # n2 = int(request.POST['num2'])  # similarly, value of num2 to n2 variable

            n1 = int(request.POST.get('num1')) # method 2 to fetch value of num1 and assign it to n1 variable
            n2 = int(request.POST.get('num2')) # similarly, value of num2 to n2 variable
            finalans =  n1 + n2
            data = {
                 'n1':n1,
                 'n2':n2,
                 'output':finalans
            }
            
            # return HttpResponseRedirect('/thank-you/')   # Method 1 : after user has performed task,he will be redirect to contactUs page.
            url = "/thank-you/?output={}".format(finalans)  # Method 2 : In a variable url give path like this, along with answer in output.
            # return HttpResponseRedirect(url)   # Method 2 return like this.
            # Alternatively if you have import render function from django.shortcuts then you can use below
            return redirect(url)
    except:
        pass

def aboutUs(request):
   # return HttpResponse("<b> Welcome to Amshekh labs pvt ltd </b>")
   return render(request, "aboutUs.html")

def contactUs(request):
    return render(request, "contactUs.html")

def thankYou(request):
    if request.method == "GET":
        output = request.GET.get('output')
    return render(request, "thankYou.html", {'output': output})

def userForm(request):
    finalans = 0
    fn = usersForm()
    data = {'form':fn}  # we are defining empty dictionary, as initially there is no value
    try:
        if request.method=="POST":
            # n1 = int(request.POST['num1'])  # method 1 to fetch value of num1 and assign it to n1 variable
            # n2 = int(request.POST['num2'])  # similarly, value of num2 to n2 variable

            n1 = int(request.POST.get('num1')) # method 2 to fetch value of num1 and assign it to n1 variable
            n2 = int(request.POST.get('num2')) # similarly, value of num2 to n2 variable
            finalans =  n1 + n2
            data = {
                # 'n1':n1,
                #'n2':n2,
                 'form':'fn',
                 'output':finalans
            }
            
            # return HttpResponseRedirect('/thank-you/')   # Method 1 : after user has performed task,he will be redirect to contactUs page.
            url = "/thank-you/?output={}".format(finalans)  # Method 2 : In a variable url give path like this, along with answer in output.
            # return HttpResponseRedirect(url)   # Method 2 return like this.
            # Alternatively if you have import render function from django.shortcuts then you can use below
            return redirect(url)
    except:
        pass    
    return render(request, "userForm.html", data)
    
def calculator(request):
    res = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                res = n1 + n2
            elif opr == "-":
                res = n1 - n2
            elif opr == "*":
                res = n1 * n2
            elif opr == "/":
                res = n1 / n2
            elif opr == "%":
                res = n1 % n2

    except:
        res = "Invalid operator"    
    return render(request, "calculator.html", {'res': res})

def evenodd(request):
    res = ''
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            if n1 % 2 == 0:
                res = "even number"
            else:
                res = "odd number"
    except:
        res = "Please enter number"    
    return render(request, "evenodd.html", {'res': res})

def marksheet(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('sub1'))
        s2 = eval(request.POST.get('sub2'))
        s3 = eval(request.POST.get('sub3'))
        s4 = eval(request.POST.get('sub4'))
        s5 = eval(request.POST.get('sub5'))
        t = s1 + s2+ s3 + s4 + s5
        p = t * 100 / 500
        if p >= 85:
            d = "Distinction"
        elif p >= 60:
            d = "First Divison"
        elif p >= 50:
            d = "Second Divison"
        elif p >= 35:
            d = "Third Divison"
        else:
            d = "Not Qualified / Fail"
        data = {
                'total': t,
                'perc': p,
                'divison': d
        }
        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")

def custom_Software_Order(request):
    return HttpResponse("<b> Welcome to custom software order page for your business </b>")
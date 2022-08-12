from django.shortcuts import render,redirect
from .models import Agreement,Customer
from django.db.models import Count
import datetime
def Workplace(request):
    context={}
    try:
        shartnoma=Agreement.objects.all()
    except Exception as ex:
        print(ex)
        shartnoma={}
    try:
        mijoz=Customer.objects.annotate(number=Count('agreement'))
    except Exception as ex:
        print(ex)
        mijoz={}

    xobj = mijoz.values('id','inn','name','number','status','who_send','firma_name_sender')
   # print(xobj)
    context['shartnoma']=shartnoma
    context['mijoz']=xobj

    return render(request,"maxsus/website/shartnoma.html",context)
def Check(request):
    try:
        shartnoma=Agreement.objects.all()
    except:
        return redirect('workplace')
    # try:
    #     mijoz=Customer.objects.all()
    # except:
    #     mijoz={}
    date=datetime.date.today()

    for i in shartnoma:
        if i.end_date.year == date.year:
            if i.end_date.month == date.month:
                if i.end_date.day >= date.day:
                    i.status=True
                    i.save()
                    i.customer.status = True
                    i.customer.save()
                else:
                    i.status=False
                    i.save()
                    i.customer.status=False
                    i.customer.save()
            elif i.end_date.month > date.month :
                i.status = True
                i.save()
                i.customer.status = True
                i.customer.save()
            else:
                i.status = False
                i.save()
                i.customer.status = False
                i.customer.save()
        elif i.end_date.year > date.year:
            i.status = True
            i.save()
            i.customer.status = True
            i.customer.save()
        else:
            i.status=False
            i.save()
            i.customer.status = False
            i.customer.save()


    return redirect('workplace')
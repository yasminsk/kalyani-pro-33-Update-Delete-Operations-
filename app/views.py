from django.shortcuts import render
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.
from app.models import *

def display_topics(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_topics.html',context=d)

def display_webpages(request):
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(topic_name='Cricket')
    #LOW=Webpage.objects.get(topic_name='Cricket')
    LOW=Webpage.objects.exclude(topic_name='Cricket')
    LOW=Webpage.objects.all()[:2:]
    LOW=Webpage.objects.order_by('name')
    LOW=Webpage.objects.order_by('-name')
    LOW=Webpage.objects.order_by(Length('name'))
    LOW=Webpage.objects.order_by(Length('name').desc())
    LOW=Webpage.objects.all()
    LOW=Webpage.objects.filter(name__startswith='S')
    LOW=Webpage.objects.filter(name__endswith='l')
    LOW=Webpage.objects.filter(name__contains='u')
    LOW=Webpage.objects.filter(name__in=('Dhoni','Rahul'))
    LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{6}')
    LOW=Webpage.objects.filter(Q(topic_name='Kabaddi') & Q(name='Rahul'))
    LOW=Webpage.objects.filter(Q(topic_name='Cricket'))
    
    d={'webpages':LOW}
    return render(request,'display_webpages.html',context=d)

def display_access(request):
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__gt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lt='2012-07-25')
    LOA=AccessRecord.objects.filter(date__gte='2012-07-25')
    LOA=AccessRecord.objects.filter(date__lte='2012-07-25')
    LOA=AccessRecord.objects.all()
    LOA=AccessRecord.objects.filter(date__year='2012')
    LOA=AccessRecord.objects.filter(date__month='10')
    LOA=AccessRecord.objects.filter(date__day='05')
    LOA=AccessRecord.objects.filter(date__year__gt='2008')
    LOA=AccessRecord.objects.filter(date__month__lt='09')
    LOA=AccessRecord.objects.filter(date__day__gt='16')
    
    d={'access':LOA}
    return render(request,'display_access.html',context=d)


def update_webpages(request):
    #Webpage.objects.filter(name='Suresh').update(email='Suresh@gmail.in')
    #Webpage.objects.filter(name='Dhoni').update(email='Dhoni@gmail.in',url='http://Dhoni.com')
    #Webpage.objects.filter(name='Rahul').update(topic_name='Kabaddi')
    #Webpage.objects.filter(topic_name='Football').update(email='SUNIL@gmail.com')

    #Webpage.objects.update_or_create(name='Rahul',defaults={'url':'https://Rahul.in'})
    #Webpage.objects.update_or_create(email='SUNIL@gmail.com',defaults={'name':'SUNIL'})
    TO=Topic.objects.get_or_create(topic_name='cricket')[0]
    TO.save()
    Webpage.objects.update_or_create(name='Hardik',defaults={'topic_name':TO,'url':'https://Hardik.com','email':'Hardik@gmail.com'})

    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpages.html',context=d)


def delete_webpages(request):
    #Webpage.objects.filter(name='SUNIL').delete()
    Webpage.objects.all().delete()

    d={'webpages':Webpage.objects.all()}
    return render(request,'display_webpages.html',d)
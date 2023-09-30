from django.shortcuts import render
from . models import MovieInfo
# Create your views here.
from . forms import MovieForm

def create(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
        
        frm=MovieForm()
        # title=request.POST.get('title')
        # year=request.POST.get('year')
        # desc=request.POST.get('desc')
        # movie_obj=MovieInfo(title=title,year=year,desc=desc)
        # movie_obj.save()


    return render(request,'create.html',{'frm':frm})


def edit(request):
    if request.GET:
        x=request.GET.get('keyd')
        m=MovieInfo.objects.get(id=x)
        m.delete()
        
        movies_set=MovieInfo.objects.all()
        return render(request,'edit.html',{'movies':movies_set})
        
    if request.POST:
        key=request.POST.get('key')
        title=request.POST.get('title')
        year=request.POST.get('year')
        desc=request.POST.get('summary')
        m=MovieInfo.objects.get(id=key)
        m.delete()
        
        movie_obj=MovieInfo(title=title,year=year,desc=desc,id=key)
        movie_obj.save()
        movies_set=MovieInfo.objects.all()
        return render(request,'edit.html',{'movies':movies_set})
    movies_set=MovieInfo.objects.all()
    return render(request,'edit.html',{'movies':movies_set})

def list(request):
    movies_set=MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movies_set})

















    """ {
        'movies':[
        {
        'title':'Leo',
        'year':2023,
        'summary':'story of gangsters who living in LCU',
        'success':True,
        'img':'leo.jpg'
        },
        {
        'title':'Vikram',
        'year':2021,
        'summary':'story of gangsters who living in LCU',
        'success':True,
        'img':'vikram.jpeg'
        },
        {
        'title':'Kaithi',
        'year':2018,
        'summary':'story of gangsters who living in LCU',
        'success':False,
        'img':'kaithi.jpg'
        },
        {
        'title':'Rolex',
        'year':2025,
        'success':True,
        'img':'rolex.jpg'
        },
    ]
    }"""
    
from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import mypost

# Create your views here.
def index(request):
    if request.method=='GET':
        return render(request, 'index.html')
    if request.method=='POST':
        return render(request, 'index.html')

def newlogin(request):
    if request.method=="POST":
        nam=request.POST.get('name')
        pas=request.POST['password']
        print(nam+pas)
        sql=mypost(name=nam, password=pas)
        sql.save()
        alldataaaa=mypost.objects.all()
        return render_to_response('work.html', {'alldata':alldataaaa})

def testfor(request):
    return render(request, 'testfor.html')

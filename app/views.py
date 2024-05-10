from django.shortcuts import render
from app.models  import   *

# Create your views here.
def innerEquijoins(request):
    JDED=Emp.objects.select_related('DEPTNO').all()
    JDED=Emp.objects.select_related('DEPTNO').filter(JOB='CLERK')
    JDED=Emp.objects.select_related('DEPTNO').all()
    JDED=Emp.objects.select_related('DEPTNO').filter(ENAME='SCOTT')
    
    d={'JDED':JDED}
    return render(request,'innerEquijoins.html',d)



def update_emp(request):
    JDED=Emp.objects.update_or_create(Ename='Scott',defaults={'Sal':'2000'})
    
    d={'JDED':JDED}
    return render(request,update_emp.html,d)
from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView


class TempDataRender(TemplateView):
    template_name='TempDataRender.html'


    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='poorna'
        return ECDO
        
# templateview inserting

class Temp_InsertData(TemplateView):
    template_name='Temp_InsertData.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('Temp_InsertData')

# stundent formview inserting by using form_valid method

class StudentFormviewinsert(FormView):
    template_name='StudentFormviewinsert.html'
    form_class=StudentForm
    def form_valid(self,form):
        form.save()
        return HttpResponse('data inserted')

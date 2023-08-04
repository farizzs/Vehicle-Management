from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from Backend.models import Vehicle_details
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
class Homepage(View):
    template="index.html"
    def get(self,request):
        data=Vehicle_details.objects.all()
        context={
            'data':data
        }
        return render(request,self.template,context)
    
class Add_Details(View):
    page_name="index.html"
    def post(self, request):
        vehicle_number = request.POST.get('Vehicle_number')
        vehicle_type = request.POST.get('Vehicle_type')
        vehicle_model = request.POST.get('Vehicle_model')
        vehicle_description = request.POST.get('Vehicle_description')
        vehicle_data = Vehicle_details(
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            vehicle_model=vehicle_model,
            vehicle_description=vehicle_description
        )
        vehicle_data.save()
        return render(request, self.page_name)
    

class Edit_Details(View):
    template_name="index.html"
    def post(self,request,dataid):
         data=Vehicle_details.objects.all()

         vehicle_number = request.POST.get('Vehicle_number')
         vehicle_type = request.POST.get('Vehicle_type')
         vehicle_model = request.POST.get('Vehicle_model')
         vehicle_description = request.POST.get('Vehicle_description')
         Vehicle_details.objects.filter(id=dataid).update(
            vehicle_number=vehicle_number,
            vehicle_type=vehicle_type,
            vehicle_model=vehicle_model,
            vehicle_description=vehicle_description
        )
         return render(request, self.template_name,{'data':data})


class Delete_Details(DeleteView):
    # model = Vehicle_details
    # context_object_name = 'index.html'
    # success_url = reverse_lazy('index.html')
    # data=Vehicle_details.objects.all()
    template_name="index.html"
    def get(self,request,dataid):
       data=Vehicle_details.objects.filter(id=dataid)
       data.delete()
       return redirect(self.template_name)









    


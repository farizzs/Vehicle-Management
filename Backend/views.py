from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from Backend.models import Vehicle_details

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
    def patch(self,request,dataid):
         data = Vehicle_details.objects.get(id=dataid)
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


    


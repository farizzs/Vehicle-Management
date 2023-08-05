from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User,Group
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from Backend.models import Vehicle_details
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login

# Create your views here.

class Homepage(PermissionRequiredMixin,View):
    permission_required="Backend.view_vehicle_details"
    template="index.html"
    def get(self,request):
        data=Vehicle_details.objects.all()
        context={
            'data':data
        }
        return render(request,self.template,context)
    
class Add_Details(PermissionRequiredMixin,View):
    permission_required="Backend.add_vehicle_details"
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
        return redirect("Home")

class Edit_Details(PermissionRequiredMixin,View):
    permission_required="Backend.change_vehicle_details"
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
         return redirect("Home")


class Delete_Details(PermissionRequiredMixin,DeleteView):
    permission_required="Backend.delete_vehicle_details"

    # model = Vehicle_details
    # context_object_name = 'index.html'
    # success_url = reverse_lazy('index.html')
    # data=Vehicle_details.objects.all()
    template_name="index.html"
    def get(self,request,dataid):
       data=Vehicle_details.objects.filter(id=dataid)
       data.delete()
       return redirect("Home")
    

    
class Singup(View):
  login_page="login.html"
 
  def get(self,request):
            return render(request,self.login_page)
    
  def post(self,request):
         try:
            context = {}
            username=request.POST.get('username')
            emailid=request.POST.get('emailid')
            password=request.POST.get('password')
           
            if User.objects.filter(username=username).exists():
                context["error"] = "This Username alraedy exists"
                return render(request,self.login_page,context)
            if  User.objects.filter(email=emailid).exists():
                context["error"] = "This Email alraedy exists"
                return render(request,self.login_page,context)
           
            # User.objects.create_user(username=username,email=emailid,password=password)
            user=  User.objects.create_user(username=username,email=emailid,password=password)
            group= Group.objects.get(name="user")
            user.groups.add(group)
         
            return render(request,self.login_page,context)
         except Exception as e:
            context = {
               "error":str(e)
            }
            return render(request,self.login_page,context)
         
class Login(View):
      login_page="login.html"
      template_name="index.html"

      def post(self,request):
                username_r = request.POST.get("username")
                password_r = request.POST.get("password")
                user = authenticate(username=username_r, password=password_r)
                if user is not None:
                    login(request=request, user=user)
                
                    return redirect("Home")
                else:  
                     return render(request,self.login_page)
         

         



         



         












    


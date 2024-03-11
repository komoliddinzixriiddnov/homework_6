from django.shortcuts import render
from django.views import View


class UserLoginPaggeView(View):
    def get (self, request):
        return render(request,"users/login.html")



class UseRegisterPaggeView(View):
    def get (self, request):
        return render(request,"users/register.html")

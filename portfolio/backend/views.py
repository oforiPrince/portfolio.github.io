from django.shortcuts import render
from django.views import View


class DashboardView(View):
   def get(self, request):
      template_name = 'pages/index.html'

      return render(request, template_name)


class ProfileView(View):
   def get(self, request):
      template_name = 'pages/profile.html'

      return render(request, template_name)

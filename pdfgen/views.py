from django.shortcuts import render
from datetime import datetime   
from io import StringIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from core.models import Profile, UserEducation, UserProject, UserJob, UserSkill


class cvgen(APIView):
    
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
       
        user = self.request.user
        
        context = {}
        context['user'] = user
        context['profile'] = Profile.objects.get(user=user)
        context['educations'] = UserEducation.objects.filter(user=user).order_by('-start_year').all()
        context['projects'] = UserProject.objects.filter(user=user).all()
        context['jobs'] = UserJob.objects.filter(user=user).order_by('-start_year').all()
        context['skills'] = UserSkill.objects.filter(user=user).all()
        return render(request, 'srt-resume.html', context=context)

class test(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        template_path = 'srt-resume.html'
        
        context = {}
        context['user'] = user
        context['profile'] = Profile.objects.get(user=user)
        context['educations'] = UserEducation.objects.filter(user=user).order_by('-start_year').all()
        context['projects'] = UserProject.objects.filter(user=user).all()
        context['jobs'] = UserJob.objects.filter(user=user).order_by('-start_year').all()
        context['skills'] = UserSkill.objects.filter(user=user).all()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename="resume{str(datetime.now().date())}"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse({'detail': 'Something went wrong!'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
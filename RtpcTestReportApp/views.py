from django.shortcuts import render
from django.http import HttpResponse
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import PatientReport
# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def view_report(request):
   template_path = 'RtpcTestReportApp/report.html'
   try:
      context = {'report': PatientReport.objects.get(patient=request.user)}
      # Create a Django response object, and specify content_type as pdf
      response = HttpResponse(content_type='application/pdf')
      # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
      # find the template and render it.
      template = get_template(template_path)
      html = template.render(context)

      # create a pdf
      pisa_status = pisa.CreatePDF(
         html, dest=response)
      # if error then show some funy view
      if pisa_status.err:
         return HttpResponse('We had some errors <pre>' + html + '</pre>')
      return response
   except PatientReport.DoesNotExist:
      return render(request,'RtpcTestReportApp/patient_report_not_found.html',{})

@login_required(login_url=settings.LOGIN_URL)
def download_report(request):
   template_path = 'RtpcTestReportApp/report.html'
   try:
      context = {'report': PatientReport.objects.get(patient=request.user)}
      # Create a Django response object, and specify content_type as pdf
      response = HttpResponse(content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename="report.pdf"'
      # find the template and render it.
      template = get_template(template_path)
      html = template.render(context)

      # create a pdf
      pisa_status = pisa.CreatePDF(
         html, dest=response)
      # if error then show some funy view
      if pisa_status.err:
         return HttpResponse('We had some errors <pre>' + html + '</pre>')
      return response
   except PatientReport.DoesNotExist:
      return render(request,'RtpcTestReportApp/patient_report_not_found.html',{})
   
@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
   try:
      patient=PatientReport.objects.get(patient=request.user)
      return render(request, 'RtpcTestReportApp/dashboard.html',{'patient': patient})
   except PatientReport.DoesNotExist:
      return render(request,'RtpcTestReportApp/patient_report_not_found.html',{})

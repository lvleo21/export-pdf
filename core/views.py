from django.shortcuts import render
from django.views.generic import ListView
from core.models import People, ProgrammingLenguage

from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.views.generic import View, TemplateView
from weasyprint import HTML


class ProgrammingLenguageListView(ListView):
    model = ProgrammingLenguage
    template_name = 'core/people/list.html'


class PDFRenderView(View):
    template_name = 'core/pdf/view.html'

    def get(self, request, *args, **kwargs):

        context = {
            'people_list': People.objects.filter(programming_lenguage__pk = kwargs['pk']),
            'lenguage': ProgrammingLenguage.objects.get(pk =kwargs['pk']).name
        }

        html_string = render_to_string(self.template_name, context)

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/report2.pdf')

        # Django built-in
        fs = FileSystemStorage('/tmp/')

        with fs.open('report2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # inline: make file to be open as to print
            response['Content-Disposition'] = 'filename="report2.pdf"'

        return response


class PDFDownloadView(View):
    template_name = 'core/pdf/view.html'

    def get(self, request, *args, **kwargs):
        context = {
            'people_list': People.objects.filter(programming_lenguage__pk=kwargs['pk']),
            'lenguage': ProgrammingLenguage.objects.get(pk=kwargs['pk']).name
        }

        html_string = render_to_string(self.template_name, context)

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/report2.pdf')

        # Django built-in
        fs = FileSystemStorage('/tmp/')

        with fs.open('report2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # attachment make file content to de downloaded
            response['Content-Disposition'] = 'attachment; filename="report2.pdf"'

        return response

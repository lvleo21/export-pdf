from django.urls import path
from .views import ProgrammingLenguageListView, PDFRenderView, PDFDownloadView

app_name = 'core'
urlpatterns = [
    path('', ProgrammingLenguageListView.as_view(), name='programming_lenguage_list_view' ),
    path('pdf/view/<pk>/', PDFRenderView.as_view(), name='pdf_view'),
    path('pdf/download/<pk>/', PDFDownloadView.as_view(), name='pdf_download'),
]
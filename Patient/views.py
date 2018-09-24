from django.shortcuts import render
from requests import request

from .models import Patient, LookupRajon, LookupRegion
from django.views import generic
import datetime
# Create your views here.
from .tables import CurrentTables
from .filters import PosteFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_patients = Patient.objects.all().count()
    # num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    # num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    # num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_patients': num_patients, },
    )

class PatientListView(generic.ListView):
 model = Patient

class PatientDetailView(generic.DetailView):
 model = Patient

class LoanedPatientByDateListView(generic.ListView):
 model = Patient
 template_name = 'patient/patient_list_enddate.html'


 def get_queryset(self):
     start_day = datetime.date.today()
     end_day = datetime.date.today() + datetime.timedelta(weeks=3)
     return Patient.objects.filter(dat_end__range=(start_day,end_day))


class FilteredPersonListView(SingleTableMixin, FilterView):
     table_class = CurrentTables
     model = Patient
     template_name = 'patient/people.html'
     filterset_class = PosteFilter


class FilteredPersonListView1(SingleTableMixin, FilterView):
    start_day = datetime.date.today()
    end_day = datetime.date.today() + datetime.timedelta(weeks=3)
    table_class = CurrentTables
    model = Patient
    template_name = 'patient/people1.html'
    filterset_class = PosteFilter
    table_data = Patient.objects.filter(dat_end__range=(start_day, end_day))

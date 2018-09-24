from django.conf.urls import include, url
from django.conf import settings

from . import views


urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^patients/$', views.PatientListView.as_view(), name='patients'),
url(r'^Patient/(?P<pk>\d+)$', views.PatientDetailView.as_view(), name='patient-detail'),
url(r'^patientsdate/$', views.LoanedPatientByDateListView.as_view(), name='patients_date'),
url(r'^people/$', views.FilteredPersonListView.as_view(), name='people'),
url(r'^people1/$', views.FilteredPersonListView1.as_view(), name='people1'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
import datetime
import django_tables2 as tables
from .models import Patient


class CurrentTables(tables.Table):
#    office = tables.LinkColumn('stats:office-workers', verbose_name=_(u'Pobočka'), accessor='office')
    class Meta:
        model = Patient
        template_name = 'django_tables2/bootstrap.html'
        # add class="paleblue" to <table> tag
        #attrs = {'class': 'paleblue'}
        #fields = ('first_name', 'addr_city', 'phone_mobile')
        attrs = {"class": "table-striped table-bordered "}
        per_page: 25

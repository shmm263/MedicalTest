from django.db import models
from django.urls import reverse
from django import forms


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Genre'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class LookupRegion(models.Model):
    regions = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'lookup_region'
        verbose_name = 'Регионы',
        verbose_name_plural = 'Регионы'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.regions


class LookupRajon(models.Model):
    rajons = models.CharField(max_length=200)
    region_id = models.ForeignKey('LookupRegion', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lookup_rajon'
        verbose_name = 'Районы',
        verbose_name_plural = 'Районы'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # LookupRajon.objects.filter(region_id=5)
        return '{0} ({1})'.format(self.rajons, self.region_id)


class Patient(models.Model):
    first_name = models.CharField(db_column='First_name', max_length=100)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_name', max_length=100)  # Field name made lowercase.
    patron_name = models.CharField(max_length=150)  # Field name made lowercase.
    date_birthday = models.DateField(blank=True, null=True)
    phone_home = models.CharField(max_length=10)
    phone_mobile = models.CharField(max_length=13)
    email = models.CharField(max_length=250)
    place_of_work = models.TextField(db_column='place_of_work',blank=True, null=True)
    date_medical_examination = models.DateField(blank=True, null=True)
    purpose = (
        ('Огляд водія', 'Огляд водія'),
        ('Дозвіл на зброю', 'Дозвіл на зброю'),
        ('Санітарна книжка', 'Санітарна книжка'),
        ('Сертифікат нарколога', 'Сертифікат нарколога'),
        ('Сертифікат психіатора', 'Сертифікат психіатора'),
        ('Довідка в бесейн', 'Довідка в бесейн'),
        ('Форма 086', 'Форма 086'),
        ('Інші', 'Інші'),

    )
    purpose_medical_examination = models.CharField(max_length=20,choices=purpose, blank=True, default='Огляд водія', help_text="Введите цель медосмотра")
    reference_number = models.CharField(max_length=30)
    #validaty_days = models.IntegerField()
    region_id = models.ForeignKey('LookupRegion', models.DO_NOTHING, blank=True, null=True)
    rajon_id = models.ForeignKey('LookupRajon', models.DO_NOTHING, blank=True, null=True)
    locality = (
        ('м', 'місто'),
        ('с', 'село'),
        ('смт', 'селище міського типу'),
    )
    addr_locality = models.CharField(max_length=3,choices=locality, blank=True, default='с', help_text="Введите тип населенного пункта")
    addr_city = models.CharField(max_length=100)
    abbreavation = (
        ('бульвар', 'бульвар'),
        ('вул', 'вулиця'),
        ('кв', 'квартал'),
        ('пр-к', 'провулок'),
        ('пр', 'проспект'),
        ('тупік', 'тупік'),
        ('узвіз', 'узвіз'),
        ('шосе', 'шосе'),
    )
    addr_abbreavation = models.CharField(max_length=10,choices=abbreavation, blank=True, default='вул', help_text="Введите абривиатуру улицы")
    addr_street = models.CharField(max_length=200)
    addr_house = models.CharField(max_length=5)
    addr_corpus = models.CharField(max_length=5)
    addr_room = models.CharField(max_length=5)
    addr_index = models.CharField(max_length=5)
    dat_end = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ["first_name"]
        managed = False
        db_table = 'Patient'
        verbose_name = 'Пациент',
        verbose_name_plural = 'Пациент'

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        # rajon_id = LookupRajon.objects.filter(region_id__regions__contains='Киевская')
        return '%s, %s, %s' % (self.last_name, self.first_name, self.patron_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
       """
        return reverse('patient-detail', args=[str(self.id)])

#class MyPatientForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#        super(MyPatientForm, self).__init__(*args, **kwargs)
#        if 'initial' in kwargs:
#         self.fields['rajon_id'].queryset = LookupRajon.objects.filter(region_id = self.region_id.id)
#
#     class Meta:
#         model = Patient
#         fields = ['first_name', 'last_name', 'patron_name', 'date_birthday', 'phone_home', 'phone_mobile'
#             , 'email', 'place_of_work', 'date_medical_examination', 'reference_number', 'validaty_days'
#             , 'region_id', 'rajon_id', 'addr_locality', 'addr_city', 'addr_abbreavation', 'addr_street', 'addr_house'
#             ,'addr_corpus', 'addr_room', 'addr_index']


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)

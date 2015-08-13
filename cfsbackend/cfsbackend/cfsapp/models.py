# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.

from __future__ import unicode_literals
from django.db import models

# Geography as it pertains to policing

class Sector(models.Model):
    sector_id = models.IntegerField(primary_key=True)
    descr     = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'sector'

class District(models.Model):
    district_id = models.IntegerField(primary_key=True)
    sector      = models.OneToOneField(Sector, blank=True, null=True)
    descr       = models.TextField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'district'

class Beat(models.Model):
    beat_id   = models.IntegerField(primary_key=True)
    district  = models.OneToOneField(District, blank=True, null=True)
    sector    = models.OneToOneField(Sector, blank=True, null=True)
    descr     = models.TextField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'beat'

# Support Classes

class CallSource(models.Model):
    call_source_id = models.IntegerField(primary_key=True)
    descr = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'call_source'

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    descr = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'

class CallUnit(models.Model):
    call_unit_id = models.IntegerField(primary_key=True)
    descr = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'call_unit'

class Nature(models.Model):
    nature_id = models.IntegerField(primary_key=True)
    descr     = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'nature'

class CloseCode(models.Model):
    close_code_id = models.IntegerField(primary_key=True)
    descr         = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table = 'close_code'

class OOSCode(models.Model):
    oos_code_id = models.IntegerField(primary_key=True)
    descr       = models.TextField(blank=False,null=False)

    class Meta:
        managed = False
        db_table= 'oos_code'


class OutOfServicePeriods(models.Model):
    oos_id        = models.IntegerField(primary_key=True)
    call_unit     = models.OneToOneField(CallUnit, blank=True, null=True, db_column="call_unit_id", related_name="call_unit")
    shift_unit_id = models.BigIntegerField(blank=True,null=True)
    oos_code      = models.OneToOneField(OOSCode, blank=True, null=True, db_column="oos_code_id", related_name="oos_code")
    location      = models.TextField(blank=True,null=True)
    comments      = models.TextField(blank=True,null=True)
    start_time    = models.DateTimeField(blank=True,null=True)
    end_time      = models.DateTimeField(blank=True,null=True)
    duration      = models.DurationField(blank=True,null=True)

    class Meta:
        managed = False
        db_table = 'out_of_service'

# Primary Classes

class Call(models.Model):
    call_id              = models.BigIntegerField(primary_key=True)
    month_received       = models.IntegerField(blank=True, null=True)
    week_received        = models.IntegerField(blank=True, null=True)
    dow_received         = models.IntegerField(blank=True, null=True)
    hour_received        = models.IntegerField(blank=True, null=True)
    case_id              = models.BigIntegerField(blank=True, null=True)
    call_source          = models.OneToOneField(CallSource, blank=True, null=True)
    primary_unit         = models.OneToOneField(CallUnit, blank=True, null=True, related_name="primary_unit")
    first_dispatched     = models.OneToOneField(CallUnit, blank=True, null=True, related_name="first_dispatched")
    reporting_unit       = models.OneToOneField(CallUnit, blank=True, null=True, related_name="reporting_unit")
    street_num           = models.IntegerField(blank=True, null=True)
    street_name          = models.TextField(blank=True, null=True)
    city                 = models.OneToOneField(City, blank=True, null=True, related_name="city")
    zipcode              = models.IntegerField(blank=True, null=True, db_column="zip")
    crossroad1           = models.TextField(blank=True, null=True)
    crossroad2           = models.TextField(blank=True, null=True)
    geox                 = models.FloatField(blank=True, null=True)
    geoy                 = models.FloatField(blank=True, null=True)
    beat                 = models.OneToOneField(Beat,blank=True, null=True)
    district             = models.OneToOneField(District,blank=True, null=True)
    sector               = models.OneToOneField(Sector,blank=True, null=True)
    business             = models.TextField(blank=True, null=True)
    nature               = models.OneToOneField(Nature, blank=True, null=True)
    priority             = models.TextField(blank=True, null=True)
    report_only          = models.NullBooleanField()
    cancelled            = models.NullBooleanField()
    time_received        = models.DateTimeField(blank=True, null=True)
    time_routed          = models.DateTimeField(blank=True, null=True)
    time_finished        = models.DateTimeField(blank=True, null=True)
    first_unit_dispatch  = models.DateTimeField(blank=True, null=True)
    first_unit_enroute   = models.DateTimeField(blank=True, null=True)
    first_unit_arrive    = models.DateTimeField(blank=True, null=True)
    first_unit_transport = models.DateTimeField(blank=True, null=True)
    last_unit_clear      = models.DateTimeField(blank=True, null=True)
    time_closed          = models.DateTimeField(blank=True, null=True)
    close_code           = models.OneToOneField(CloseCode, blank=True, null=True)
    close_comments       = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'call'

class Incident(models.Model):
    incident_id = models.BigIntegerField(primary_key=True)
    case_id     = models.BigIntegerField(unique=True, blank=True, null=True)
    time_filed  = models.DateTimeField(blank=True, null=True)
    month_filed = models.IntegerField(blank=True, null=True)
    week_filed  = models.IntegerField(blank=True, null=True)
    dow_filed   = models.IntegerField(blank=True, null=True)
    street_num  = models.IntegerField(blank=True, null=True)
    street_name = models.TextField(blank=True, null=True)
    city        = models.OneToOneField(City, blank=True, null=True)
    zipcode     = models.IntegerField(blank=True, null=True, db_column="zip")
    geox        = models.FloatField(blank=True, null=True)
    geoy        = models.FloatField(blank=True, null=True)
    beat        = models.OneToOneField(Beat,blank=True, null=True)
    district    = models.OneToOneField(District,blank=True, null=True)
    sector      = models.OneToOneField(Sector,blank=True, null=True)
    #premise    = models.ForeignKey('Premise', blank=True, null=True)
    #weapon     = models.ForeignKey('Weapon', blank=True, null=True)
    domestic    = models.NullBooleanField()
    juvenile    = models.NullBooleanField()
    gang_related = models.NullBooleanField()
    #emp_bureau = models.ForeignKey(Bureau, blank=True, null=True)
    #emp_division = models.ForeignKey(Division, blank=True, null=True)
    #emp_unit = models.ForeignKey('Unit', blank=True, null=True)
    num_officers = models.IntegerField(blank=True, null=True)
    #investigation_status = models.ForeignKey('InvestigationStatus', blank=True, null=True)
    #investigator_unit = models.ForeignKey('Unit', blank=True, null=True)
    #case_status = models.ForeignKey(CaseStatus, blank=True, null=True)
    ucr_code = models.IntegerField(blank=True, null=True)
    #ucr_descr = models.ForeignKey('UcrDescr', blank=True, null=True)
    committed = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'incident'


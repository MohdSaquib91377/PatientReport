from django.db import models
from datetime import datetime 
from patient.models import Patient
class PatientReport(models.Model):
    COVID_RESULT = (
        ('POSITIVE', 'Positive'),
        ('NEGATIVE', 'Negative'),
    )
    covid_result=(('positive','Positive'),('negative','Negative'))
    patient = models.ForeignKey(Patient, related_name='reports',on_delete=models.CASCADE)
    srf_id = models.BigIntegerField(verbose_name='SRF ID',unique=True)
    ref_by = models.CharField(max_length=64,verbose_name='Ref .By')
    lab_id = models.IntegerField(verbose_name='LAB ID')
    printed = models.DateTimeField(default=datetime.now)
    sample_collection = models.DateTimeField(default=datetime.now,verbose_name='Sample Collection')
    sample_received = models.DateTimeField(default=datetime.now,verbose_name='Sample Received')
    report_released = models.DateTimeField(default=datetime.now,verbose_name='Report Release')
    created_at = models.DateTimeField(auto_now_add=True)
    type_of_sample = models.TextField(verbose_name='Type of Sample')
    sample_condition_of_receipt = models.CharField(max_length=124,verbose_name='Sample Condition of Receipt')
    pcr_kit = models.CharField(max_length=64,verbose_name='PCR Kit')
    n_gene = models.CharField(max_length=64,verbose_name='N gene')
    e_gene = models.CharField(max_length=64,verbose_name='E gene')
    rdrp_gene = models.CharField(max_length=64,verbose_name='RdRP gene')
    rtpcr_test = models.CharField(choices=COVID_RESULT, verbose_name='SARS-CoV2 (COVID-19) RT PCR Test result',max_length=10)
    equipment = models.CharField(max_length=64,verbose_name='Equipment')
    def __str__(self):
        return self.patient.name
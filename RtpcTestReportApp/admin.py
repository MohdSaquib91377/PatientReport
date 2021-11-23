from django.contrib import admin
from RtpcTestReportApp.models import PatientReport

class PatientReportAdmin(admin.ModelAdmin):
    list_display = ['id','srf_id','ref_by',
                    'lab_id','printed','sample_collection',
                    'sample_received','report_released',
                    'created_at'
                    ]
    list_filter = ('created_at',)
    search_fields = ("srf_id", )

    
    fieldsets = (
       
        ('Patient Info', {
            'fields': ('srf_id','ref_by',
                    'lab_id','printed','sample_collection',
                    'sample_received','report_released',),
        }),
         
        ('SARS-CoV2 (COVID-19) Real Time RT PCR Test', {
            'fields': ('type_of_sample','sample_condition_of_receipt',
                       'pcr_kit','n_gene','rdrp_gene','rtpcr_test',
                       'equipment'
            ),
        }),

      
        
        )
  
    
admin.site.register(PatientReport,PatientReportAdmin)
from django.contrib import admin
from .models import *


class ObjectivesAdmin(admin.ModelAdmin):
    list_display = (
        'id_objetives',
        'name'
    )
    list_filter = (
        'name',
    )


class ObjectiveCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id_objective_category',
        'objettives',
        'name',
    )
    list_filter = (
        'id_objective_category',
        'objettives',
        'name',
    )

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id_subcategory',
        'objective_category',
        'name',
    )
    
    list_filter = (
        'id_subcategory',
        'objective_category',
        'name',
    )


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id_question',
        'subcategory',
        'question',
        'score'
    )
    list_filter = (
        'id_question',
        'subcategory',
        'question',
    )


class ProgramAdmin(admin.ModelAdmin):
    list_display = (
        'user', 
        'name',
    )

    list_filter = (
        'user',
        'name',
    )


admin.site.register(Program, ProgramAdmin)
admin.site.register(Categorization)
admin.site.register(RiskAnalysis)
admin.site.register(Evaluation)
admin.site.register(Objectives, ObjectivesAdmin)
admin.site.register(ObjectiveCategory, ObjectiveCategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Questions, QuestionAdmin)

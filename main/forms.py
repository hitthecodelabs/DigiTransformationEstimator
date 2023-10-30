from django import forms
from .models import Categorization, RiskAnalysis, Program, Evaluation


class CategorizationForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    #self.fields['business'].widget.attrs.update({'class': 'form-control', 'hidden':'true'})
    self.fields['program']=forms.ModelChoiceField(queryset=Program.objects.filter(user=user))
    self.fields['program'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['code'].widget.attrs.update({'class': 'form-control'})
    self.fields['project'].widget.attrs.update({'class': 'form-control'})
    self.fields['project_detail'].widget.attrs.update({'class': 'form-control'})
    self.fields['year'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['category'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['dimension'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['strategic_objective'].widget.attrs.update({'class': 'form-control'})
    self.fields['total_budget'].widget.attrs.update({'class': 'form-control'})

  class Meta:
    model = Categorization
    exclude = ['user',]
    fields = [
        #'business',
        'program',
        'program',
        'code',
        'project',
        'project_detail',
        'year',
        'category',
        'dimension',
        'strategic_objective',
        'total_budget',
    ]


class RiskAnalysisModelForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    self.fields['program'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['risk'].widget.attrs.update({'class': 'form-control'})
    self.fields['sub_risk'].widget.attrs.update({'class': 'form-control'})
    self.fields['probability'].widget.attrs.update({'class': 'form-control',  'style': 'color: #666666'})
    self.fields['impact'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['risk_evaluation'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})
    self.fields['risk_categorization'].widget.attrs.update({'class': 'form-control', 'style': 'color: #666666'})

  class Meta:
    model = RiskAnalysis
    exclude = ['user',]


class ProgramModelForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    # self.user = kwargs.pop('user', None)
    super().__init__(*args, **kwargs)
    self.fields['name'].widget.attrs.update({'class': 'form-control'})

  class Meta:
    model = Program
    exclude = ['user', 'optimizations']


class EvaluationModelForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    user = kwargs.pop('user')
    super().__init__(*args, **kwargs)
    self.fields['program'].widget.attrs.update({'class': 'form-control form-control-solid form-control-lg'})
    self.fields['risk_rate'].widget.attrs.update({'class': 'form-control form-control-solid form-control-lg'})
    self.fields['inflation_rate'].widget.attrs.update({'class': 'form-control form-control-solid form-control-lg'})
    self.fields['initial_investment'].widget.attrs.update({'class': 'form-control form-control-solid form-control-lg'})
    self.fields['years'].widget.attrs.update({'class': 'form-control form-control-solid form-control-lg'})
    
  class Meta:
    model = Evaluation
    exclude = ['user']
    fields = [
      'program',
      'risk_rate',
      'inflation_rate',
      'initial_investment',
      'years',
      'total_income',
      'total_expense',
      'net_cash_flow',
      'cash_flow_at_present_value',
      'accumulated_cash_flow',
      'vpn',
      'recovery_period',
      'interal_rate_of_return',
      'return_on_investment',
    ]

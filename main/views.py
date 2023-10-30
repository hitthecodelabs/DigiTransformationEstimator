import json

import numpy as np
import numpy_financial as npf
from django.contrib import messages
from django.core import serializers
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import (CreateView, DeleteView, ListView, UpdateView,
                                  View, TemplateView)

from main.utils import fevp, vn_a, vn_a2, vp2, vp_e2, fen2, fevp2, fe_ac2
from django.http import JsonResponse

from .forms import (CategorizationForm, EvaluationModelForm, ProgramModelForm,
                    RiskAnalysisModelForm)
from .models import *


class CategoryCreateView(CreateView):
    model = Categorization
    form_class = CategorizationForm
    template_name = "categorization/form.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The record created successfully')
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return HttpResponseRedirect(reverse_lazy('list_categorization'))
            # return super().form_valid(form)
        else:
            self.object = self.get_object()
            messages.error(request, 'The update has failed.') 
            return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class CategoryListView(ListView):
    model = Categorization
    template_name="categorization/index.html"

    def get_queryset(self):
        return Categorization.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_data = serializers.serialize("json", context["object_list"])
        context["object_list"] = json_data
        return context
    

class CategoryUpdateView(UpdateView):
    model = Categorization
    form_class = CategorizationForm
    template_name="categorization/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The record updated successfully')
            return super().form_valid(form)    
        else:
            messages.error(request, 'The update has failed.')   
            return super().form_invalid(form)


class CategoryDeleteView(DeleteView):
    model = Categorization
    success_url = reverse_lazy("list_categorization")
    template_name="categorization/delete-confirm.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'The record deleted successfully!')
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect("index")


class RiskCreateView(CreateView):
    model = RiskAnalysis
    form_class = RiskAnalysisModelForm
    template_name="analysis/form.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The record created successfully')
            risk = form.save(commit=False)
            risk.user = request.user
            risk.save()
            return HttpResponseRedirect(reverse_lazy('list_risk'))
            # return super().form_valid(form) 
        else:
            self.object = self.get_object()
            messages.error(request, 'The update has failed.')   
            return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class RiskListView(ListView):
    model = RiskAnalysis
    template_name="analysis/index.html"

    def get_queryset(self):
        return RiskAnalysis.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_data = serializers.serialize("json", context["object_list"])
        context["object_list"] = json_data
        return context


class RiskUpdateView(UpdateView):
    model = RiskAnalysis
    form_class = RiskAnalysisModelForm
    template_name="analysis/form.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The record updated successfully')
            return super().form_valid(form)    
        else:
            messages.error(request, 'The update has failed.')   
            return super().form_invalid(form)


class RiskDeleteView(DeleteView):
    model = RiskAnalysis
    success_url = reverse_lazy("list_risk")
    template_name="analysis/delete-confirm.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'The record deleted successfully!')
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect("index")


class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramModelForm
    template_name="program/form.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The program created successfully')
            program = form.save(commit=False)
            program.user = request.user
            program.save()
            return HttpResponseRedirect(reverse_lazy('create_program'))
            # return super().form_valid(form)
        else:
            self.object = None
            return super().form_invalid(form)


class ProgramUpdate(UpdateView):
    model = Program

    def post(self, request, *args, **kwargs):
        pass


class EvaluationCreateView(CreateView):
    model = Evaluation
    form_class = EvaluationModelForm
    template_name="evaluation/form.html"

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            messages.success(request, 'The record created successfully')
            evaluation = form.save(commit=False)
            evaluation.user = request.user
            evaluation.save()
            return HttpResponseRedirect(reverse_lazy('list_evaluation'))
            # return super().form_valid(form)
        else:
            self.object = self.get_object()
            messages.error(request, 'The update has failed.')   
            return super().form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class EvaluationListView(ListView):
    model = Evaluation
    template_name="evaluation/index.html"

    def get_queryset(self):
        return Evaluation.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_data = serializers.serialize("json", context["object_list"])
        context["object_list"] = json_data
        context["programs"] = Evaluation.objects.filter(user=self.request.user)
        return context


class EvaluationUpdateView(UpdateView):
    model = Evaluation
    form_class = EvaluationModelForm
    template_name="evaluation/form.html"
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, 'The record updated successfully')
            return super().form_valid(form)    
        else:
            messages.error(request, 'The update has failed.')   
            return super().form_invalid(form)


class EvaluationDeleteView(DeleteView):
    model = Evaluation
    success_url = reverse_lazy("list_risk")
    template_name="evaluation/delete-confirm.html"

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'The record deleted successfully!')
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect("index")


@csrf_exempt
@require_http_methods(['POST'])
def update_program(request):
    data = json.loads(request.body)
    mi_program = Program.objects.filter(name=data['project']).first()
    mi_program.optimizations = ''
    mi_program.optimizations = json.dumps(data)
    mi_program.save()
    return JsonResponse({
        'messaje': 'ok'
    })

@csrf_exempt
@require_http_methods(['POST'])
def calculate_cash_flow(request):
    if request.is_ajax:
        form_data = request.POST
        tasa_inflacion = float(form_data['inflation_rate'])
        inversion_inicial = float(form_data['initial_investment'])
        total_income = [float(income) for income in form_data['total_income'].split(",")]
        total_expense = [float(expense) for expense in form_data['total_expense'].split(",")]
        R1 = vn_a(total_income, tasa_inflacion)
        R2 = vn_a(total_expense, tasa_inflacion)
        arr = np.array([R1, R2])
        total_income_c = list(arr[0])[-1]
        total_expense_c = list(arr[1])[-1]

        flujo_efectivo_neto_0 = arr[0, :-1] - arr[1, :-1]
        flujo_efectivo_neto = vn_a2(flujo_efectivo_neto_0[1:], flujo_efectivo_neto_0, tasa_inflacion, inversion_inicial)
        net_cash_flow = flujo_efectivo_neto[-1]

        flujo_efectivo_valor_presente = fevp(flujo_efectivo_neto, tasa_inflacion)
        cash_flow_at_present_value = flujo_efectivo_valor_presente[-1]

        iii = flujo_efectivo_valor_presente[1:]
        flujo_efectivo_acumulado = [flujo_efectivo_valor_presente[0]]
        for j in iii:
            KO = j + flujo_efectivo_acumulado[-1]
            flujo_efectivo_acumulado.append(KO)
        flujo_efectivo_acumulado = np.array(flujo_efectivo_acumulado)
        accumulated_cash_flow = flujo_efectivo_acumulado[-1]

        cont = 0
        part = 0
        n = 0
        '''
        while n < inversion_inicial:
            n += flujo_efectivo_acumulado[part]
            part += 1

        vpn = flujo_efectivo_neto[-1]
        abajo = flujo_efectivo_acumulado[part - 2]
        arriba = flujo_efectivo_valor_presente[part - 1]
        recovery_period = (part - 1) + ((inversion_inicial - abajo) / arriba)
        interal_rate_of_return = npf.irr(flujo_efectivo_neto[:-1]) * 100
        return_on_investment = (arr[0, -1] - arr[1, -1])/arr[1, -1]
        '''
        
        '''
        '''
        total_ingresos2 = total_income + [vp2(total_income, tasa_inflacion)]
        total_egresos2 = total_expense + [vp2(total_expense, tasa_inflacion)]
        fe_n2 = fen2(total_income, total_expense, tasa_inflacion)
        fe_vp2 = fevp2(fe_n2, tasa_inflacion)
        flujo_ea2 = fe_ac2(fe_vp2)
        
        
        VPN = fe_n2[-1]
        
        cont = 0
        part = 0
        n = 0

        #while n < inversion_inicial:
        #    n += flujo_ea2[part]
        #    part += 1
        for val in flujo_ea2:
            if n<inversion_inicial:
                n+=val
                part+=1
            # n+=val

        abajo = flujo_ea2[part - 2]
        arriba = fe_vp2[part - 1]
        izq = part - 1
        if (part - 2)<0:
            abajo = 0
        derecha = ((inversion_inicial - abajo) / arriba)
        #print(derecha, "derecha")
        #print(izq, "izq")
        recovery_period = izq + derecha
        #print(fe_n2[:-1], "fe_n2")
        TIR = npf.irr(fe_n2[:-1])*100
        roi = (total_ingresos2[-1]-total_egresos2[-1])/total_egresos2[-1]

        '''
        
        return JsonResponse({
            'total_income': total_income_c,
            'total_expense': total_expense_c,
            'net_cash_flow': net_cash_flow,
            'cash_flow_at_present_value': cash_flow_at_present_value,
            'accumulated_cash_flow': accumulated_cash_flow,
            'vpn': vpn,
            'recovery_period': recovery_period,
            'interal_rate_of_return': interal_rate_of_return,
            'return_on_investment': return_on_investment
        })
        '''
        #print(total_income_c,total_expense_c,net_cash_flow,cash_flow_at_present_value,accumulated_cash_flow,round(VPN, 2),recovery_period,interal_rate_of_return,return_on_investment)
        print(round(total_ingresos2[-1], 2),round(total_egresos2[-1], 2),round(fe_n2[-1], 2),round(fe_vp2[-1], 2),round(flujo_ea2[-1], 2),round(VPN, 2),round(recovery_period, 2),round(TIR, 2),round(roi, 2))
        return JsonResponse({
            'total_income': round(total_ingresos2[-1], 2),
            'total_expense': round(total_egresos2[-1], 2),
            'net_cash_flow': round(fe_n2[-1], 2),
            'cash_flow_at_present_value': round(fe_vp2[-1], 2),
            'accumulated_cash_flow': round(flujo_ea2[-1], 2),
            'vpn': round(VPN, 2),
            'recovery_period': round(recovery_period, 2),
            'interal_rate_of_return': round(TIR, 2),
            'return_on_investment': round(roi, 2)
        })


class OptimizationView(View):
    template_name = "optimization/index.html"

    def get(self, request, *args, **kwargs):
        programs = Program.objects.filter(user=request.user)

        return render(
            request, 
            self.template_name, 
            {'programs': programs}
        )


def questions_get(request):
    """Retorna un json de las preguntas"""
    objetives = Objectives.objects.all()
    objetives_ser = [
        {'id_objetive': ob.id_objetives, 'name': ob.name, 'complete': 0}
        for ob in objetives
    ]

    objetive_category = ObjectiveCategory.objects.all()
    objetive_category_ser = [
        {
            'id_objective_category': ob.id_objective_category, 
            'id_objetive': ob.objettives_id , 
            'name': ob.name,
            'complete': 0,
        }
        for ob in objetive_category
    ]

    subcategory = Subcategory.objects.all()
    subcategory_ser = [
        {
            'id_subcategory': sb.id_subcategory,
            'objective_category_id': sb.objective_category_id,
            'name': sb.name,
            'complete': 0,
        }
        for sb in subcategory
    ]

    questions = Questions.objects.all()
    questions_ser = [
        {
            'id_question': q.id_question, 
            'id_subcategory': q.subcategory_id, 
            'question': q.question, 
            'score': q.score,
            'selected': 0,
        }
        for q in questions
    ]

    data = {
        'objectives': objetives_ser,
        'objectives_categories': objetive_category_ser,
        'subcategory': subcategory_ser,
        'questions': questions_ser,
    }
    data = json.dumps(data, ensure_ascii= False)
    return JsonResponse(data, safe=False,)


# Retorna el quiz de un programa
def questions_project(request, project):
    my_program = Program.objects.filter(name=project).first()
    data = None

    if bool(my_program.optimizations) == True:
        data = json.loads(my_program.optimizations)
        print('Retornamos datos existentes para {}'.format(my_program.name))
    else:
        objetives = Objectives.objects.all()
        objetives_ser = [
            {'id_objetive': ob.id_objetives, 'name': ob.name, 'complete': 0}
            for ob in objetives
        ]

        objetive_category = ObjectiveCategory.objects.all()
        objetive_category_ser = [
            {
                'id_objective_category': ob.id_objective_category, 
                'id_objetive': ob.objettives_id , 
                'name': ob.name,
                'complete': 0,
            }
            for ob in objetive_category
        ]

        subcategory = Subcategory.objects.all()
        subcategory_ser = [
            {
                'id_subcategory': sb.id_subcategory,
                'objective_category_id': sb.objective_category_id,
                'name': sb.name,
                'complete': 0,
            }
            for sb in subcategory
        ]

        questions = Questions.objects.all()
        questions_ser = [
            {
                'id_question': q.id_question, 
                'id_subcategory': q.subcategory_id, 
                'question': q.question, 
                'score': q.score,
                'selected': 0,
            }
            for q in questions
        ]
        print('Retornamos datos nuevos para {}'.format(my_program.name))
        data = {
            'project' : project,
            'quiz': {
            'objectives': objetives_ser,
            'objectives_categories': objetive_category_ser,
            'subcategory': subcategory_ser,
            'questions': questions_ser,
        }}
    data = json.dumps(data, ensure_ascii=False)
    return JsonResponse(data, safe=False)


class UpdateUserBussiness(TemplateView):
    template_name="bussines.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        enterprise = request.POST
        user = request.user
        user.first_name = enterprise['first_name']
        user.save()
        return HttpResponseRedirect('/home/')

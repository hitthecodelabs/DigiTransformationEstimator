from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

YEAR_LIST = (
  ('2020', 2020),
  ('2021', 2021),
  ('2022', 2022)
)

CATEGORY_LIST = (
  ("must_do", "Must do"),
  ("wont_do", "Won’t do"),
  ("may_do", "May do")
)

DIMENSION_LIST = (
  ("customers", "Clientes"),
  ("strategy", "Estrategia"),
  ("technology", "Tecnología"),
  ("operations", "Operaciones"),
  ("culture", "Cultura"),
  ("data", "Datos"),
  ("clients_strategy", "Clientes/Estrategia"),
  ("clients_technology", "Clientes/Tecnología"),
  ("clients_culture", "Clientes/Cultura"),
  ("clients_data", "Clientes/Datos"),
)

PROBABILITY_LIST = (
  ("0.9", "CASI SEGURO"),
  ("0.7", "PROBABLE"),
  ("0.5", "POSIBLE"),
  ("0.3", "IMPROBABLE"),
  ("0.1", "RARA VEZ")
)

IMPACT_LIST = (
  ("0.05", "MUY BAJO"),
  ("0.1", "BAJO"),
  ("0.2", "MODERADO"),
  ("0.4", "ALTO"),
  ("0.8", "MUY ALTO")
)

RISK_CATEGORIZATION_LIST = (
  ("Slow Risk", "Slow Risk"),
  ("Moderate Risk", "Moderate Risk"),
  ("High Risk", "High Risk")
)


class Program(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField(_("Program Name"), max_length=50, unique=True)
  optimizations = models.TextField(default=None, blank=True, null=True)
  
  def __str__(self):
      return self.name
  
  def get_absolute_url(self):
      return reverse("create_program")
  

class Categorization(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  business = models.CharField(_("EMPRESA"), max_length=50)
  program = models.ForeignKey(Program, on_delete=models.CASCADE)
  code = models.IntegerField(_("CÓDIGO"))
  project = models.CharField(_("PROYECTO"), max_length=50)
  project_detail = models.CharField(_("DETALLE DE PROYECTO"), max_length=50)
  year = models.CharField(_("AÑO"), choices=YEAR_LIST, default="2021", max_length=50)
  category = models.CharField(_("CATEGORIZACIÓN"), choices=CATEGORY_LIST, default="must_do", max_length=50)
  dimension = models.CharField(_("DIMENSIÓN"), choices=DIMENSION_LIST, default="customers", max_length=50)
  strategic_objective = models.CharField(_("OBJETIVO ESTRATÉGICO"), max_length=50)
  total_budget = models.FloatField(_("PRESUPUESTO TOTAL"))

  def get_absolute_url(self):
      return reverse("list_categorization")

  def __str__(self):
    return self.business
  

class RiskAnalysis(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  program = models.ForeignKey(Program, on_delete=models.CASCADE)
  risk = models.CharField(_("RISK"), max_length=50)
  sub_risk = models.CharField(_("RISK FACTOR's"), max_length=50)
  probability = models.CharField(_("PROBABILIDAD"), choices=PROBABILITY_LIST, default="0.9", max_length=50)
  impact = models.CharField(_("IMPACTO"), choices=IMPACT_LIST, default="0.05", max_length=50)
  risk_evaluation = models.FloatField(_("EVALUACIÓN DE RIESGO"))
  risk_categorization = models.CharField(_("RISK CATEGORIZATION"), choices=RISK_CATEGORIZATION_LIST, max_length=50)

  def get_absolute_url(self):
      return reverse("list_risk")

  def __str__(self):
    return self.risk


class Evaluation(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  program = models.ForeignKey(Program, on_delete=models.CASCADE)
  # risk_rate = models.FloatField(_("Tasa de Riesgo"))
  # inflation_rate = models.FloatField(_("Tasa de Inflación"))
  risk_rate = models.FloatField(_("Tasa"))
  inflation_rate = models.FloatField(_("Tasa de Interés"))
  initial_investment = models.FloatField(_("Inversion Inicial"))
  years = models.IntegerField(_("AÑOS"))
  total_income = models.FloatField(_("TOTAL INGRESOS"))
  total_expense = models.FloatField(_("TOTAL EGRESOS"))
  net_cash_flow = models.FloatField(_("Flujo de Efectivo Neto"))
  cash_flow_at_present_value = models.FloatField(_("Flujo de efectivo a Valor Presente"))
  accumulated_cash_flow = models.FloatField(_("Flujo de Efectivo Acumulado"))
  vpn = models.FloatField(_("VPN"))
  recovery_period = models.FloatField(_("Periodo de Recuperación"))
  interal_rate_of_return = models.FloatField(_("Tasa Interna de Retorno"))
  return_on_investment = models.FloatField(_("Retorno sobre la Inversión ROI"))

  def __str__(self):
    return self.program.name

  def get_absolute_url(self):
    return reverse("list_evaluation")


class Objectives(models.Model):
  id_objetives = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)

  def __str__(self):
      return self.name
  

class ObjectiveCategory(models.Model):
  id_objective_category = models.AutoField(primary_key=True)
  objettives = models.ForeignKey(
    Objectives,
    on_delete=models.CASCADE
  )
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name


class Subcategory(models.Model):
  id_subcategory = models.AutoField(primary_key=True)
  objective_category = models.ForeignKey(
    ObjectiveCategory, 
    models.CASCADE,
    )
  name = models.CharField(max_length=250)

  def __str__(self):
    return self.name


class Questions(models.Model):
  id_question = models.AutoField(primary_key=True)
  subcategory = models.ForeignKey(Subcategory, models.CASCADE)
  question = models.TextField()
  score = models.FloatField()
from django.urls import path
from django.contrib.auth.decorators import login_required

from main import views

urlpatterns = [
    path('home/', login_required(views.UpdateUserBussiness.as_view(template_name="bussines.html")), name="home"),
    path('categories/', login_required(views.CategoryListView.as_view()), name="list_categorization"),
    path('categories/create/', login_required(views.CategoryCreateView.as_view()), name="create_categorization"),
    path('categories/update/<pk>/', login_required(views.CategoryUpdateView.as_view()), name="update_categorization"),
    path('categories/delete/<pk>/', login_required(views.CategoryDeleteView.as_view()), name="delete_categorization"),
    path('risks/', login_required(views.RiskListView.as_view()), name="list_risk"),
    path('risks/create/', login_required(views.RiskCreateView.as_view()), name="create_risk"),
    path('risks/update/<pk>/', login_required(views.RiskUpdateView.as_view()), name="update_risk"),
    path('risks/delete/<pk>/', login_required(views.RiskDeleteView.as_view()), name="delete_risk"),
    path('program/create/', login_required(views.ProgramCreateView.as_view()), name="create_program"),
    path('evaluations/', login_required(views.EvaluationListView.as_view()), name="list_evaluation"),
    path('evaluation/create/', login_required(views.EvaluationCreateView.as_view()), name="create_evaluation"),
    path('evaluation/update/<pk>/', login_required(views.EvaluationUpdateView.as_view()), name="update_evaluation"),
    path('evaluation/delete/<pk>/', login_required(views.EvaluationDeleteView.as_view()), name="delete_evaluation"),
    path('cal_cash_flow/', login_required(views.calculate_cash_flow), name="calculate_cash_flow"),
    path('program/update/', login_required(views.update_program), name="update_program"),
    path('optimizations/', login_required(views.OptimizationView.as_view()), name="optimization"),
    path('questions/', views.questions_get, name="questions-json"),
    path('questions-projects/<str:project>/', views.questions_project, name="questions-project-json"),
]

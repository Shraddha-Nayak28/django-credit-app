from django.urls import path
from .views import register_customer, check_customer_eligibility, create_loan

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('check-eligibility/', check_customer_eligibility, name='check_customer_eligibility'),
    path('create-loan/', create_loan, name='create_loan'),
]

from .views import view_loans

urlpatterns += [
    path('view-loans/<str:customer_id>/', view_loans, name='view_loans'),
]

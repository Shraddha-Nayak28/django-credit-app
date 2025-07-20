from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Application
from .serializers import CustomerSerializer
from .eligibility import check_eligibility
from django.utils import timezone
import random
import json


@api_view(['POST'])
def register_customer(request):
    try:
        data = request.data

        salary = data.get('monthly_income')
        if salary is None:
            return Response({'error': "Missing field 'monthly_income'"}, status=status.HTTP_400_BAD_REQUEST)
        salary = int(salary)

        approved_limit = round((36 * salary) / 100000) * 100000

        customer = Customer.objects.create(
            customer_id=data.get('customer_id', f"CU{random.randint(100000, 999999)}"),
            name=f"{data.get('first_name', '')} {data.get('last_name', '')}".strip(),
            age=int(data.get('age', 0)),
            gender=data.get('gender', 'Not Specified'),
            income=salary,
            employment_status=data.get('employment_status', 'Unemployed'),
            approved_limit=approved_limit
        )

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except KeyError as e:
        return Response({'error': f"Missing field {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({'error': 'Invalid data type in request'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def check_customer_eligibility(request):
    try:
        data = request.data

        if not data or 'monthly_income' not in data:
            try:
                data = json.loads(request.body.decode('utf-8'))
            except Exception as e:
                return Response({'error': f"Invalid JSON format: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        salary = data.get('monthly_income')
        if salary is None:
            return Response({'error': "Missing field 'monthly_income'"}, status=status.HTTP_400_BAD_REQUEST)
        salary = int(salary)

        approved_limit = round((36 * salary) / 100000) * 100000

        customer = Customer.objects.create(
            customer_id=data.get('customer_id', f"CU{str(salary)[-4:]}{random.randint(100, 999)}"),
            name=f"{data.get('first_name', '')} {data.get('last_name', '')}".strip(),
            age=int(data.get('age', 0)),
            gender=data.get('gender', 'Not Specified'),
            income=salary,
            employment_status=data.get('employment_status', 'Unemployed'),
            approved_limit=approved_limit
        )

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except KeyError as e:
        return Response({'error': f"Missing field {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    except ValueError:
        return Response({'error': 'Invalid data type in request'}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def create_loan(request):
    return Response({"message": "Loan creation endpoint working!"}, status=200)

from django.shortcuts import get_object_or_404
import math

@api_view(['POST'])
def check_customer_eligibility(request):
    data = request.data

    required_fields = ['customer_id', 'loan_amount', 'interest_rate', 'tenure']
    for field in required_fields:
        if field not in data:
            return Response({'error': f"Missing field '{field}'"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        customer = get_object_or_404(Customer, customer_id=data['customer_id'])
        loan_amount = float(data['loan_amount'])
        interest_rate = float(data['interest_rate'])
        tenure = int(data['tenure'])

        # Use your actual eligibility function here:
        result = check_eligibility(customer, loan_amount, interest_rate, tenure)

        return Response(result, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from .models import Loan
from .serializers import LoanSerializer
import math

@api_view(['POST'])
def create_loan(request):
    data = request.data
    try:
        customer_id = data.get('customer_id')
        customer = Customer.objects.get(customer_id=customer_id)

        loan = Loan.objects.create(
            customer=customer,
            loan_amount=data.get('loan_amount'),
            interest_rate=data.get('interest_rate'),
            tenure=data.get('tenure'),
            monthly_installment=data.get('monthly_installment')
        )

        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

from .models import Loan, Customer
from .serializers import LoanSerializer

@api_view(['GET'])
def view_loans(request, customer_id):
    try:
        customer = Customer.objects.get(customer_id=customer_id)
        loans = Loan.objects.filter(customer=customer)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

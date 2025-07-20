# Django Credit App

A Django-based Credit Approval System that allows customers to register, check loan eligibility, and create loan applications. This system uses predefined business logic to approve or reject loans based on customer financial information.

---

## 🚀 Features

- ✅ Customer registration with monthly income and personal details
- ✅ Automatic loan approval limit calculation
- ✅ Loan eligibility check based on credit rules
- ✅ Loan creation with EMI calculations
- ✅ Django REST Framework APIs
- ✅ Dockerized environment for easy setup
- ✅ Postman-friendly API structure
- ✅ Built-in credit approval logic based on income and loan terms

---

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Task Queue**: Celery (future integration possible)
- **Queue Broker**: Redis
- **Containerization**: Docker & Docker Compose
- **Testing & API Demo**: Postman

---

## 🛠️ API Endpoints

### 1. Register Customer  
**POST** `/api/register/`
```json
{
  "customer_id": "CU123456",
  "first_name": "John",
  "last_name": "Doe",
  "age": 30,
  "gender": "Male",
  "monthly_income": 50000,
  "employment_status": "Salaried"
}
```

2. Check Loan Eligibility
POST /api/check-eligibility/
{
  "customer_id": "CU123456",
  "loan_amount": 100000,
  "interest_rate": 12,
  "tenure": 12
}


Sample Response
{
  "customer_id": "CU123456",
  "approval": true,
  "interest_rate": 12.0,
  "corrected_interest_rate": 16.0,
  "tenure": 12,
  "monthly_installment": 8887.45,
  "approval_details": "Customer eligible"
}

 3.Create Loan
POST /api/create-loan/

{
  "customer_id": "CU123456",
  "loan_amount": 100000,
  "interest_rate": 12.0,
  "tenure": 12,
  "monthly_installment": 8887.45
}

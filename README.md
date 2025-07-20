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

---

## 📦 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Task Queue**: Celery (for future extensions)
- **Queue Broker**: Redis
- **Containerization**: Docker & Docker Compose

---

## 🛠️ API Endpoints

### 1. Register Customer
`POST /api/register/`

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

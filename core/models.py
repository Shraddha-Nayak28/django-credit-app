from django.db import models


class Customer(models.Model):
    customer_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    employment_status = models.CharField(max_length=30)
    approved_limit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    tenure = models.IntegerField()
    monthly_installment = models.DecimalField(max_digits=12, decimal_places=2)
    emi_paid_on_time = models.BooleanField(default=True)
    start_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Loan {self.id} - {self.customer.customer_id}"



class Application(models.Model):
    application_id = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_purpose = models.CharField(max_length=100)
    loan_term = models.IntegerField(help_text="Loan term in months")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # ✅ ADD THIS
    credit_score = models.IntegerField()
    approval_status = models.CharField(max_length=10, choices=[
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected')
    ])


    def __str__(self):
        return f"{self.application_id} - {self.customer.name}"

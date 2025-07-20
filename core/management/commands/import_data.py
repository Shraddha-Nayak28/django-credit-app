import pandas as pd
from django.core.management.base import BaseCommand
from core.models import Customer, Application

class Command(BaseCommand):
    help = 'Import customer and application data from Excel files'

    def handle(self, *args, **kwargs):
        # Load customer data
        customer_df = pd.read_excel('customer_data.xlsx')
        for _, row in customer_df.iterrows():
            Customer.objects.update_or_create(
                customer_id=row['Customer ID'],
                defaults={
                    'name': row['First Name'] + ' ' + row['Last Name'],
                    'age': row['Age'],
                    'gender': 'Unknown',  # No gender field, so defaulting
                    'income': row['Monthly Salary'],
                    'employment_status': 'Unknown'  # No info, so placeholder
                }
            )
        self.stdout.write(self.style.SUCCESS("✅ Customer data imported."))

        # Load application data
        application_df = pd.read_excel('loan_data.xlsx')
        for _, row in application_df.iterrows():
            try:
                customer = Customer.objects.get(customer_id=(row['Customer ID']))
                Application.objects.update_or_create(
                    application_id=row['Loan ID'],
                    defaults={
                        'customer': customer,
                        'loan_amount': row['Loan Amount'],
                        'loan_term': row['Tenure'],
                        'interest_rate': row['Interest Rate'],
                        'loan_purpose': 'General',  # or any default value
                        'credit_score': 700,  # optional placeholder
                        'approval_status': 'Approved'  # optional placeholder
                    }
                )

            except Customer.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"⚠️ Customer {row['Customer']} not found. Skipping."))

        self.stdout.write(self.style.SUCCESS("✅ Application data imported."))

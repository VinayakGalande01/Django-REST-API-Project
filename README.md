# Django-REST-API-Project

# Project: Company Management System

This project is a Django-based application designed to manage company information, including company names, locations, and types. Recent updates include dynamic handling of company details such as locations (Pune, Mumbai) and company types (IT, Biotech).



📌 Features
✔️ Django Admin Panel for managing companies & employees.
✔️ RESTful APIs using Django REST Framework.
✔️ Company & Employee Management (CRUD operations).
✔️ Search & Filters for admin panel.
✔️ Hyperlinked API with serializers.
✔️ SQLite/PostgreSQL/MySQL support.
✔️ Modular structure for future scalability.
- Integrated with Django ORM for efficient database operations


📂 Project Structure

/api_project  
│── api/  
│   ├── migrations/       # Database migrations  
│   ├── templates/        # (Optional) Frontend templates  
│   ├── admin.py          # Django admin customization  
│   ├── models.py         # Database models (Company, Employee)  
│   ├── serializers.py    # Django REST Framework serializers  
│   ├── views.py          # API Views (CRUD operations)  
│   ├── urls.py           # API Endpoints  
│   ├── tests.py          # Unit tests (if needed)  
│── api_project/  
│   ├── settings.py       # Django project settings  
│   ├── urls.py           # Project-level URL configurations  
│── manage.py             # Django CLI tool  


### 1️⃣ Clone the Repository
```bash
# Replace with your GitHub repository URL
git clone https://github.com/your-username/company-management.git
cd company-management
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Run the Server
```bash
python manage.py runserver
```

Access the app at `http://127.0.0.1:8000/` 🚀


🔮 Future Improvements & Scope

🚀 Frontend Integration using HTML, Bootstrap, JavaScript (AJAX/Fetch API).
🚀 Token-based Authentication (JWT or OAuth).
🚀 Dockerizing the App for easy deployment.
🚀 Deploying on AWS, DigitalOcean, or Heroku.
🚀 Unit & Integration Testing with Pytest.
🚀 Adding Role-Based Access Control (RBAC).
🚀 Caching & Performance Optimizations.

---


## ⚡ Database Update Script
```python
from api.models import Company

# Fetch companies
companies = list(Company.objects.all())

# Update first company to Pune & IT
if len(companies) >= 1:
    company1 = companies[0]
    company1.location = 'Pune'
    company1.type = 'IT'
    company1.save()

# Update second company to Mumbai & Biotech
if len(companies) >= 2:
    company2 = companies[1]
    company2.location = 'Mumbai'
    company2.type = 'Biotech'
    company2.save()

# Verify updates
for company in Company.objects.all():
    print(f"Name: {company.name}, Location: {company.location}, Type: {company.type}")
```


Happy Coding! 🚀


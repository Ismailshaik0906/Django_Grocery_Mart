

Django GroceryMart is a web application built using the Django framework that allows users to browse, add to cart, and order grocery items online. It provides an intuitive interface for both customers and administrators to manage products, orders, and user accounts.

Features:

-User authentication (Login/Signup)
-Product listing with categories
-Shopping cart functionality
-Search functionality
-Order management
-Admin panel for product and order management
-Responsive design for mobile and desktop

Installation:

Prerequisites:
Ensure you have the following installed:
Python (>=3.x)
Django (>=3.x)
Virtual environment (optional but recommended)

Steps to Setup

1. Clone the repository:
git clone https://github.com/Ismailshaik0906/django-grocerymart.git
cd django-grocerymart

2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows

3. Install dependencies:
pip install -r requirements.txt

4. Apply migrations:
python manage.py migrate

5. Create a superuser (for admin access):
python manage.py createsuperuser

6. Run the development server:
python manage.py runserver

7. Open the application in your browser:
http://127.0.0.1:8000/

Project Structure:

├── grocerymart/
│   ├── manage.py
│   ├── Account/ (Main Django Project)
│   ├── cartapp/ (Product Management App)
│   ├── category/ (User Authentication App)
│   ├── orderapp/ (Order Processing App)
│   ├── templates/ (HTML Templates)
│   ├── static/ (CSS, JS, Images)

Technologies Used:
Backend: Django, Django REST Framework
Database: SQLite/PostgreSQL/MySQL
Frontend: HTML, CSS, JavaScript, Bootstrap

Future Enhancements:
Implementing a recommendation system
Adding a rating and review system
Integrating a delivery tracking system

Contact:
For any queries, reach out to:
SHAIK ISMAIL
Email: sk.ismail0906@gmail.com
GitHub: [MyGitHubProfile](https://github.com/Ismailshaik0906)


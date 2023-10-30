# DigiTransformationEstimator

This project represents the evolution of a system initially based on Excel into a robust and user-friendly web solution for managing and estimating digital projects.

## Background

The original Excel system allowed users to input information about digital projects, estimating the annual earnings for the first few years to calculate financial metrics such as Net Present Value, IRR, and Present Value. Despite its utility, the interface was not the most suitable for client interactions. For this reason, a decision was made to transform this tool into a web application, aiming to not only enhance the user experience but also provide a more effective and professional graphical representation.

## Web Development Features

The web project was developed using the Django framework and has the following features:

- User registration and login interface.
- Registration and management of digital transformation projects.
- Budget estimation and management.
- Project classification by categories.
- Graphical visualization developed with Vue.js, showcasing cost and earnings projections.

## Technologies Used

- **Backend**: Python with Django
- **Frontend**: Vue.js

## How to Run the Project?

1. **Clone the Repository**
   ```bash
   git clone [Repository URL]
   cd [Repository Name]
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Perform Django Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

5. Navigate to `http://127.0.0.1:8000/` in your browser to access the project.

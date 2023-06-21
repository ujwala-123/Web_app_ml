# Iris Flower Species Web Application using Django Framework

In this project, I have created a web application using the Django framework that leverages machine learning to predict the species of an iris flower based on its sepal length, sepal width, petal length, and petal width. By integrating a pre-trained model with Django's user-friendly interface, I have developed a platform where I can easily input the measurements of an iris flower and obtain an accurate prediction for its species. This application showcases the seamless integration of Django and machine learning, providing me with a convenient and efficient tool to identify the species of iris flowers based on their physical attributes.

## Files Uploaded
The following files are included in this repository:
1. 'README.md': This file provides an overview of the project.
2. 'demoapp/': This directory contains the web application files, including models, views, templates, URL configuration, encoded dataset CSV file, and python file to extract the encoded dataset.
3. 'myproject/': This directory contains Django project settings and configuration files.
4. 'manage.py': This Django management script initiates operations like running the development server and migrating the database.

## Procedure to build the Web app
### Set Up the Development Environment
   Install Django, and Python and set up the environment.
### Create Django Project
1. Create a project using the following command in the terminal after navigating to the directory. 
django-admin startproject myproject
2. Navigate to the project directory
cd myproject
### Create Django App
1. In the project directory, create a new Django app using following command:<br>
python manage.py startapp demoapp
2. update this app name in 'INSTALLED_APPS' list in settings.py in the project directory.
### Set Up URL routing:
1. I defined URL patterns in urls.py in demoapp for creating two pages ('index' and 'predict') and connected them to corresponding views.
2. The code is available in 'demoapp/urls.py'.
### Create Views:
1. Views handle user requests and return responses.
2. I have created two functions for 'index' and 'predict'.
3. Each function takes a request and gets the response from the model by giving instances.
4. The code is available in 'demoapp/views.py'.
### Define Models:
1. In models.py, I defined models for all the features of the Iris dataset in class Iris and also defined the 'ipredict_species' functions in the class.
2. Here, 'predict_species' function has a machine learning model (Logistic Regression) and the predicted value gives to views.
3. The code is available in 'demoapp/models.py'.
### Create Templates
1. Created two HTML templates in the templates directory of demoapp to define the structure and layout of web pages. These templates dynamically display data from the views.
2. The HTML files available in 'demoapp/templates'
### Run Migrations
1. Run migrations to create the necessary database tables: <br>
python manage.py makemigrations<br>
python manage.py migrate
### Run the WebApplication
1. Run the development server using the following command.<br>
python manage.py runserver

## Web App
The 'Predict' web page:
![Screenshot (194)](https://github.com/ujwala-123/Web_app_ml/assets/72090397/4aa63451-e87d-4a30-9a59-c8060b4879cc)
The 'index' web page:
![Screenshot (195)](https://github.com/ujwala-123/Web_app_ml/assets/72090397/6c32ba54-87c7-40b7-9cc7-4d6b61e2b9d3)








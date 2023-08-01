 # Data Application

Data Application is a Django-based web application that allows users to manage and analyze data. This application provides various features for data visualization, manipulation, and Ploting.


## Overview

The project is about building a simple dataApplication - where a user is able to upload a dataset, view the list of uploaded datasets. Select a dataset and create visualizations to analyze the data.

## Requirements
 - Python (Version: 3.11.0)
 - Django (Version: 4.2.3)
 - Pip (Version: 23.2.1)
 - Plotly.js (Version: 5.15.0)
 - Pandas (Version: 2.0.3)
   
## Installations
Steps to run the project:
1. Create a Project Folder
- mkdir Data Application
2. Install Virtual Environment
- python -m venv myenv
3. Install Django
- pip install django
4. Upgrade pip package installer
- python -m pip install --upgrade pip
5. Migrations
- python manage.py makemigrations
- python manage.py migrate
6. Create a Superuser to access admin
- python  manage.py createsuperuser (give username and password)
7. Run the Application
- python manage.py runserver
8. If any error occurs "module not found" then install the package using pip
- e.g (pip install pandas)

## Features
- Data Visualization
- RESTful API
- Dataset Upload
- Dataset Management
- User-Friendly Interface

## How to Use;

Upload Dataset:

Navigate to the "Data" section.
Click on the "Upload" button and select the dataset csv file from your computer.
Wait for the upload process to complete.

View Uploaded Datasets:

Go to the "Fetch Data" section to see a list of datasets you have uploaded.
You should see the names and details of each uploaded dataset.

Compute Data:

Navigate to Compute Data section and click on the name of the dataset you want to analyze and give data name, column name(column1, column2) and click on Result to see the value

Data Visualization:

Navigate to Data section and select the dataset details page, explore the various visualization options available.
Select the columns and click on plot to see the data visualization.
 

  
               


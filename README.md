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

### Upload Dataset:

Navigate to the "Data" section.
Click on the "Upload" button and select the dataset csv file from your computer.
Wait for the upload process to complete.

![Screenshot (18)](https://github.com/Ishan854/DataApplication/assets/50164669/c44a99fb-b144-478c-abfe-530c56dd49ec)

### View Uploaded Datasets:

Go to the "Fetch Data" section to see a list of datasets you have uploaded.
You should see the names and details of each uploaded dataset.

![Screenshot (19)](https://github.com/Ishan854/DataApplication/assets/50164669/951c0268-7a5c-46ba-a7e2-b7b8baeb5760)


### Compute Data:

Navigate to Compute Data section and click on the name of the dataset you want to analyze and give data name, column name(column1, column2) and click on Result to see the value

![Screenshot (20)](https://github.com/Ishan854/DataApplication/assets/50164669/c80c6295-1a01-4e7e-adc7-782252c3a1cc)

### Data Visualization:

Navigate to Data section and select the dataset details page, explore the various visualization options available.
Select the columns and click on plot to see the data visualization.

![Screenshot (21)](https://github.com/Ishan854/DataApplication/assets/50164669/bee26a32-6f06-48f0-83c6-1a973a409c42)

### For your reference I have created a demo video for this Project follow the link.
https://clipchamp.com/watch/uyz8JaB7PGe

## Contact

For any queries, you can reach me at:
- Email: srivastava.ishan854@gmail.com
- LinkedIn: [@Kumar Ishan](https://www.linkedin.com/in/kumar-ishan-502950182/)
- GitHub: [@ishan854](https://github.com/Ishan854)

  
               


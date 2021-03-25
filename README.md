# WORKFINDER API

## INTRODUCTION
This API contains endpoints that take csv files, store the data in the files and display the data as a visualize graph. 


## Design decision 
using simple html code, each endpoint should display the upload button and once the button is clicked and file is uploaded, a calculated graph should be displayed 

# How to run the application
To load in all python dependencies, go to the project directory name "finder"
* pip install -r requirements.txt (Python 2), 
* pip3 install -r requirements.txt (Python 3)


### migrate the database, run the following command in the command prompt
py manage.py makemigrations
py manage.py migrate

### start Django server
py manage.py runserver
* use the link below for direct access to the endpoints
* http://127.0.0.1/api/endpoint/

### Limitation of implementation
not hosted online

### IDEAS FOR IMPROVEMENTS
* permission should be included so authenticated users alone should be allowed to upload datas

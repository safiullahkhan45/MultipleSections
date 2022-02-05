# Multiple Sections/Subsections Creation using Django and DRF

## Introduction
The given repository shows how to create multiple sections and subsections in Django and DRF.

## API EndPoints
- create_section</br>
  This endpoint serves two puposes. You can hit it the following way to serve the required purpose.
  - Hit this endpoint over a POST Method with only title in request.data to save a section.
  - Hit this endpoint over a POST Method with title and parent_section (id) in request.data to save a subsection.

- get_section</br>
  This endpoint returns a particular section along with its parent and child sections in a nested format.
  - Hit this endpoint over a GET Method with the id of the section in request.query_params.
  - The param used here is 'section'.

- get_all_sections</br>
  This endpoint returns all the sections along with their parent and child sections in a nested format.
  - Hit this endpoint over a GET Method with no parameters.
  
## How to Install
To install you need to follow the following simple steps.
- Clone this repository
- Create & activate a Virtual Python Environment by running following commands.
```
pip install virtualenv
virtualenv env
source env/bin/activate
```
- Instatll the required packages from `requirements.txt` file using:
`pip install -r requirements.txt`

- Run the following command to setup the database
```
python manage.py migrate
```
- Now you can start the project and enjoy by running the following command.
```
python manage.py runserver
```

- Happy Coding.

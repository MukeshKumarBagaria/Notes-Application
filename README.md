# Notes App - 

This project is a simple Notes App implemented using Django REST Framework. It provides basic CRUD (Create, Read, Update, Delete) functionality for managing notes through a RESTful API.

## Dependencies

- Django
- Django REST Framework
- Django Core Headers

## Setup

1. **Clone the Repository:**

    ```bash
   git clone https://github.com/MukeshKumarBagaria/Notes-Application.git
    ```

2. **Install Dependencies:**

    ```bash
     pip install django djangorestframework django-cors-headers
    ```

3. **Run Migrations:**

    ```bash
   python manage.py makemigrations                                           ─╯
   python manage.py migrate
    ```

4. **Create Superuser (Optional):**

Existing super user cred.
```
username:mukesh
password:123456
```
or you can create a new super user with this command
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Admin Panel (Optional):**

    Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to log in with the superuser credentials and manage notes from the Django admin.

## API Endpoints

1. **Get All Notes:**
    - Endpoint: [http://127.0.0.1:8000/api/notes/](http://127.0.0.1:8000/api/notes/)
    - Method: GET

2. **Get Note Details:**
    - Endpoint: [http://127.0.0.1:8000/api/notes/1/](http://127.0.0.1:8000/api/notes/1/)
    - Method: GET
    - Replace `1` with the ID of the desired note.

3. **Update Note:**
    - Endpoint: [http://127.0.0.1:8000/api/notes/1/update/](http://127.0.0.1:8000/api/notes/1/update/)
    - Method: PUT
    - Replace `1` with the ID of the note to update.
    - Include the updated data in the request body.

4. **Delete Note:**
    - Endpoint: [http://127.0.0.1:8000/api/notes/1/delete/](http://127.0.0.1:8000/api/notes/1/delete/)
    - Method: DELETE
    - Replace `1` with the ID of the note to delete.

## Auth 
Basic auth is implemented using inbuilt libraries so to use any endpoint as a user you will require user cred. either if you are an admin you can create one for yourself or ask the admin of the project for one, currently, signup is not implemented.
or simply you can use the below-given cred. for testing-
```
username:mukesh
password:123456
```

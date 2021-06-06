# Shop HD App
A simple product CRUD structure in Python Django Framework with Follow user feature and Product Recommendations on views by following users

Users can demo it here http://wasimtamboli.pythonanywhere.com/


Project Details
--------------------------------------------
- Backend - Python/Django
- Database - SQLite3
- Hosted on - pythonanywhere
- website - http://wasimtamboli.pythonanywhere.com/


Setup Project
--------------------------------------------
1. Create a virtual environmnet and activate
```
$ virtualenv venv
$ source venv/bin/activate
```
2. Clone Project from https://github.com/wasi-m/shop-hd.git
```
$ git clone https://github.com/wasi-m/shop-hd.git
```
3. Install all project dependency from requirements.txt file
```
$ pip install -r requirements.txt
```
4. Go to project folder and run the Django makemigrations and migrate
```
$ python manage.py makemigrations
$ python manage.py migrate
```
5. To populate dummy data run following
```
$ python manage.py seed_user
$ python manage.py seed_followers
$ python manage.py seed_product
```
6. Go to project folder and run Django development server
```
$ python manage.py runserver
```
7. Open http://127.0.0.1:8000 in browser

**NOTE\*\* All Default loaded users will have _password_ as default password and will be non supersuer, to perform CRUD operation on product need to register new user with admin rights**

To Demo Product Recommendation
--------------------------------------------
1. Login with username as _Krzysztof Gould_ and password as _password_
2. Click on _Product Recommendation_ situated on top right corner
3. Top 10 Product Recommendations are shown

App Structure
--------------------------------------------
- accounts module to handle user signin/signup
- products module to handle product CRUD operations
- templates store html layout files

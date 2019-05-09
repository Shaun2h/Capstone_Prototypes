## Prototypes for Capstone. 
### Django Prototype
Python 3.7++
```
python -m pip install Django
```

### Django Prototype
Completed, Has an SQL database with in built models.<br>
To start:<br>
```
python manage.py runserver
```
`http:127.0.0.1:8000` or `http:/localhost:8000/`<br>
Admin is currently enabled on the server as it is a prototype.<br>
`http:127.0.0.1:8000/` brings you to the various templates available.<br>
`http:127.0.0.1:8000/models` brings you to the models pages. These  are loaded from iframes in the actual pages to allow a visible model.<br>
For simplicity, Admin username is user, password is password. This needs to be changed.<br>
From: https://stackoverflow.com/questions/6358030/how-to-reset-django-admin-password
> You may try through console: <br>
> python manage.py shell <br>
> then use following script in shell <br>
> from django.contrib.auth.models import User <br>
> User.objects.filter(is_superuser=True) <br>
> will list you all super users on the system. if you recognize yur username from the list: <br>
> usr = User.objects.get(username='your username') <br>
> usr.set_password('raw password') <br>
> usr.save() <br>
> and you set a new password (:

* Database
Database structure can be viewed in /admin.<br>
Database insertion needs to support file input and structure creation too. (Under first TODO.)<br>
For more details on the structure, look into models.py<br>

#### TODO:
* some file upload system and entry that is properly made would be nice.<br>
* HTML and CSS updates to make it look more presentable. Bootstrap?<br>
* Video Hosting availability? <br>
* Enable separate CDN on django for the relevant html. <br>



### NodeJS Prototype
* Current ExpressJS, Serves up static html page for simplicity
* Will not be using pug or other frontend engines.
* Database has yet to be finalised.


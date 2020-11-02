# RealEstate User microservice


The goal of this project is to create a user microservice for a real estate management web application. This microservice allows a user to fulfill real estates and consult other estates available on the platform. 

# Features

  - A user can add / modify a real estate.
  - Users can enter / edit their personal information on the platform.
  - Users can view estates by city.
  - An owner can only modify the characteristics of his real estate without having access to the edition of the other estates.

#### Sprint 1
During the first sprint I designed and developed these features : 
  - Users can add their personal information on the platform.
  - Users can edit their informations.

#### Sprint 2
Concerning this sprint I designed and developed these features : 
  - Users can add real estates.
  - Users can edit their real estates.
  - Users can add rooms to their real estates.
  - Users can edit rooms of their real estates.

# Installation & Usage

After downloading the project make sure you have installed all the requirements tools below:

* [Python - 3.7.4] - Python is an interpreted, cross-platform programming language and object-oriented.
* [Flask - 1.1.2] - Flask is an open-source micro framework for web development in Python.
* [Flask-RESTful - 0.3.8] - Flask-RESTful is an extension for Flask that adds support for quickly building REST APIs.
* [SQLAlchemy - 1.3.20] - SQLAlchemy is an open source SQL toolkit and object-relational mapping written in Python.
* [Flask-SQLAlchemy - 2.4.4] - Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application.
* [Flask-swagger-ui - 3.36.0] - Swagger is an interface description language for describing RESTful APIs expressed using JSON.

Install the dependencies and devDependencies and start the server.

```sh
$ pip install -r requirement.txt
```

You can also check requirement.txt file in order to install other requirement.

You can now run the server using this command line : 
```sh
$ python -m flask run
```
Please note that server by default is running on port 5000. you can change the port in the app.py file.

   [Flask - 1.1.2]: <https://flask.palletsprojects.com/en/1.1.x/>
   [Python - 3.7.4]: <https://www.python.org/>
   [Flask-RESTful - 0.3.8]: <https://flask-restful.readthedocs.io/en/latest/>
   [SQLAlchemy - 1.3.20]: <https://www.sqlalchemy.org/>
   [Flask-SQLAlchemy - 2.4.4]: <https://flask-sqlalchemy.palletsprojects.com/en/2.x/>
   [Flask-swagger-ui - 3.36.0]: <https://swagger.io/>
 
### API

This section contains general API description of REST API. You can find all the details in the swagger.

| API | description |
| ------ | ------ |
| /users | Add user |
| /users/{id_user} | Edit user information |
| /users/{id_user}/estates | Add estate |
| /users/{id_user}/estates/{id_estate} | Edit estate of current owner |
| /estates/{city} | Get estates by city |
| /users/{id_user}/estates/{id_estate}/rooms | Add room for an estate |
| /users/{id_user}/estates/{id_estate}/rooms/{id_room} | Edit room of an estate |

### Workspace

This is the tools I used during the development of this microservice :

| Workspace & Tools | Link |
| ------ | ------ |
| PyCharm | [https://www.jetbrains.com/fr-fr/pycharm/][PlDb] |
| Postman | [https://www.postman.com/][PlGh] |
| git | [https://git-scm.com/][PlGd] |

### Conclusion

If you find a bug don't hesitate to contact me or fix it.
Want to contribute ? Great ! Please fork this project and add great features. Finally, don't forget to make a pull request :)

In order to improve this version of the project we can separate this microservice into two microservices: User and Estate.
We can also add an authentication system using jwt.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

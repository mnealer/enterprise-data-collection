# enterprise-data-collection

A while ago, I created a function in a larger app to send forms out to all branches in a business so the
branches could fill in risk assessment data required for insurance. This showed a need to have a set of forms
that will be linked to a given person or entity, but the form would not be sent out fresh each time, but a 
request for updates if required for the form. the Central administration also needed to see who had or hadn't 
updated the required forms.

There was a recent request on Upworks for a project of this nature, so I decided it would be a good project to
use as an example. 

I was going to use Django for this, but recent work on FastAPI has left me a little cold on the framework
so I have decided to build this using the following libraries

* FastAPI
* Tortoise-ORM
* Asyncpg
* Mako
* Python-dotenv
* Bulma
* Brython


## Why these Libraries

### FastAPI

Fully Async, supports background tasks out of the box. Uses Pydantic for Data validation instead of forms.

### Tortoise-ORM

Somewhat similar to Django's ORM, but not much. Much simpler implementation than SQLAlchemy. Fully Async.

### Asyncpg

Postgresql Async driver

### Mako

A test for this project. Mako allows for more Python code in the templates and other features. I want to compare
its use to how I would have coded with Django's templaing or Jinija2

### Python DotEnv

Do you really have to ask!!!

### Bulma

I like this CSS library. Makes the UI builds easy

### Brython

Half Python, half Javascript. It just makes the FE coding easier for a python programmer.


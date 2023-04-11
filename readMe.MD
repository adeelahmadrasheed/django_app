# Django Project Documentation
## create a new repository on the command line
<ul><li> 
git init
</li><li> 
git add README.md
</li><li> 
git commit -m "first commit"
</li><li>
git branch -M master
</li><li> 
git remote add origin https://github.com/adeelahmadrasheed/django_app.git 
</li><li> 
git push -u origin master
</li></ul>

## or push an existing repository from the command line
<ul><li> 
git remote add origin https://github.com/adeelahmadrasheed/django_app.git
</li><li>
git branch -M master
</li><li>
git push -u origin master
</li></ul>


### Django Commands List
python -m django
### create new app
python -m django startproject .#create in same folder
### generate requirements file
pip freeze > requirements.txt 
### Initialize requirement.txt file
pip install -r requirements.txt
### Creating new databse model
python manage.py startapp articles
### Run migrations
python manage.py migrate #create sqlite.db
### Make migrations
python manage.py makemigrations
### Include your module/app inside settings.py
add new app under INSTALLED_APPS section in settings.py file 
### Creating super user for admin
python manage.py createsuperuser
### Data class module for django shell
pip install dataclasses
#### Usage
from dataclasses import dataclass
> @dataclass
... class BlogPost:
...     title: str
...     content: str
obj = BlogPost(title="Blogpost Title", content="Blogpost Content")
obj.title
'Blogpost Title'
obj.content
'Blogpost Content'
obj.save


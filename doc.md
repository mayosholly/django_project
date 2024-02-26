Django rest framework

1. You would need to create a virtual environment

python -m venv myVirtualEnvironment 


after creating the virtual environment, you need to activate it with the activate script

like myVirtualEnvironment/Script/activate


2. Install django using pip install django
   now django is in the virtual environment

3. create a requirement file using pip freeze > requirements.txt
4. django-admin startproject simpleblog .
5. py manage.py 
6. py manage.py runserver -  this helps to run your server
7. install django rest framework, pip install djangorestframework

use pip list to check the list of installed packages

8. py manage.py startapp posts -  this create a new app called posts

file structure
    migration used for keep track of migration files
    models - where we define our database table structures and others

    the view function like the controller. it takes in http response.

9. setup structute 
    write a function or method in the views.py using the http request
    call the function from the urls using the url paths
    then link it to the admin

    you can use the pip install black for formatting the 
    
    test view.py
    from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def homepage(request:HttpResponse):
    response = {"message" : "Hello world"}
    return JsonResponse(data=response)


10. serializers - it allows you to turn data base models into JSON data
11. migration - python manage.py makemigration
    migration - python manage.py makemigration

    

12. to load the python shell configuration for importing data use py manage.py shell

>>> from posts.serializers import PostSerializer
>>> from posts.models import Post
>>> new_post1 = Post( 
... title="React",
... content="This is a video for React")
>>> new_post1.save()
>>> new_post2=Post( 
... title="Vue",
... content="This is vue"   
... )
>>> new_post2.save()
>>> serializer=PostSerializer(instance=new_post)
>>> serializer
>>> Post.objects.all()
>>> json_data=JSONRenderer().render(serializer.data)
>>> json_data
b'{"id":3,"title":"Learn DRF","content":"Basic of DRF","created":"2024-02-23T10:06:27.177399Z"}'

here is an example of a normal serializer 
from rest_framework import serializers

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created = serializers.DateTimeField(read_only=True)

13. create a new post file and call it serializer. import serializer from django rest framework
how to use serializer to convert models to json object

we have various methods

1. function 
2. class 
3. generic  mixin
4. model view set
5. class view set

pip install djangorestframework-simplejwt
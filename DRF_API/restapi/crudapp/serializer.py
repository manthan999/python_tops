from rest_framework import serializers
from crudapp.models import *

class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
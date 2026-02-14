from rest_framework import serializers
from crudapp.models import *

class Countryserializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['country'] = Authorserializer(instance.country).data
        return resp
class Authorserializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        depth=1

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):

        if attrs['qty']<10:
            raise serializers.ValidationError("qty must be above or equal 10")
        return attrs
        
    def to_representation(self, instance):
        resp = super().to_representation(instance)
        resp['author'] = Authorserializer(instance.author).data
        return resp

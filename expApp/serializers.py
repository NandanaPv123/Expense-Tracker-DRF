from rest_framework import serializers
from expApp.models import ExpenseModel
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=["username","email","password"]
    
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExpenseModel
        fields="__all__"
        read_only_fields=['id','created_at','owner']




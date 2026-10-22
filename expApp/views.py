from django.shortcuts import render
from expApp.serializers import ExpenseSerializer,UserSerializer
from expApp.models import ExpenseModel
from rest_framework.response import Response
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.


class UserCreateView(CreateAPIView):
    serializer_class=UserSerializer
    def perform_create(self,serializer):
        return User.objects.create_user(**serializer.validated_data)

class ExpenseCreateListView(CreateAPIView,ListAPIView):   
    serializer_class=ExpenseSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.BasicAuthentication] 
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filterset_fields=['category','payment']
    search_fields=['title']
    ordering_fields=['amount','created_at']    

    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return ExpenseModel.objects.filter(owner=self.request.user)    

class ExpenseRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=ExpenseSerializer
    permission_classes=[permissions.IsAuthenticated]
    authentication_classes=[authentication.BasicAuthentication]
    queryset=ExpenseModel.objects.all()
    lookup_url_kwarg="id"

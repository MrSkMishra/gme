from django.shortcuts import render
from .serializers import RegistrationSerializer
from rest_framework import generics
import uuid
from rest_framework  import permissions,status
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import PalindromeGamez
from .serializers import PalindromeSerializer


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer
    queryset =  PalindromeGamez.objects.all()

    def post(self,request):
        serializer = self.get_serializer(data = request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestID":str(uuid.uuid4()),
                "Message":"User Created Successfully",
                "User":serializer.data},status=status.HTTP_201_CREATED)
        return Response({"Errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
class PalindromeGameListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PalindromeGamez.objects.all()
    serializer_class = PalindromeSerializer

class PalindromeGameRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = PalindromeGamez.objects.all()
    serializer_class = PalindromeSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from quote.models import Quote
from quote.serializers import QuoteSerializer

# Create your views here.

class QuoteAPIView(APIView):

    def get(self,request,*args,**kwargs):
        quo_objs = Quote.objects.all()
        quo_ser_obj = QuoteSerializer(quo_objs,many=True)
        return Response(quo_ser_obj.data)

    def post(self,request,*args,**kwargs):
        quo_ser_obj = QuoteSerializer(data = request.data)
        if quo_ser_obj.is_valid():
            quo_ser_obj.save()
            return Response(quo_ser_obj.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(quo_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteUpdateAPIView(APIView):
    def put(self,request,id,*args,**kwargs):
        quo_obj = Quote.objects.get(id=id)
        quo_ser_obj = QuoteSerializer(instance = quo_obj,data = request.data, partial=True)
        if quo_ser_obj.is_valid():
            updated_obj = quo_ser_obj.save()
            obj = QuoteSerializer(updated_obj)
            return Response(obj.data)
        else:
            return Response(quo_ser_obj.errors, status=status.HTTP_400_BAD_REQUEST)


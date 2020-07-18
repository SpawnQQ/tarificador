from .tarifas.r_environment import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_400_BAD_REQUEST,
	HTTP_401_UNAUTHORIZED,
	HTTP_404_NOT_FOUND,
	HTTP_426_UPGRADE_REQUIRED,
)

# Create your views here.

class Tarificador(APIView):

	permission_classes = (AllowAny,)

	def post(self, request):

		form = request.data 

		input_form = self.pre_proceso(form)

		result = self.post_proceso(input_form)
		print(asd)

		return Response(result, status=HTTP_200_OK)

	def pre_proceso(self, form):

		column_names = form['ColumnNames']
		values = form['Values']
		column_types = form['ColumnTypes']

		input_form = {
			'a': column_names,
			'b': values,
			'c': column_types,
		}

		return input_form

	def post_proceso(self, input_form):

		result = input_form
		
		return result
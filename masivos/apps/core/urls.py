from .views import (
	Tarificador
)
from django.urls import path


urlpatterns = [

	path(
		'api/', 	
		Tarificador.as_view(),
		name='api',
	),

]
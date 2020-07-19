from .views import (
	Tarificador
)
from django.urls import path


urlpatterns = [

	path(
		'', 	
		Tarificador.as_view(),
		name='api',
	),

]

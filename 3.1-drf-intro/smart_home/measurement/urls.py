from django.urls import path

from .views import SensorsView, SensorDetailView, MeasurementAdd

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementAdd.as_view()),
]

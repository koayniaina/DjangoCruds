from django.urls import path
from .import views

urlpatterns = [
    path('', views.show , name='shows' ),
    path('add/', views.studentAdd , name='add' ),
    path('update/<int:id>' , views.update , name="update"),
    path('delete/<int:id>' , views.delete , name="delete")
]




from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import viewIndex, viewCatalog, viewCar, viewAdmin, viewCreateCar, viewDeleteCar, viewUpdateCar

urlpatterns = [
    path("admin/", viewAdmin, name="admin"),
    path("", viewIndex, name="index"),

    #Create
     path('catalog/criar/', viewCreateCar, name='create' ),
    
    #Read
      path("catalog/", viewCatalog, name='catalog'),
      path("catalog/detail/<int:id>/", viewCar, name='detail'),
    
    #Update
      path("catalog/detail/update/<int:id>/", viewUpdateCar, name="update"),

    #Delete
     path("catalog/detail/delete/<int:id>/", viewDeleteCar, name = "delete"),
    
   
   

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

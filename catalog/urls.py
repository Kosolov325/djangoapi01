from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path("admin/", viewAdmin, name="admin"),
    path("", viewIndex, name="index"),

    #Create
      path('catalog/criar/', viewCreateCar, name='create' ),

      path('marcas/criar/', viewCreateMarca, name = 'createMarca'),

    #Read
      path("catalog/", viewCatalog, name='catalog'),
      path("catalog/detail/<int:id>/", viewCar, name='detail'),

      path("marcas/", view_Marcas, name='marcas'),
      path("marcas/detail/<int:id>/", viewMarca, name="detailMarca" ),
  
    #Update
      path("catalog/detail/update/<int:id>/", viewUpdateCar, name="update"),

      path("marcas/detail/update/<int:id>/", viewUpdateMarca, name="updateMarca"),

    #Delete
      path("catalog/detail/delete/<int:id>/", viewDeleteCar, name = "delete"),

      path("marca/detail/delete/<int:id>/", viewDeleteMarca, name = "deleteMarca"),
    
   
   

   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

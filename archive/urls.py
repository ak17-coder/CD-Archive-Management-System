from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-cd/', views.add_cd, name='add_cd'),
    path('view-cd/', views.view_cd, name='view_cd'),
    path("edit-cd/<int:id>/", views.edit_cd, name="edit_cd"),
    path("delete-cd/<int:id>/", views.delete_cd, name="delete_cd"),
    path("logout/", views.logout_view, name="logout"),
    path("import-excel/", views.import_excel, name="import_excel"),
    path("export-excel/", views.export_excel, name="export_excel"),
    path("open-folder/<int:id>/", views.open_folder, name="open_folder"),
    path("view-details/<int:id>/", views.view_details, name="view_details"),
    path("categories/", views.categories, name="categories"),
    
]
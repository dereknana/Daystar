from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    # path("auth/", views.auth),
    path('home/',  views.home, name='home'),

#-------------------------------------------
    path('view_baby/<int:baby_id>/', views.view_baby, name='view_baby'),
    path('edit_baby/<int:baby_id>/', views.edit_baby, name='edit_baby'),
    path('view_babies/', views.view_babies, name='view_babies'),
    # path('edit_baby/<int:baby_id>/', views.edit_baby, name='edit_baby'),

# ----------------------------------------------------------------
    path('view_sitters/', views.view_sitters, name='view_sitters'),
    path('add_baby/', views.add_baby, name='add_baby'),
    path('add_sitter/', views.add_sitter, name='add_sitter'),
    path('sitter/<int:sitter_id>/delete/', views.delete_sitter, name='delete_sitter'),
    path('baby/<int:baby_id>/delete/', views.delete_baby, name='delete_baby'),
    path('redirect_to_dashboard/', views.redirect_to_dashboard, name='redirect_to_dashboard'),
    path('procurement/', views.procurement, name='procurement'),
]



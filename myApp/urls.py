from django.contrib import admin
from django.urls import path
from . import views  # Import views from the current app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('library/', views.library, name='library'),
    path('books/', views.books, name='books'),


    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('admin_login/', views.admin_login, name='admin_login'),

    path('logout/', views.user_logout, name='logout'),
    
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # path('create_exam/', views.create_exam, name='create_exam'),
    # path('select_exam/', views.select_exam, name='select_exam'),  # Experienced students can select exams
    # path('take_exam/<int:exam_id>/', views.take_exam, name='take_exam'),
    # path('view_results/<int:submission_id>/', views.view_results, name='view_results'),

    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

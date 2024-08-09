from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('greeting', views.greeting, name="greet"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('services/', views.service, name="service"),
    path('blog/', views.handleblog, name="blog"),
    path('blog_details/<int:pk>', views.blog_details, name="blog-details"),
    path('internshipdetails/', views.internshipdetails, name="internshipdetails"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('portfolio_cat/<str:foo>', views.portfolio_cat, name="portfolio_cat"),
    path('portfolio-details/<int:pk>', views.portfolio_details, name="portfolio-details"),
]
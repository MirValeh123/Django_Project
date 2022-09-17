from django.urls import path
from .views import delete,  editProfile, loginUser, logoutUser, register, home, about, portfolio, whatwedo, project_details, blog, blog_details, contact, addwork, mywork, update

urlpatterns = [


    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
    path('about', about, name='about'),
    path('addwork', addwork, name='addwork'),
    path('mywork', mywork, name='mywork'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('portfolio/', portfolio, name='portfolio'),
    path('whatwedo', whatwedo, name='whatwedo'),
    path('project_details/<int:id>', project_details, name='project_details'),
    path('blog', blog, name='blog'),
    path('blog_details', blog_details, name='blog_details'),
    path('contact', contact, name='contact'),
    path('edit', editProfile, name='edit'),







]

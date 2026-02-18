from django.urls import path
from doctorApp.views import *

urlpatterns = [
    path('', indexPage, name="index"),
    path('doctor-info', doctorInfoPage, name="doctor-info"),
    path('doctor-form', doctorFormPage, name="doctor-form"),
    path('register', registerPage, name="register"),
    path('login', loginPage, name="login"),

    path('add-doctor', addDoctor, name="add-doctor"),
    path('edit-redirect', editRedirect, name="edit-redirect"),
    path('update-doctor', updateDoctor, name="update-doctor"),
    path('delete-doctor', deleteDoctor, name="delete-doctor"),

    path('register-user', registerUser,),
    path('login-user', loginUser),
    path('logout-user', logoutUser, name="logout-user"),
]

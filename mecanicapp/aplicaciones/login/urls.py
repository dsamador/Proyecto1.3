from django.urls import path

from aplicaciones.login.views import *
from .views import *

urlpatterns = [
    path('login/', LoginFormView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(),   name = 'logout'),
    path('signup/', SingUpView.as_view(),   name = 'signup'),
    path('perfil/', PerfilView.as_view(),   name = 'perfil'),
    path('perfil/email/', EmailUpdate.as_view(), name="email"),
]
"""userapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from user.views.v1.register_user import register_user
from user.views.v1.check_username import check_username
from user.views.v1.get_user import get_user_info
from user.views.v1.change_avatar import change_avatar
from user.views.v1.update_user import update_user

urlpatterns = [
    path('register/', register_user),
    path('check-username/', check_username),
    path('info/', get_user_info),
    path('change-avatar/', change_avatar),
    path('update-user/', update_user),
]

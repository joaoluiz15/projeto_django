"""
URL configuration for bibliotecalocal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


# definição do caminho para o módulo catalog.urls
from django.conf.urls import include
from django.urls import path

urlpatterns += [
    path('catalogo/', include('catalogo.urls')),
]

# redireciona a página inicial para '/catalogo/'
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalogo/')),
]

# permite o uso de arquivos estáticos (CSS, JavaScript, etc)
# no servidor de desenvolvimento
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
from django.urls import path, include
from .views import CreateApplicationForPrinter, thanks_page

urlpatterns = [
    path('', CreateApplicationForPrinter.as_view(), name='index'),
    path('thanks-page/', thanks_page, name='thanks_page'),
    path('captcha/', include("captcha.urls")),
]


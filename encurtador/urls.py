from django.conf.urls import url
from .views import IndexView, Encurtar, LinkView
from .models import Url

urlpatterns = [
    url(r'^encurtar$', Encurtar.as_view(), name='encurtar' ),
    url(r'^index$', IndexView.as_view(model=Url, success_url='/encurtador/encurtar')),
    url(r'(?P<code>.*)^$', LinkView.as_view())
]

# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from .api import RequisicaoResource
from tastypie.api import Api

v1_api = Api(api_name="v1")
v1_api.register(RequisicaoResource())

urlpatterns = [
    url(r'^api/', include(v1_api.urls)),
]
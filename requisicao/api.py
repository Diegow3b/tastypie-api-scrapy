from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash
from tastypie.exceptions import BadRequest
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django.conf.urls import url, include
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from .models import Requisicao
import json
import hashlib

class RequisicaoResource(ModelResource):

    class Meta:
        queryset = Requisicao.objects.all()
        resource_name = "requisicao"
        authorization = Authorization()
        authentication = Authentication()
        allowed_methods = ['get','post']
        filtering = {"key": ALL_WITH_RELATIONS, "url": ALL_WITH_RELATIONS }
        always_return_data = True
        limit = 1

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/crawler%s$" % \
                (self._meta.resource_name, trailing_slash()), \
                self.wrap_view('crawler'), name="api_crawler"),
        ]

    def crawler(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        # self.is_authenticated(request)
        self.throttle_check(request)
        payload = json.loads(request.body)
        # print '\n\n\n\n\n\n-------------------------------------------------'
        # print payload.get('json'
        # print '-------------------------------------------------\n\n\n\n\n\n'
        try:
            if 'key' in payload and 'url' in payload:
                Requisicao.call_spider(payload.get('key'), payload.get('url'),\
                                       payload.get('json') if payload.get('json') else None)
                return self.create_response(request, {'Enviado'}, status=200)
        except ValidationError as e:
            raise BadRequest(repr(e))
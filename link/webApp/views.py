from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from random import randint
import re

from webApp.forms import LinkForm
from webApp.models import LinkModel,NameModel


# Create your views here.
class Index(View):
    html = 'index.html'

    def get(self, request, *args, **kwargs):
            form = LinkForm()
            list_link = LinkModel.objects.all().order_by("id").reverse()[:5]
            return render(request, self.html, locals())

    def post(self,request,*args):
        form = LinkForm(request.POST)
        error = ""
        if form.is_valid():
            print("valid !")
            link_data = form.cleaned_data['link'].strip()
            p = re.compile('http(s)?:\/\/*')
            if p.match(link_data):
                try:
                    print("roro")
                    link_bdd = self.generate_url(link_data)
                except KeyError:
                    error = "The link has not been created, try again"
            else:
                error = "not a valid url"
            
        list_link = LinkModel.objects.all()
        return render(request, self.html, locals())

    def get_name(self):
        a = NameModel.objects.all().count()
        return NameModel.objects.all()[randint(0,a-1)].name

    def generate_url(self,url):
        print("titi")
        for i in range(50):
            print("toto")
            name = self.get_name().strip()
            obj, created = LinkModel.objects.get_or_create(key=name,link=url)
            print(obj)
            if created:
                return obj
        
        raise KeyError

class Url_load(View):
    def get(self, request,name, *args, **kwargs):
        res = LinkModel.objects.get(key=name)
        return HttpResponseRedirect(res.link)


class Delete(View):
    html = 'index.html'

    """
        return index page if not authentificated else home account page
    """
    def get(self, request, *args, **kwargs):
            key = kwargs.get("key")
            try:
                link = LinkModel.objects.get(pk=key)
                link.delete()
                
            except:
                error = "not a valid ID"
            form = LinkForm()
            list_link = LinkModel.objects.all()
            return render(request, self.html, locals())
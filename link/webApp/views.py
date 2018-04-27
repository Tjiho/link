from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webApp.forms import LinkForm
from webApp.models import LinkModel
import re
# Create your views here.
class Index(View):
    html = 'index.html'

    def get(self, request, *args, **kwargs):
            form = LinkForm()
            list_link = LinkModel.objects.all()
            return render(request, self.html, locals())

    def post(self,request,*args):
        form = LinkForm(request.POST)
        error = ""
        if form.is_valid():
            print("valid !")
            link_data = form.cleaned_data['link']
            p = re.compile('http(s)?:\/\/*')
            if p.match(link_data):
                try:
                    link_bdd = LinkModel.objects.create(link=link_data)
                except:
                    error = "the link already exists"
            else:
                error = "not a valid url"
            
        list_link = LinkModel.objects.all()
        return render(request, self.html, locals())

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
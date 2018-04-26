from django.shortcuts import render
from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from webApp.forms import LinkForm
from webApp.models import LinkModel
# Create your views here.
class Index(View):
    html = 'index.html'

    """
        return index page if not authentificated else home account page
    """
    def get(self, request, *args, **kwargs):
            form = LinkForm()
            list_link = LinkModel.objects.all()
            return render(request, self.html, locals())

    """
        login with arel...
    """
    def post(self,request,*args):
        form = LinkForm(request.POST)
        error = ""
        if form.is_valid():
            print("valid !")
            link_data = form.cleaned_data['link']
            link_bdd = LinkModel.objects.create(link=link_data)
            
        list_link = LinkModel.objects.all()
        return render(request, self.html, locals())
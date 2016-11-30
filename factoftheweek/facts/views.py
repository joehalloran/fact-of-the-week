from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Fact

class HomeView(ListView):
    """ 
    The home page for the entire site.
    """
    template_name = 'facts/home.html'
    context_object_name = 'newest_fact'

    def get_queryset(self):
        """
        Return the last 4 published questions.
        """
        return Fact.objects.filter(
        	pub_date__lte=timezone.now()
    	).order_by('-pub_date')[:4]

class IndexView(ListView):
    """
    The /facts/ root. Lists more recent facts.
    """
    template_name = 'facts/index.html'
    context_object_name = 'latest_facts_list'

    def get_queryset(self):
        """
        Return all published facts.
        """
        return Fact.objects.filter(
        	pub_date__lte=timezone.now()
    	).order_by('-pub_date')

class DetailView(DetailView):
    model = Fact
    template_name = 'facts/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Fact.objects.filter(pub_date__lte=timezone.now())

from django.views.generic.list import ListView
from django.db.models.functions import Cast

from count_app.models import Count
# from count_app.forms import Countermodelform

# Create your views here.


class CountListView(ListView):

    def get_queryset(self):
        self.queryset = Count.objects.all()

        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'counter'

        # context['form'] = Countermodelform()

        return context

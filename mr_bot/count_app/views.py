from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from count_app.models import Count, BotUser
from count_app.forms import BotUserRegisterForm, CounterForm

# Create your views here.
# from count_app.forms import BotUserLoginForm


class CountListView(ListView):

    def get_queryset(self):
        # print(self.request.user)
        if self.request.user.is_authenticated:
            self.queryset = Count.objects.filter(usr=self.request.user)

        else:
            self.queryset = Count.objects.all()

        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'counter'

        return context


class CounterUpdate(UpdateView):
    model = Count
    success_url = reverse_lazy('main:count_list')
    form_class = CounterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'редактирование'

        return context


class CounterDelete(DeleteView):
    model = Count
    success_url = reverse_lazy('main:count_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.count > 0:
            self.object.count -= 1
        else:
            self.object.count = 0
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'удаление'

        return context


class UserRegister(CreateView):
    model = BotUser
    success_url = reverse_lazy('main:count_list')
    form_class = BotUserRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'create'
        return context


class CountLoginView(LoginView):
    model = BotUser
    template_name = 'count_app/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'login'

        return context


class CountLogoutView(LogoutView):

    model = BotUser
    success_url = reverse_lazy('main:count_list')

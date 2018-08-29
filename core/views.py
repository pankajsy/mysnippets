from django.views.generic import TemplateView, CreateView, ListView
from braces.views import LoginRequiredMixin, StaffuserRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy


def feed(request):
        return HttpResponseRedirect(reverse('account:admin_users_list'))
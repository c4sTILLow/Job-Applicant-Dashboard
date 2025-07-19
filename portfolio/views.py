from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Portfolio
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


def applicant_list(request):
    users = User.objects.filter(portfolio__isnull=False)
    return render(request, 'portfolio/applicant_list.html', {'users': users})


from django.views.generic import DetailView

class ApplicantDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/applicant_detail.html'
    context_object_name = 'portfolio'

    def get_object(self, queryset=None):
        user = get_object_or_404(User, username=self.kwargs['username'])
        return get_object_or_404(Portfolio, user=user)

class ApplicantDeleteView(View):
    def post(self, request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return redirect('/')


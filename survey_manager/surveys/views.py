from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import(
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count

from .models import Survey, Question, Choice, Response, Answer
from .forms import SurveyForm, QuestionFormSet

# Create your views here.


class SurveyListView(ListView):
    model = Survey
    template_name = 'survey/survey_list.html'   #fetch the template file under survey_manager
    context_object_name = 'surveys'
    
    def get_queryset(self):
        return Survey.objects.filter(is_active=True)
    
class UserSurveyListView(LoginRequiredMixin, ListView):
    model = Survey
    template_name = 'survey/survey_list.html'
    context_object_name = 'surveys'

    def get_queryset(self):
        return Survey.objects.filter(created_by=self.request.user)


class SurveyDeyailView(DetailView):
    model = Survey
    template_name = 'survey/survey_list.html'
    context_object_name = 'survey'
    
class SurveyCreateView(LoginRequiredMixin, CreateView):
    model = Survey
    form_class = SurveyForm:forms.py
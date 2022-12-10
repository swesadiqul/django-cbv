from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'cbv/index.html'
   
# class ContactView(View):
#     form_class = ContactForm
#     template_name = 'cbv/contact-form.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form':form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')    
#         return render(request, self.template_name, {'form':form})

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = "cbv/contact-create.html"
    success_url = reverse_lazy('contact_list')


class ContactListView(ListView):
    model = Contact
    context_object_name = 'contacts'
    template_name='cbv/contact-list.html'

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ['name', 'phone', 'email', 'subject', 'message']
    template_name = "cbv/contact-update.html"
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(DeleteView):
    model = Contact
    context_object_name = 'task'
    template_name = 'cbv/contact_confirm_delete.html'
    success_url = reverse_lazy('contact_list')




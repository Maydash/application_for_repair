from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import ApplicationForPrinterModelForm
from django.views.generic import CreateView


class CreateApplicationForPrinter(CreateView):
    form_class = ApplicationForPrinterModelForm
    template_name = 'repair/index.html'
    success_url = reverse_lazy('thanks_page')


def thanks_page(request):
    return render(request, 'repair/thanks_page.html')



# def add_application(request):
#     if request.method == 'GET':
#         form = ApplicationForPrinterModelForm()
#         return render(request, 'repair/index.html', locals())
#     elif request.method == 'POST':
#         title = request.POST['title']
#         price = Decimal(request.POST['price'])
#         quantity = request.POST['quantity']
#         description = request.POST['description']
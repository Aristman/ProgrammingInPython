from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from .forms import Form1


class Form1View(LoginRequiredMixin, View):
    def get(self, request):
        form1 = Form1()
        return render(request, 'form.html', context={'form': form1})

    def post(self, request):
#        text = request.POST.get('text')
#        number = request.POST.get('number')
#        photo = request.FILES.get('photo')
#        content = photo.read()
        form = Form1(request.POST)
        if form.is_valid():
            context = form.cleaned_data
#            context = {
#                'text': text,
#                'number': number,
#                'photo': content
#            }
            return render(request, 'form.html', context=context)
        else:
            return render(request, 'error.html', context={'error': form.errors})

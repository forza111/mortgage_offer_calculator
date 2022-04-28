import coreapi
from django.views.generic.edit import FormView
from django.shortcuts import render

from .forms import CalculatorForm


class CalculatorView(FormView):
    template_name = 'index.html'
    form_class = CalculatorForm
    success_url = '/main'

    def form_valid(self, form):
        # print(f"A___________{form.cleaned_data['term']}")

        # return super().form_valid(form)
        print(self.get_success_url())
        data = get_mortage_offer(self.request)
        print(type(data[0]))
        return render(self.request, self.template_name)

def get_mortage_offer(request):
    client = coreapi.Client()
    data = client.get('http://127.0.0.1:8000/v1/api/offer/')
    return data

from django.views.generic.edit import FormView
from .forms import CalculatorForm
from services import get_offers


class CalculatorView(FormView):
    template_name = 'index.html'
    form_class = CalculatorForm
    success_url = "main"

    def form_valid(self, form):
        price = form.data["real_estate_price"]
        deposit = form.data["an_initial_fee"]
        term = form.data["term"]
        data = get_offers(price, deposit, term)
        return self.render_to_response(self.get_context_data(data=data))

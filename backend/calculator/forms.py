from django import forms

class CalculatorForm(forms.Form):
    real_estate_price = forms.IntegerField(label="Стоимость недвижимости", min_value=10000, max_value=1000000000)
    an_initial_fee = forms.IntegerField(label="Первоначальный взнос", min_value=10000, max_value=1000000000)
    term = forms.IntegerField(label="Срок", min_value=1, max_value=80, label_suffix="")

    def clean(self):
        cleaned_data = self.cleaned_data
        real_estate_price = cleaned_data.get("real_estate_price")
        an_initial_fee = cleaned_data.get("an_initial_fee")
        if real_estate_price < an_initial_fee:
            raise forms.ValidationError("Первоначальный взнос не может быть выше стоимоси недвижимости")
        return cleaned_data
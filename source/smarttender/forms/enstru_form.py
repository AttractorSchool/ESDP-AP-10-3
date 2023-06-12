from django import forms

from smarttender.models import EnsTruCode


class EnsTruForm(forms.ModelForm):
    class Meta:
        model = EnsTruCode
        fields = ('code', 'name')

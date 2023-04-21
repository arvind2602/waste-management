from django.forms import ModelForm
from .models import detail

class userform(ModelForm):
    class Meta:
        model=detail
        fields='__all__'
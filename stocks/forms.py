from .models import UserStock
from django.forms import ModelForm

class UserStockForm(ModelForm):
    class Meta:
        model = UserStock
        fields = '__all__'


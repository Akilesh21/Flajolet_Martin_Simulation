from django import forms
from .models import Feedback
class DataStreamForm(forms.Form):
    data_stream = forms.IntegerField(label='Data Stream')
    hash_function = forms.IntegerField(label='Hash Function')
    new_data_stream = forms.IntegerField(label='New Data Stream')
    tail_length = forms.IntegerField(label='Tail Length')
    distinct_elements = forms.IntegerField(label='No of Distinct Elements')

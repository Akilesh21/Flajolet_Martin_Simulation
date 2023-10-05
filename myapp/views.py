from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataStreamForm

# Create your views here.
def index(request):
    return render(request,"index.html")
def simulation(request):
    if request.method == 'POST':
        form = DataStreamForm(request.POST)
        if form.is_valid():
            data_stream = form.cleaned_data['data_stream']
            hash_function = form.cleaned_data['hash_function']
            new_data_stream = form.cleaned_data['new_data_stream']
            tail_length = form.cleaned_data['tail_length']
            distinct_elements = form.cleaned_data['distinct_elements']
            # Perform the necessary calculations or logic here
            # You can update the 'results' variable with your calculated values
            results = f"Data Stream: {data_stream}, Hash Function: {hash_function}, New Data Stream: {new_data_stream}, Tail Length: {tail_length}, No of Distinct Elements: {distinct_elements}"
    else:
        form = DataStreamForm()
        results = None

    return render(request, 'simulation.html', {'form': form, 'results': results})


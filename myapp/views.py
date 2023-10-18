from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import DataStreamForm
from .models import Feedback

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
def save_feedback(request):
    if request.method == 'POST':
        feedback_text = request.POST.get('feedback')  # Get feedback data from the request
        if feedback_text:
            Feedback.objects.create(text=feedback_text)  # Create a Feedback model instance
            return JsonResponse({'message': 'Feedback submitted successfully'})
        else:
            return JsonResponse({'message': 'Feedback is empty'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
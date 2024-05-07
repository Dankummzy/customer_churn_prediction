# churn_pred/views.py

from django.shortcuts import render
from joblib import load
from .forms import PredictionForm
from .models import ChurnPredictionResult
from django.views.generic import TemplateView


# Load the Decision Tree Classifier model
dt_model = load('C:/Users/Dell/Desktop/Software/john/churn_prediction/model/decision_tree_model.joblib')

def predict_churn(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            # Extract features from the form
            is_tv_subscriber = form.cleaned_data['is_tv_subscriber']
            is_movie_package_subscriber = form.cleaned_data['is_movie_package_subscriber']
            subscription_age = form.cleaned_data['subscription_age']
            bill_avg = form.cleaned_data['bill_avg']
            remaining_contract = form.cleaned_data['remaining_contract']  # Corrected field name
            service_failure_count = form.cleaned_data['service_failure_count']
            download_avg = form.cleaned_data['download_avg']
            upload_avg = form.cleaned_data['upload_avg']
            download_over_limit = form.cleaned_data['download_over_limit']
            # Create a new ChurnPredictionResult instance with an incremented ID
            try:
                latest_prediction_id = ChurnPredictionResult.objects.latest('id').id
            except ChurnPredictionResult.DoesNotExist:
                latest_prediction_id = None
            next_prediction_id = latest_prediction_id + 1 if latest_prediction_id is not None else 1689745
            # Make prediction using the loaded model
            prediction = dt_model.predict([[next_prediction_id, is_tv_subscriber, is_movie_package_subscriber, subscription_age, bill_avg, remaining_contract, service_failure_count, download_avg, upload_avg, download_over_limit]])
            prediction_result = ChurnPredictionResult(
                id=next_prediction_id,
                is_tv_subscriber=is_tv_subscriber,
                is_movie_package_subscriber=is_movie_package_subscriber,
                subscription_age=subscription_age,
                bill_avg=bill_avg,
                remaining_contract=remaining_contract,
                service_failure_count=service_failure_count,
                download_avg=download_avg,
                upload_avg=upload_avg,
                download_over_limit=download_over_limit,
                predicted_churn=prediction
            )
            # Save the prediction result
            prediction_result.save()
            return render(request, 'churn_pred/result.html', {'prediction': prediction})
    else:
        # Generate a new ID for the form
        try:
            latest_prediction_id = ChurnPredictionResult.objects.latest('id').id
        except ChurnPredictionResult.DoesNotExist:
            latest_prediction_id = None
        next_prediction_id = latest_prediction_id + 1 if latest_prediction_id is not None else 1689745
        initial_data = {'id': next_prediction_id}  # Set the initial data for the form
        form = PredictionForm(initial=initial_data)  # Pass the initial data to the form
    return render(request, 'churn_pred/predict.html', {'form': form})


def list_predictions(request):
    predictions = ChurnPredictionResult.objects.all()
    return render(request, 'churn_pred/prediction_list.html', {'predictions': predictions})


class AboutView(TemplateView):
    template_name = 'churn_pred/about.html'



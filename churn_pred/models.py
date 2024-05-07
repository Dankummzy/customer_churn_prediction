# churn_pred/models.py

from django.db import models

class ChurnPredictionResult(models.Model):
    id = models.AutoField(primary_key=True)  # Add the ID field
    prediction_date = models.DateTimeField(auto_now_add=True)
    is_tv_subscriber = models.IntegerField()
    is_movie_package_subscriber = models.IntegerField()
    subscription_age = models.FloatField()
    bill_avg = models.IntegerField()
    remaining_contract = models.FloatField()
    service_failure_count = models.IntegerField()
    download_avg = models.FloatField()
    upload_avg = models.FloatField()
    download_over_limit = models.IntegerField()
    predicted_churn = models.IntegerField()

    def __str__(self):
        return f'Prediction made on {self.prediction_date} - Churn: {self.predicted_churn}'

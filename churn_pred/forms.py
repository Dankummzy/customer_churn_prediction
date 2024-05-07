# churn_pred/forms.py

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class PredictionForm(forms.Form):
    is_tv_subscriber = forms.IntegerField(label='TV Subscriber', initial=1)
    is_movie_package_subscriber = forms.IntegerField(label='Movie Package Subscriber', initial=0)
    subscription_age = forms.FloatField(label='Subscription Age', initial=0)
    bill_avg = forms.IntegerField(label='Bill Average', initial=25)
    remaining_contract = forms.FloatField(label='Remaining Contract', initial=0.14)
    service_failure_count = forms.IntegerField(label='Service Failure Count', initial=0)
    download_avg = forms.FloatField(label='Download Average', initial=8.4)
    upload_avg = forms.FloatField(label='Upload Average', initial=2.3)
    download_over_limit = forms.IntegerField(label='Download Over Limit', initial=0)

    # Add crispy forms layout
    helper = FormHelper()
    helper.form_method = 'post'
    helper.add_input(Submit('submit', 'Predict', css_class='btn-primary'))
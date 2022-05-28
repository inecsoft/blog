# users/views.py

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CustomUserCreationForm

def dashboard(req):
    return render(req, "users/dashboard.html")

def register(req):
    if req.method == "GET":
        return render(
            req, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif req.method == "POST":
        form = CustomUserCreationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            login(req, user)
            return redirect(reverse("dashboard"))
        
import boto3

# Create an SNS client
client = boto3.client(
    "sns",
    aws_access_key_id="YOUR ACCES KEY",
    aws_secret_access_key="YOUR SECRET KEY",
    region_name="eu-west-1"
)

# Create the topic if it doesn't exist (this is idempotent)
topic = client.create_topic(Name="notifications")
topic_arn = topic['TopicArn']  # get its Amazon Resource Name

# Add SMS Subscribers

client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint={{ email }}  # <-- number who'll receive an SMS message.
)


# Publish a message.
client.publish(Message="Someone asked for password reset for email {{ email }}", TopicArn=topic_arn, Subject="Password Reset")

client.unsubscribe(TopicArn=topic_arn)

client.delete_topic(TopicArn=topic_arn)

def personal_info(request):
    from portfolio.models import PersonalInfo  # Import the model inside the function
    personal_info = PersonalInfo.objects.first()  # Assuming there's only one instance of PersonalInfo
    return {'personal_info': personal_info}

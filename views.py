# Import necessary Django response modules
from django.http import HttpResponse,JsonResponse

# Define a view function to handle the home page request
def home_page(request):
"""
Handles requests to the home page and returns a JSON response.
"""
    # Log a message to indicate the home page was requested
    print("home page requested")

    # List of friends to be returned as a JSON response
    friends = [
        'ankit',
        'ravi',
        "uttam"
    ]

    # Return the list as a JSON response with safe=False (since it's a list, not a dictionary)
    return JsonResponse(friends,safe=False)

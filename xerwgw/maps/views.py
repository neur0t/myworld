from django.shortcuts import render

# Create your views here.
def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.eyJ1IjoibmV1cm90IiwiYSI6ImNsbXpleG5qdjBtdGEyam51aDQ1eXkxcWMifQ.LqEqkPXq98hmCaBG4zZw9Q'
    return render(request, 'default.html', 
                  { 'mapbox_access_token': mapbox_access_token })
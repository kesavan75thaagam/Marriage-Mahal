from MahalApp.models import HomeSlider 

def Home(request):
    try:
        slider=HomeSlider.objects.get(id=1)
    except HomeSlider. DoesNotExist:
        slider = None

    return {
    "Home":slider
    }
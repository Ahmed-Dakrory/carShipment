
from django.http import JsonResponse
from datetime import datetime
from .models import profile
from django.conf import settings  # this is a good example of extra
                                  # context you might need across templates
def default(request):
    # you can declare any variable that you would like and pass 
    # them as a dictionary to be added to each template's context:
    user =request.user
    userProfile = None
    if user.is_authenticated:
        userProfile = profile.objects.get(user = user)
        print("Ok")
    else:
        print("Not Found")
    return dict(
        userdata = user,
        userProfile = userProfile,
        example = "This is an example string.",
        current_date = datetime.now().strftime('%M:%S.%f')[:-4],                
        MEDIA_URL = settings.MEDIA_URL, # just for the sake of example
    )

def returnTimeNow(request):
    data = {
        'current_date': datetime.now().strftime('%M:%S.%f')[:-4]
            }
    return JsonResponse(data)
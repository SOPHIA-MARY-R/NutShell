from django.shortcuts import render, redirect
import uuid
from .models import URL
from django.http import HttpResponse
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method=='POST':
        S=request.POST['link']
        if S!='' and is_string_an_url(S):
            Link=S
            Uuid=str(uuid.uuid4())[:5]
            newURL=URL(link=Link, uuid=Uuid)
            newURL.save()
            return HttpResponse(Uuid)

def go(request, uid):
    urlDetails=URL.objects.get(uuid=uid)
    return redirect(urlDetails.link)

def is_string_an_url(url_string: str) -> bool:
    validate_url = URLValidator()
    try:
        validate_url(url_string)
    except ValidationError:
        return False
    return True
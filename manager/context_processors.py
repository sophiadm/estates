from .models import Property

def propsexist(request):
    if Property.objects.all() or request.user.is_authenticated():
        return {"propsexist":True}
    else:
        return {"propsexist":False}
    

import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    print(request.GET) # url query params
    print(request.POST)
    
    body = request.body
    data = {}
    
    try:
        data = json.loads(body) # String of JSON data -> Python Dictionary
    except:
        pass
    
    # print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
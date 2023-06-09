from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """ DRF API VIEW """
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title'])
        
    return Response(data)
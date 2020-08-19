from rest_framework.response import Response
from rest_framework.views import APIView
from .models import category
from .serializers import categorySerializer

class data(APIView):
    def get(self, request, shop_id):
        shop_id_filter = self.kwargs['shop_id']
        data_list = category.objects.filter(shop_id=shop_id_filter)
        serializer = categorySerializer(instance=data_list,many=True)
        return Response(serializer.data)

    def Post(self):
        pass





from rest_framework import generics
from calc.models.menu.category import Category
from calc.serializers import CategorySerializer
from utils.response_wrapper import api_response

class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return api_response(
            data=serializer.data,
            message=["Category retrieved successfully"],
            status="success",
            remark="category_retrieved"
        )
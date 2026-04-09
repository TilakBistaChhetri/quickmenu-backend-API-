from rest_framework import generics, status
from calc.models.menu.item import Item
from calc.models.menu.category import Category
from calc.serializers import ItemSerializer
from utils.response_wrapper import api_response


class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    # GET Items (optional: filter by category)
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')

        if category_id:
            return Item.objects.filter(categoryId=category_id)

        return Item.objects.all()

    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return api_response(
            data=serializer.data,
            message=["Items fetched successfully"],
            status="success",
            remark="items_fetched",
            http_code=status.HTTP_200_OK
        )

    # POST
    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # 🔥 get category id from URL
        category_id = self.kwargs.get('category_id')

        try:
            category = Category.objects.get(id=category_id)
            data['categoryId'] = category.id
        except Category.DoesNotExist:
            return api_response(
                data=[],
                message=["Invalid categoryId"],
                status="fail",
                remark="not_found",
                http_code=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return api_response(
                data=[serializer.data],
                message=["Item created successfully"],
                status="success",
                remark="item_created",
                http_code=status.HTTP_201_CREATED
            )

        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )
    







    

        # self is Class instance 
        # request is HTTP request data (headers, body, user, etc.)
        #*args is Extra positional arguments (in tuple)
        #**kwargs Extra keyword arguments (in dictionary)
        """
        get_serializer() 
        - Django DRF le dekop predefine function ho.
        - yasale serializers banauxa(serializers means translator between model to json)
        -yasale ItemSerializer ko new instance create garxa.
        - postman baat aako data laai serializer maa rakhna ko laagi use garinxa.
"""



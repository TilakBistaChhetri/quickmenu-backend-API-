


from rest_framework import generics, status
from calc.models.menu.item import Item
from calc.serializers import ItemSerializer
from utils.response_wrapper import api_response  



from rest_framework import status
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

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
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return api_response(
                data=[serializer.data],  # wrap single object in list
                message=["Item created successfully"],
                status="success",
                remark="item_created",
                http_code=status.HTTP_201_CREATED
            )
        else:
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



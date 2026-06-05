







from rest_framework import generics, status
from calc.models.category import Category
from calc.serializers import CategorySerializer
from utils.response_wrapper import api_response


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


    # GET
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return api_response(
            data=serializer.data,
            message=["Categories fetching successfully"],
            status="success",
            remark="categories_fetched"
        )
    


    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            #self.perform_create(serializer)
            serializer.save(client=self.request.user.client)

            return api_response(
                data=[serializer.data],   
                message=["Category created successfully"],
                status="success",
                remark="category_created",
                http_code=status.HTTP_201_CREATED
            )

        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )
    

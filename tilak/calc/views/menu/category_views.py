

from rest_framework import generics, status
from calc.models.menu.category import Category
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
            message=["Categories retrieved successfully"],
            status="success",
            remark="categories_fetched"
        )
    


    
    # PATCH / PUT (update)
    def update(self, request, *args, **kwargs):
        partial = True  # PATCH = partial update
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return api_response(
                data=[serializer.data],
                message=["Category updated successfully"],
                status="success",
                remark="category_updated"
            )
        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )

    # DELETE
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return api_response(
            data=[],
            message=["Category deleted successfully"],
            status="success",
            remark="category_deleted"
        )

    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)

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




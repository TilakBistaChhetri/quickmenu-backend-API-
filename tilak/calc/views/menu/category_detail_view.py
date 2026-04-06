

# calc/views/menu/category_detail_view.py
from rest_framework import generics, status
from calc.models.menu.category import Category
from calc.serializers import CategorySerializer
from utils.response_wrapper import api_response

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'  # matches URL: categories/<int:id>/

    # GET: Retrieve single category
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return api_response(
            data=[serializer.data],
            message=["Category retrieved successfully"],
            status="success",
            remark="category_fetched"
        )

    # PATCH: Partial update
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # PATCH mode
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
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

    # DELETE: Remove category
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return api_response(
            data=[],
            message=["Category deleted successfully"],
            status="success",
            remark="category_deleted"
        )
    
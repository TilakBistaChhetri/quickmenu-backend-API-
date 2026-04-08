

from rest_framework import generics, status
from calc.models.menu.item import Item
from calc.serializers import ItemSerializer
from utils.response_wrapper import api_response

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    lookup_field = 'id'  # lookup by item id

    def get_queryset(self):
        return Item.objects.all()

    # GET item by id
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Item.DoesNotExist:
            return api_response(
                data=[],
                message=["Item not found"],
                status="fail",
                remark="not_found",
                http_code=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance)
        return api_response(
            data=[serializer.data],
            message=["Item fetched successfully"],
            status="success",
            remark="item_fetched",
            http_code=status.HTTP_200_OK
        )

    # UPDATE item by id
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Item.DoesNotExist:
            return api_response(
                data=[],
                message=["Item not found"],
                status="fail",
                remark="not_found",
                http_code=status.HTTP_404_NOT_FOUND
            )

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return api_response(
                data=[serializer.data],
                message=["Item updated successfully"],
                status="success",
                remark="item_updated",
                http_code=status.HTTP_200_OK
            )

        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )

    # DELETE item by id
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return api_response(
                data=[],
                message=["Item deleted successfully"],
                status="success",
                remark="item_deleted",
                http_code=status.HTTP_200_OK
            )
        except Item.DoesNotExist:
            return api_response(
                data=[],
                message=["Item not found"],
                status="fail",
                remark="not_found",
                http_code=status.HTTP_404_NOT_FOUND
            )
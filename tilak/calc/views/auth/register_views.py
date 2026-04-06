




# calc/views.py
from rest_framework import generics, status
from django.contrib.auth.models import User
from calc.serializers.auth.register_serializer import RegisterSerializer


from utils.response_wrapper import api_response


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)

            return api_response(
                data=[serializer.data],   # same as category format
                message=["User registered successfully"],
                status="success",
                remark="user_registered",
                http_code=status.HTTP_201_CREATED
            )

        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )
    





#     """

#     CategoryListCreateView:
#     -CategoryListCreateView is our custom view class
#     -In Django REST Framework (DRF), a view handles HTTP requests like GET, POST, PUT, DELETE.
#     -You named it CategoryListCreateView because it will list categories and allow creating new categories.

#     """






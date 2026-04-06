from rest_framework import generics, status
from calc.serializers.auth.login_serializer import LoginSerializer
from utils.response_wrapper import api_response

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return api_response(
                data=[{"id": user.id, "username": user.username, "email": user.email}],
                message=["Login successful"],
                status="success",
                remark="login_success",
                http_code=status.HTTP_200_OK
            )

        return api_response(
            data=serializer.errors,
            message=["Login failed"],
            status="error",
            remark="login_failed",
            http_code=status.HTTP_400_BAD_REQUEST
        )
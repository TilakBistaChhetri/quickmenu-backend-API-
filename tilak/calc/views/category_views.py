



from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from calc.models.category import Category
from calc.models.restaurant_user import RestaurantUser
from calc.serializers import CategorySerializer
from utils.response_wrapper import api_response


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        restaurant_user = RestaurantUser.objects.get(
            user=self.request.user
        )
        return Category.objects.filter(
            restaurant=restaurant_user.restaurant
        )

    # GET
    def list(self, request, *args, **kwargs):

     

        serializer = self.get_serializer(
            self.get_queryset(),
            many=True
        )

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

            restaurant_user = RestaurantUser.objects.get(
                user=request.user
            )

            serializer.save(
                restaurant=restaurant_user.restaurant
            )

            return api_response(
                data=[serializer.data],
                message=["Category created successfully"],
                status="success",
                remark="category_created",
                http_code=status.HTTP_201_CREATED
            )

        print("SERIALIZER ERRORS =", serializer.errors)

        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST
        )
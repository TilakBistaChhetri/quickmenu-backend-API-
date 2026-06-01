










from rest_framework import generics, status
#from calc.models.home.about import Contact
from calc.serializers import ContactSerializer
from utils.response_wrapper import api_response
from calc.models import Contact


class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


    #POST

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            self.perform_create(serializer)


            return api_response(
                data= [serializer.data],
                message = ["Contact data created successfully"],
                status = "success",
                remark =  "contact created",
                http_code = status.HTTP_201_CREATED
            )
        
        return api_response(
            data=serializer.errors,
            message=["Validation failed"],
            status="error",
            remark="validation_error",
            http_code=status.HTTP_400_BAD_REQUEST

        )

    






    #GET


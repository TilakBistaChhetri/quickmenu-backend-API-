


from calc.models.contact import Contact
from calc.serializers.contact_serializer import ContactSerializer

from rest_framework import generics, status


from utils.response_wrapper import api_response

class ContactDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    
    serializer_class = ContactSerializer
    lookup_field = 'id'


# GET
def retrieve(self, request, *args, **kwargs):
    instance = self.get_object()
    serializer = self.get_serializer(instance)
    return api_response(
        data = serializer.data,
        message = ['Contact details fetched successfully'],
        status = "success",
        remark = 'contact details fetched'
    )


#PATCH 

def update(self, request, *args, **kwargs):
    instance = self.get_object()
    partial = kwargs.pop('partial', True) 
    serializer = self.get_serializer(instance, data = request.data, partial = True)

    if serializer.is_valid():
        self.perform_update(serializer)
        return api_response(
            data = serializer.data,
            message = ['Contact details updated successfully'],
            status = 'success',
            remark = 'contact details updated'
        )
    return api_response(
        data = serializer.error,
        message = ['validation failed'],
        staus = 'error',
        remark = 'validation error',
        http_code = status.HTTP_400_BAD_REQUEST
    ) 



    



    
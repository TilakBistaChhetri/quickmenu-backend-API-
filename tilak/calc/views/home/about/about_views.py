
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from calc.serializers.home.about.about_serializer import AboutSerializer
from calc.models.home.about.about import About

# /api/about -> GET all, POST new
class AboutView(APIView):

    def get(self, request):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response({
            "remark": "about_fetched",
            "status": "success",
            "message": ["About data retrieved successfully"],
            "data": serializer.data
        })

    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "remark": "about_created",
                "status": "success",
                "message": ["About entry created successfully"],
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "remark": "validation_error",
            "status": "fail",
            "message": serializer.errors,
            "data": []
        }, status=status.HTTP_400_BAD_REQUEST)


# /api/about/<id>/ -> GET, PATCH, DELETE single entry
class AboutDetailView(APIView):

    def get_object(self, id):
        try:
            return About.objects.get(id=id)
        except About.DoesNotExist:
            return None

    def get(self, request, id):
        about = self.get_object(id)
        if about:
            serializer = AboutSerializer(about)
            return Response({
                "remark": "about_fetched",
                "status": "success",
                "message": ["About entry retrieved successfully"],
                "data": serializer.data
            })
        return Response({
            "remark": "not_found",
            "status": "fail",
            "message": ["About entry not found"],
            "data": []
        }, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):
        about = self.get_object(id)
        if not about:
            return Response({
                "remark": "not_found",
                "status": "fail",
                "message": ["About entry not found"],
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = AboutSerializer(about, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "remark": "about_updated",
                "status": "success",
                "message": ["About entry updated successfully"],
                "data": serializer.data
            })
        return Response({
            "remark": "validation_error",
            "status": "fail",
            "message": serializer.errors,
            "data": []
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        about = self.get_object(id)
        if not about:
            return Response({
                "remark": "not_found",
                "status": "fail",
                "message": ["About entry not found"],
                "data": []
            }, status=status.HTTP_404_NOT_FOUND)

        about.delete()
        return Response({
            "remark": "about_deleted",
            "status": "success",
            "message": ["About entry deleted successfully"],
            "data": []
        }, status=status.HTTP_204_NO_CONTENT)
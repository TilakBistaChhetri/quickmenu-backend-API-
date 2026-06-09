






# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from calc.serializers.about_serializer import AboutSerializer
# from calc.models.about import About
# from calc.models.restaurant import Restaurant

# # /api/restaurants/<restaurant_id>/about -> GET all, POST new
# class AboutView(APIView):

#     def get(self, request, restaurant_id):
#         try:
#             Restaurant.objects.get(id=restaurant_id)
#         except Restaurant.DoesNotExist:
#             return Response({
#                 "remark": "restaurant_not_found",
#                 "status": "fail",
#                 "message": ["Restaurant not found"],
#                 "data": []
#             }, status=status.HTTP_404_NOT_FOUND)

#         abouts = About.objects.filter(restaurant_id=restaurant_id)
#         serializer = AboutSerializer(abouts, many=True)
#         return Response({
#             "remark": "about_fetched",
#             "status": "success",
#             "message": ["About data retrieved successfully"],
#             "data": serializer.data
#         })

#     def post(self, request, restaurant_id):
#         try:
#             restaurant = Restaurant.objects.get(id=restaurant_id)
#         except Restaurant.DoesNotExist:
#             return Response({
#                 "remark": "restaurant_not_found",
#                 "status": "fail",
#                 "message": ["Restaurant not found"],
#                 "data": []
#             }, status=status.HTTP_404_NOT_FOUND)

#         data = request.data.copy()
#         data['restaurant'] = restaurant.id
#         serializer = AboutSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "remark": "about_created",
#                 "status": "success",
#                 "message": ["About entry created successfully"],
#                 "data": [serializer.data]
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             "remark": "validation_error",
#             "status": "fail",
#             "message": serializer.errors,
#             "data": []
#         }, status=status.HTTP_400_BAD_REQUEST)


# # /api/restaurants/<restaurant_id>/about/<id>/ -> GET, PATCH, DELETE single entry
# class AboutDetailView(APIView):

#     def get_object(self, restaurant_id, id):
#         try:
#             return About.objects.get(id=id, restaurant_id=restaurant_id)
#         except About.DoesNotExist:
#             return None

#     def get(self, request, restaurant_id, id):
#         about = self.get_object(restaurant_id, id)
#         if about:
#             serializer = AboutSerializer(about)
#             return Response({
#                 "remark": "about_fetched",
#                 "status": "success",
#                 "message": ["About entry retrieved successfully"],
#                 "data": [serializer.data]
#             })
#         return Response({
#             "remark": "not_found",
#             "status": "fail",
#             "message": ["About entry not found"],
#             "data": []
#         }, status=status.HTTP_404_NOT_FOUND)

#     def patch(self, request, restaurant_id, id):
#         about = self.get_object(restaurant_id, id)
#         if not about:
#             return Response({
#                 "remark": "not_found",
#                 "status": "fail",
#                 "message": ["About entry not found"],
#                 "data": []
#             }, status=status.HTTP_404_NOT_FOUND)

#         serializer = AboutSerializer(about, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 "remark": "about_updated",
#                 "status": "success",
#                 "message": ["About entry updated successfully"],
#                 "data": [serializer.data]
#             })
#         return Response({
#             "remark": "validation_error",
#             "status": "fail",
#             "message": serializer.errors,
#             "data": []
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, restaurant_id, id):
#         about = self.get_object(restaurant_id, id)
#         if not about:
#             return Response({
#                 "remark": "not_found",
#                 "status": "fail",
#                 "message": ["About entry not found"],
#                 "data": []
#             }, status=status.HTTP_404_NOT_FOUND)

#         about.delete()
#         return Response({
#             "remark": "about_deleted",
#             "status": "success",
#             "message": ["About entry deleted successfully"],
#             "data": []
#         }, status=status.HTTP_204_NO_CONTENT)
    

    
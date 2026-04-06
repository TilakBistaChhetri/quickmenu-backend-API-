


from rest_framework.response import Response
from rest_framework import status as http_status

def api_response(data=None, message=None, status="success", remark="success", http_code=http_status.HTTP_200_OK):
    """
    Uniform API Response Formatter
    """
    if message is None:
        message = []
    elif isinstance(message, str):
        message = [message]
    
    response_data = {
        "remark": remark,
        "status": status,
        "message": message,
        "data": data
    }
    
    return Response(response_data, status=http_code)
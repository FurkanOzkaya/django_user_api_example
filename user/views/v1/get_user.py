
from serializers.request_serializers import UserModelSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from common.common_funtions import generate_200_model_response
from serializers.response_serialziers import UserResponseSerializer
from rest_framework.permissions import IsAuthenticated
from common.decarators import get_user

RESPONSE = generate_200_model_response(UserResponseSerializer)


@swagger_auto_schema(tags=['User'], operation_description="Get User Information", method="GET", responses=RESPONSE)
@api_view(["GET"])
@permission_classes([IsAuthenticated])
@get_user()
def get_user_info(request, serializer, user):
    serializer = UserModelSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from common.decarators import validator
from serializers.request_serializers import UserUpdateParameterSerializer, UserModelSerializer
from drf_yasg.utils import swagger_auto_schema
from common.common_funtions import generate_200_base_response
from common.decarators import get_user


RESPONSE = generate_200_base_response()


@swagger_auto_schema(tags=['User'], operation_description="Change User Informations", method="POST", request_body=UserUpdateParameterSerializer, responses=RESPONSE, USE_SESSION_AUTH=False)
@api_view(["POST"])
@validator("body", UserUpdateParameterSerializer)
@get_user()
def update_user(request, serializer, user):
    print(request.data)
    if serializer.data:
        user_serializer = UserModelSerializer(
            user, data=serializer.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save(data=serializer.data)
            return Response(status=status.HTTP_200_OK)
        print("asdasd", serializer.errors)
    return Response(status=status.HTTP_400_BAD_REQUEST)

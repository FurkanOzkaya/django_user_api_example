
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from common.decarators import validator
from serializers.request_serializers import UserModelSerializer
from drf_yasg.utils import swagger_auto_schema
from common.common_funtions import generate_201_base_response


RESPONSE = generate_201_base_response()


@swagger_auto_schema(tags=['User'], operation_description="Register Api", method="POST", request_body=UserModelSerializer, responses=RESPONSE, USE_SESSION_AUTH=False)
@api_view(["POST"])
@validator("body", UserModelSerializer)
def register_user(request, serializer):
    serializer.save()
    return Response(status=status.HTTP_201_CREATED)

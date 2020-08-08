from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from rest_framework.response import Response

from rest.permissions import IsStaffUser
from user.models import User
from rest.serializers import SignUpSerializer

from rest.models import Info
from rest.serializers import InfoModelSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class InfoModelViewSet(ModelViewSet):
    serializer_class = InfoModelSerializer
    queryset = Info.objects.all()
    authentication_classes = [TokenAuthentication, ]

    def get_permissions(self):
        if self.action == 'create' or self.action == 'update' or self.action == 'destroy':
            permissions = [IsStaffUser]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        ser = SignUpSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        pw = ser.validated_data.pop('password')
        validated_data = ser.validated_data
        u = User.objects.create(**validated_data)
        u.set_password(pw)
        u.save()
        return Response(validated_data)

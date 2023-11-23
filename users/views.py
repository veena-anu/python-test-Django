from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, YourNotificationSerializer
from .models import UserNotification, LoginLog
from core_viewsets.custom_viewsets import CreateViewSet, ListViewSet

class RegisterViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = RegisterSerializer
    queryset = get_user_model().objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        phone_number = serializer.validated_data.get('phone_number')

        user = get_user_model().objects.create_user(email=email, password=password, phone_number=phone_number)

        UserNotification.objects.create(user_id=user, notification_text='Welcome to the platform!')

        return Response(
            {'code': 200, 'message': 'success', 'user_id': user.pk},
            status=status.HTTP_201_CREATED
        )

class LoginViewSet(CreateViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        try:
            user_obj = get_user_model().objects.get(email=email, password=password)
        except get_user_model().DoesNotExist:
            return Response({'code': 401, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        user_obj.last_login = timezone.now()
        user_obj.save()

        login_log, created = LoginLog.objects.get_or_create(user_id=user_obj)
        login_log.login_count += 1
        login_log.last_logged_in = timezone.now()
        login_log.save()

        refresh = RefreshToken.for_user(user_obj)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response(
            {
                'code': 200,
                'message': 'success',
                'access_token': access_token,
                'refresh_token': refresh_token,
                'user_id': user_obj.pk,
                'name': user_obj.first_name,
                'email': user_obj.email,
                'last_login': user_obj.last_login,
            },
            status=status.HTTP_200_OK
        )

class MeViewSet(ListViewSet):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def list(self, request, *args, **kwargs):
        user = self.request.user

        notifications = UserNotification.objects.filter(user_id=user, is_read=False)
        login_log = LoginLog.objects.get(user_id=user)

        serialized_user = UserSerializer(user).data
        serialized_notifications = YourNotificationSerializer(notifications, many=True).data
        serialized_login_log = LoginSerializer(login_log).data

        return Response({
            'user': serialized_user,
            'notifications': serialized_notifications,
            'login_log': serialized_login_log,
        })

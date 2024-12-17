from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, LoginSerializer, PasswordResetSerializer
from .models import CustomUser

class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint to register a new user.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    """
    API endpoint to log in a user.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

class PasswordResetView(APIView):
    """
    API endpoint to request a password reset.
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = CustomUser.objects.get(email=email)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        reset_link = f"http://yourdomain.com/reset-password/{uid}/{token}/"
        send_mail(
            'Password Reset Request',
            f'Click the following link to reset your password: {reset_link}',
            'from@yourdomain.com',
            [email],
            fail_silently=False,
        )
        return Response({"detail": "Password reset email has been sent."}, status=200)

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


    @swagger_auto_schema(
        operation_description="Retrieve or update user profile",
        responses={200: UserSerializer, 401: "Unauthorized", 403: "Forbidden"}
    )
    def get(self, request, *args, **kwargs):
        print(request.META.get('HTTP_AUTHORIZATION'))
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update user profile",
        request_body=UserSerializer,
        responses={200: UserSerializer, 400: "Bad Request", 401: "Unauthorized", 403: "Forbidden"}
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get_object(self):
        return self.request.user
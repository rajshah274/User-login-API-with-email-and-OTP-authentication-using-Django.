from django.utils.crypto import get_random_string
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from .models import User, OTP
from .serializers import UserSerializer
from .utils import generate_token

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful. Please verify your email.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RequestOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
            otp_code = get_random_string(6, '0123456789')
            OTP.objects.create(user=user, otp_code=otp_code)
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp_code}',
                'noreply@example.com',
                [email],
            )
            return Response({'message': 'OTP sent to your email.'})
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp_code = request.data.get('otp')
        try:
            user = User.objects.get(email=email)
            otp = OTP.objects.filter(user=user, otp_code=otp_code).first()
            if otp:
                token = generate_token(user)
                return Response({'message': 'Login successful.', 'token': token})
            return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

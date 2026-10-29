import time
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.testapp.tasks import send_welcome_email_task

class StatsView(APIView):
    def get(self, request):
        cache_key = 'heavy_stats_key'
        stats = cache.get(cache_key)
        
        if not stats:
            time.sleep(2)
            stats = {"users_count": 1000, "active_orders": 42}
            cache.set(cache_key, stats, timeout=60)
            
        return Response(stats, status=status.HTTP_200_OK)

class RegisterView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        send_welcome_email_task.delay(email)
        
        return Response({"message": "Registration received, processing email in background."}, status=status.HTTP_201_CREATED)
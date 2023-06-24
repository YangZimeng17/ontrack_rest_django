from rest_framework import generics, permissions
from .serializers import MaterialTypeSerializer
from materialmanager.models import MaterialType
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.contrib.auth import authenticate

class MaterialTypeListCreate(generics.ListCreateAPIView):
    serializer_class = MaterialTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MaterialType.objects.filter(active = 1).order_by('id')

    def perform_create(self, serializer):
        serializer.save()

class MaterialTypeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MaterialTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MaterialType.objects.order_by('id')

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request=request,
            username=data['username'],
            password=data['password']
        )

        if user is None:
            return JsonResponse({'error': 'unable to login. check username and password'}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
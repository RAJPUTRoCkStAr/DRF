from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializer import AditSerializer
from .models import Adit
# Create your views here

class AditCreate(generics.CreateAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditListCreate(generics.ListCreateAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditUpdate(generics.UpdateAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditRetireve(generics.RetrieveAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditDestroy(generics.DestroyAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditRAV(generics.RetrieveAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditAV(generics.GenericAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditLAV(generics.ListAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditRUDAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditRDAV(generics.RetrieveDestroyAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]

class AditRUAV(generics.RetrieveUpdateAPIView):
    queryset = Adit.objects.all()
    serializer_class = AditSerializer
    permission_classes = [AllowAny]
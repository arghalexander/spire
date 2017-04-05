from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import Member

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


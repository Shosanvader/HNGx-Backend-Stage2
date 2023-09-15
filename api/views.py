from rest_framework import viewsets  
from .serializers import PersonSerializer  
from .models import Person  

class PersonView(viewsets.ModelViewSet):  
    serializer_class = PersonSerializer  
    queryset = Person.objects.all()

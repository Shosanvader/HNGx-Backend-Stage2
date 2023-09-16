from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import PersonSerializer
from .models import Person

class PersonView(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

    # Custom create method
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)

    # Custom update method
    def update(self, request, *args, **kwargs):
        # Your custom logic here
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # Custom destroy (delete) method
    def destroy(self, request, *args, **kwargs):
        # Your custom logic here
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

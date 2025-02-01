# viuews for the recipe apis

from rest_framework import (
    viewsets,
    mixins,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    Tag,
)

from recipe import serializers

class RecipeViewSet(viewsets.ModelViewSet):
   """ view for manage recipe apis"""
   serializer_class = serializers.RecipeDetailSerializer
   queryset = Recipe.objects.all()
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      """ retrieve recipes for authenticated user"""
      return self.queryset.filter(user=self.request.user).order_by('-id')

   def get_serializer_class(self):
      """return the serializer class for request"""
      if self.action == 'list':
         return serializers.RecipeSerializer

      return self.serializer_class

   def perform_create(self, serializer):
      """create a new recipe"""
      serializer.save(user=self.request.user)

class TagViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
   """manage tags in the database"""
   serializer_class = serializers.TagSerializer
   queryset = Tag.objects.all()
   authentication_classes = [TokenAuthentication]
   permission_classes = [IsAuthenticated]

   def get_queryset(self):
      """filter queryset to authenticated user"""
      return self.queryset.filter(user=self.request.user).order_by('-name')



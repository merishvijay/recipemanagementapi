
from django.shortcuts import render


# Create your views here.
from rest_framework import viewsets
from recipe.models import Recipe
from recipe.serializer import RecipeSerializer
from recipe.models import Review_or_Comment
from recipe.serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from recipe.serializer import UserSerializer
from django.db.models import Q
from rest_framework.response import Response
from rest_framework.views import APIView



# class RecipeDetails(viewsets.ModelViewSet):
#     queryset=Recipe.objects.all()
#     serializer_class=RecipeSerializer



class RecipeDetails(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer

class ReviewandRating(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Review_or_Comment.objects.all()
    serializer_class = ReviewSerializer


class CreateUser(viewsets.ModelViewSet):         #  --------By using  Viewset Function
    queryset = User.objects.all()
    serializer_class = UserSerializer

class Search(APIView):
    def get(self, request):
        query = self.request.query_params.get('search')
        if query:
            # Perform search based on the query parameter
            recipes = Recipe.objects.filter(
                Q(name__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(cuisine__icontains=query) |
                Q(meal_type__icontains=query)
            )
            serializer = RecipeSerializer(recipes, many=True)
            return Response(serializer.data)
        else:
            return Response([])




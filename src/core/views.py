from django.shortcuts import render
from django.http import JsonResponse

#third  party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


class PostView(mixins.ListModelMixin, 
               mixins.CreateModelMixin, 
               generics.GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    
        
class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.list(self, request, *args, **kwargs)
    
class PostListCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer 
    queryset = Post.objects.all()  
    
############## WORKING WITH AUTHENTICATION && SERIALIZERS ##############

#class TestView(APIView): 
    
#    Permission_classes = (IsAuthenticated, )
    
#    def get(self, request, *args, **kwargs):
#        qs = Post.objects.all()
        # To recieve one instance
#        post = qs.first()
        
#        #serializer = PostSerializer(qs, many=True)
        
        # Comment next line to remove one instance post return
#        serializer = PostSerializer(post)
#        return Response(serializer.data)
    
#    def post(self, *args, **kwargs):
#        serializer = PostSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors)

############## WORKING WITH AUTHENTICATION && SERIALIZERS ##############

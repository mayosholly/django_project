# from django.shortcuts import render, get_list_or_404
# from rest_framework import viewsets, status
# from rest_framework.request import Request
# from .models import Post
# from classposts.serializer import PostSerializer
# from rest_framework.response import Response
# # Create your views here.

# # class view set
# # class PostView(viewsets.ViewSet):
# #     def list(self, request):
# #         queryset=Post.objects.all()
# #         serializer = PostSerializer(instance=queryset, many=True)
# #         return Response(data=serializer.data, status=status.HTTP_200_OK )
    
# #     def retrieve(self, request:Request, pk=None):
# #         post = get_list_or_404(Post, pk=pk)
# #         serializer = PostSerializer(instance=post)
# #         return Response(data=serializer.data, status=status.HTTP_200_OK)


# # model view set
    
# class PostView(viewsets.ViewSet):
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer
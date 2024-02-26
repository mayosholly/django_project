from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view,APIView, permission_classes
from .models import Post
from .serializers import PostSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import ReadOnly, AuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination

class CustomPaginator():
    page_size = 3
    page_query_param = "page"
    page_size_query_param = "page_size"

# posts = [
#     {
#         "id": 1,
#         "title": "Hello World",
#         "body": "Hello World"
#     },
#     {
#         "id": 2,
#         "title": "Hello World",
#         "body": "Hello World"
#     },
#     {
#         "id": 3,
#         "title": "Hello World",
#         "body": "Hello World"
#     }
# ]


class PostListCreateView(generics.GenericAPIView,
                                   mixins.ListModelMixin,
                                   mixins.CreateModelMixin):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    
    def get(self, request:Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request:Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
class PostRetreiveUpdateDeleteView(generics.GenericAPIView,
                                   mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin,
                                   mixins.DestroyModelMixin):
    """
        a view for creating and listing post 
    """
    serializer_class = PostSerializer
    permission_classes = [AuthorOrReadOnly]
    queryset = Post.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class PostRetreiveUpdateDeleteView(APIView):
#     serializer_class = PostSerializer
    
#     def get(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         serializer = self.serializer_class(instance=post)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         data = request.data
#         serializer = self.serializer_class(instance=post,data=data)
#         if(serializer.is_valid()):
#             serializer.save()
#             response  = {
#                 "message" : "Post updated successfully",
#                 "data" : serializer.data
#             }
#             return Response(response, status=status.HTTP_200_OK)
#         return Response(serializer.error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def delete(self, request:Request, post_id:int):
#         post = get_object_or_404(Post, pk=post_id)
#         post.delete()
#         response={'message':'Post deleted Successfully'}
#         return Response(response,status=status.HTTP_204_NO_CONTENT)

# class PostListCreateView(APIView):
#     """
#         a view for creating and listing post 
#     """
#     serializer_class = PostSerializer
#     def get(self, request: Request, *args, **kwargs):
#         posts = Post.objects.all()
#         serializer = self.serializer_class(instance=posts, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request: Request, *args, **kwargs):
#         data = request.data

#         serializer = self.serializer_class(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 'message' : 'Post created',
#                 'data' : serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)
#         return Response(data=serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(http_method_names=["GET", "POST"])
@permission_classes([AllowAny])
def homepage(request:Request):

    if request.method == "POST":
        data = request.data

        response = {"message": "Hello World!", "data": data}
        return Response(data=response, status=status.HTTP_201_CREATED)

    response = {"message": "Hello World"}
    return Response(data=response, status=status.HTTP_200_OK)


# @api_view(http_method_names=['GET'])
# @permission_classes([IsAuthenticated])
# def get_posts_for_current_user(request: Request):
#     user = request.user

#     serializer = Cu

class ListPostsForAuthor(
    generics.GenericAPIView,
    mixins.ListModelMixin
):
    queryset = Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[IsAuthenticated]
    pagination_class = CustomPaginator

    def get_queryset(self):
        username = self.request.query_params.get("username") or None

        queryset = Post.objects.all()

        if username is not None:
            return Post.objects.filter(author__username=username)
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter(author=user)
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)


# @api_view(http_method_names=['GET', 'POST'])

# def get_posts(request:Request):
#     posts = Post.objects.all()

#     if request.method == 'POST':
#         data = request.data
#         serializer = PostSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Post Created",
#                 "data": serializer.data
#             }
#             return Response(data=response, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     serializer = PostSerializer(instance=posts, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

# @api_view(http_method_names=['GET',])
# def get_post(request: Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)

#     serializer = PostSerializer(instance=post)

#     response = {
#         "message" : "post",
#         "data" : serializer.data
#     }

#     return Response(data=response, status=status.HTTP_200_OK)




# @api_view(http_method_names=["PUT"])
# def update_post(request: Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     data = request.data
#     serializer = PostSerializer(instance=post, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         response = {
#             "message" : "post updated",
#             "data" : serializer.data
#         }
#         return Response(data=response, status=status.HTTP_200_OK)
#     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# @api_view(http_method_names=["DELETE"])
# def delete_post(request: Request, post_id:int):
#     post = get_object_or_404(Post, pk=post_id)
#     post.delete()
#     response = {
#         "message" : "post deleted"
#     }
#     return Response(data=response, status=status.HTTP_200_OK)
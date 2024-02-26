from . import views
from django.urls import path

urlpatterns = [

    path("", views.PostListCreateView.as_view(), name="posts_list"),
    path("<int:pk>/", views.PostRetreiveUpdateDeleteView.as_view(), name="posts_list"),
    path("posts_for/", views.ListPostsForAuthor.as_view(), name="posts_for_current_user"),


    # path("posts_for_current_user", views.ListPostsForAuthor.as_view(), name="posts_for_current_user"),

    # path("", views.PostListCreateView.as_view(), name="posts_list"),
    # path("<int:post_id>/", views.PostRetreiveUpdateDeleteView.as_view(), name="posts_list"),


    path("homepage/", views.homepage, name="posts_home"),
    # path("", views.get_posts, name="posts_list"),
    # path("<int:post_id>", views.get_post, name="get_post"),
    # path("update/<int:post_id>/", views.update_post, name="update_post"),
    # path("delete/<int:post_id>/", views.delete_post, name="delete_post"),
]
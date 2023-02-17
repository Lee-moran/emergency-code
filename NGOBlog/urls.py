from django.urls import path, include
from . import views
from .views import index

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path("", views.PostList.as_view(), name="blogs"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
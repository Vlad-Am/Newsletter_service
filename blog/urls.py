from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urls = [
    path('blog/view_blog/<slug:the_slug>/', BlogDetailView.as_view(), name='view_blog'),
]

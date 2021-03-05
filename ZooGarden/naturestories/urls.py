from django.urls import path
from . import views

urlpatterns = [
    path('', views.stories_main),
    path('create', views.stories_create),
    path('<int:numb>', views.stories_read_more),
    path('ajax_zone_stories', views.stories_partial),

    path('new_story', views.storiesck),
    path('new_comment', views.new_comment),

]
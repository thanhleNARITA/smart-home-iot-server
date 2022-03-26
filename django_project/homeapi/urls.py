from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('room-button/update/<str:pk>/', views.taskUpdate, name='update'),
    path('room-button/view/', views.taskList, name='view-all-in-room'),
    path('room-button/createnew/', views.taskCreate, name='creat-new-status'),

    path('todolist/view/', views.todolist_view, name='view-todolist'),
    path('todolist/view/<str:pk>/', views.todolist_detail, name='view-todolist-detail'),
    path('todolist/create/', views.todolist_create_new, name='create-todolist'),
    path('todolist/update/<str:pk>/', views.todolist_update, name='update-todolist'),
    path('todolist/delete/<str:pk>/', views.todolist_delete, name='delete-todolist'),

    path('room-status/view/', views.roomstatus_view, name='view-room-status'),
    path('room-status/view/<str:pk>/', views.roomstatus_view_detail, name='view-room-status-detail'),
    path('room-status/create/', views.roomstatus_create_new, name='create-room-status'),
    path('room-status/update/<str:pk>/', views.roomstatus_update, name='update-room-status'),
    path('room-status/delete/<str:pk>/', views.roomstatus_delete, name='delete-room-status'),
    path('stream/', views.stream_response, name='stream_response'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

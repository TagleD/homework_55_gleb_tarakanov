from django.urls import path

from webapp.views.base import index_view
from webapp.views.tasks import tasks_view, add_view, detail_view, update_view

urlpatterns = [
    path('', index_view),
    path('tasks', tasks_view),
    path('task', detail_view),
    path('tasks/add', add_view),
    path('task/<int:pk>/update/', update_view, name='task_update')
]

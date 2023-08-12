from django.urls import path
from rest_framework.routers import SimpleRouter

from users import views
from users.api import views as api_views

app_name = 'users'

urlpatterns = [
    path('', views.UsersListView.as_view(), name='users-list'),
    path('<int:pk>', views.UsersDetailView.as_view(), name='users-detail'),
    path('create/', views.UsersCreateView.as_view(), name='users-create')
]

router = SimpleRouter()
router.register('api', api_views.UsersModelViewSet)

urlpatterns += router.urls

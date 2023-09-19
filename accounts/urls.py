from django.urls import path
from accounts import views


urlpatterns = [
    path('post-accounts/', views.post_accounts),
    path('get-accounts/', views.get_accounts),
    path('get-update-delete-account/<int:pk>', views.get_update_delete_account)
]

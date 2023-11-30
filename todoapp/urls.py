from django.urls import path
from . import views

urlpatterns = [
    # 作成
    path("create/", views.TodoCreate.as_view(), name="todo_create"),
    # 更新
    # 削除
    path("delete/<int:pk>", views.TodoDelete.as_view(), name="todo_delete"),
    # 詳細
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name="todo_detail"),
    # 一覧
    path("", views.TodoList.as_view(), name="todo_list")
]

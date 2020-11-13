from django.urls import include, path
from . import views

app_name = 'summary'

urlpatterns = [
    # summarys urls 
    path('', views.SummaryList.as_view(), name='summary_list'),
    path('<int:tag_id>/', views.SummaryList.as_view(), name='summary_list'),
    path('add/', views.SummaryCreate.as_view(), name='summary_add'),
    path('<int:pk>/detail/', views.SummaryDetail.as_view(), name='summary_detail'),
    path('<int:pk>/update/', views.SummaryUpdate.as_view(), name='summary_update'),
    path('<int:pk>/delete/', views.SummaryDelete.as_view(), name='summary_delete'),
]



from django.conf.urls import url
from jnv_api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^v1/admin/user-history', views.AdminUserHistory.as_view()),
    url(r'^v1/user-history', views.DbUserHistory.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)


from django.conf.urls import url
from django.contrib import admin
from exams import views as exam_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^exams/dashboard/', exam_views.dashboard.as_view(), name = 'exam_dashboard' ),
    url(r'^exams/add/', exam_views.exam_add , name = 'exam_add'),
    url(r'^exams/(?P<pk>\d+)/edit/', exam_views.exam_edit , name = 'exam_edit'),
    url(r'^exams/(?P<pk>\d+)/print/', exam_views.exam_print , name = 'exam_print'),
    url(r'^exams/getset/', exam_views.getset , name = 'getset'),
    url(r'^exams/(?P<sub_id>\d+)/sub_delete/', exam_views.sub_delete , name = 'sub_delete'),
]

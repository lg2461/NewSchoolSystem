from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^student_menu/$', views.student_menu, name='student_menu.html'),
    url(r'^$', views.login, name='login.html'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^student/add_one/$', views.student_add_one, name='student/add_one.html'),
    # url(r'^student/select_me/$', views.student_select_me, name='student/select_me.html'),
    url(r'^manage_add/$', views.manage_add),
    url(r'^register_one/$', views.Register.register_one),
    url(r'^register_two/$', views.Register.register_two),
    url(r'^register_three/$', views.Register.register_three),
    url(r'^register_four/$', views.Register.register_four),
    # url(r'^upload_image/$', views.upload_image),
    url(r'^update_user_photo/$', views.update_user_photo),
    # url(r'^student_leave/$', views.student_leave),
    url(r'^sms_verification/$', views.sms_verification),
    url(r'^forget_passwd/$', views.forget_passwd),
]

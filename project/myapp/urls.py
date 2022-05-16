"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_changepassword', views.admin_changepassword, name='admin_changepassword'),
    path('admin_logout', views.admin_logout, name='admin_logout'),
    path('admin_home', views.admin_home, name='admin_home'),

    path('admin_bus_type_master_add', views.admin_bus_type_master_add, name='admin_bus_type_master_add'),
    path('admin_bus_type_master_edit', views.admin_bus_type_master_edit, name='admin_bus_type_master_edit'),
    path('admin_bus_type_master_view', views.admin_bus_type_master_view, name='admin_bus_type_master_view'),
    path('admin_bus_type_master_delete', views.admin_bus_type_master_delete, name='admin_bus_type_master_delete'),

    path('admin_rate_master_add', views.admin_rate_master_add, name='admin_rate_master_add'),
    path('admin_rate_master_view', views.admin_rate_master_view, name='admin_rate_master_view'),
    path('admin_rate_master_delete', views.admin_rate_master_delete, name='admin_rate_master_delete'),

    path('admin_depot_master_add', views.admin_depot_master_add, name='admin_depot_master_add'),
    path('admin_depot_master_edit', views.admin_depot_master_edit, name='admin_depot_master_edit'),
    path('admin_depot_master_view', views.admin_depot_master_view, name='admin_depot_master_view'),
    path('admin_depot_master_delete', views.admin_depot_master_delete, name='admin_depot_master_delete'),

    path('depot_login', views.depot_login, name='depot_login'),
    path('depot_changepassword', views.depot_changepassword, name='depot_changepassword'),
    path('depot_logout', views.depot_logout, name='depot_logout'),
    path('depot_home', views.depot_home, name='depot_home'),

    path('depot_depot_master_view', views.depot_depot_master_view, name='depot_depot_master_view'),
    path('depot_bus_type_master_view', views.depot_bus_type_master_view, name='depot_bus_type_master_view'),
    path('depot_rate_master_view', views.depot_rate_master_view, name='depot_rate_master_view'),

    path('depot_stop_master_add', views.depot_stop_master_add, name='depot_stop_master_add'),
    path('depot_stop_master_edit', views.depot_stop_master_edit, name='depot_stop_master_edit'),
    path('depot_stop_master_view', views.depot_stop_master_view, name='depot_stop_master_view'),
    path('depot_stop_master_delete', views.depot_stop_master_delete, name='depot_stop_master_delete'),

    path('depot_route_master_add', views.depot_route_master_add, name='depot_route_master_add'),
    path('depot_route_master_view', views.depot_route_master_view, name='depot_route_master_view'),
    path('depot_route_master_delete', views.depot_route_master_delete, name='depot_route_master_delete'),

    path('depot_route_stop_details_add', views.depot_route_stop_details_add, name='depot_route_stop_details_add'),
    path('depot_route_stop_details_view', views.depot_route_stop_details_view, name='depot_route_stop_details_view'),
    path('depot_route_stop_details_delete', views.depot_route_stop_details_delete, name='depot_route_stop_details_delete'),

    path('depot_app_form_view',views.depot_app_form_view,name='depot_app_form_view'),
    path('depot_app_form_view1',views.depot_app_form_view1,name='depot_app_form_view1'),
    path('depot_app_form_view2',views.depot_app_form_view2,name='depot_app_form_view2'),
    path('depot_app_form_update',views.depot_app_form_update,name='depot_app_form_update'),

    path('user_login', views.user_login_check, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_home', views.user_home, name='user_home'),
    path('user_details_add', views.user_details_add, name='user_details_add'),
    path('user_changepassword', views.user_changepassword, name='user_changepassword'),

    path('institution_login', views.institution_login_check, name='institution_login'),
    path('institution_logout', views.institution_logout, name='institution_logout'),
    path('institution_home', views.institution_home, name='institution_home'),
    path('institution_details_add', views.institution_details_add, name='institution_details_add'),
    path('institution_changepassword', views.institution_changepassword, name='institution_changepassword'),

    path('institution_depot_master_search', views.institution_depot_master_search, name='institution_depot_master_search'),
    path('institution_depot_master_view', views.institution_depot_master_view, name='institution_depot_master_view'),

    path('institution_route_master_search', views.institution_route_master_search, name='institution_route_master_search'),
    path('institution_route_master_view', views.institution_route_master_view, name='institution_route_master_view'),
    path('institution_route_stop_details_view', views.institution_route_stop_details_view, name='institution_route_stop_details_view'),

    path('institution_student_details_add', views.institution_student_details_add, name='institution_student_details_add'),
    path('institution_student_details_view', views.institution_student_details_view,name='institution_student_details_view'),
    path('institution_student_details_delete', views.institution_student_details_delete,name='institution_student_details_delete'),
    path('institution_student_details_search', views.institution_student_details_search,name='institution_student_details_search'),

    path('institution_app_form_add',views.institution_app_form_add,name='institution_app_form_add'),
    path('institution_app_form_view',views.institution_app_form_view,name='institution_app_form_view'),
    path('institution_app_form_view2', views.institution_app_form_view2, name='institution_app_form_view2'),
    path('institution_app_form_update',views.institution_app_form_update,name='institution_app_form_update'),
    path('institution_app_form_delete', views.institution_app_form_delete, name='institution_app_form_delete'),

]

from django.contrib import admin

# Register your models here.
from .models import user_login, user_details
#user_login,depot_master,feedback,institution_master,student_details,app_form,bus_type_master
#rate_master,route_master,stop_master,route_stop_details,consession_details

from .models import depot_master,feedback,institution_master,student_details,app_form,bus_type_master
from .models import rate_master,route_master,stop_master,route_stop_details,consession_details
admin.site.register(user_login)
admin.site.register(user_details)
admin.site.register(depot_master)
admin.site.register(feedback)
admin.site.register(institution_master)
admin.site.register(student_details)
admin.site.register(app_form)
admin.site.register(bus_type_master)
admin.site.register(rate_master)
admin.site.register(route_master)
admin.site.register(stop_master)
admin.site.register(route_stop_details)
admin.site.register(consession_details)

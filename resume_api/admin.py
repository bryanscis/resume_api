from django.contrib import admin
from .models import Comments, Projects, Experience, Contact, Route

admin.site.register(Comments)
admin.site.register(Projects)
admin.site.register(Experience)
admin.site.register(Contact)
admin.site.register(Route)
from django.contrib import admin
from rides.models import Bus, Driver, Route, Passenger, Trip

admin.site.register(Bus)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Passenger)
admin.site.register(Trip)

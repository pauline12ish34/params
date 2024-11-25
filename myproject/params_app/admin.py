from django.contrib import admin
from .models import ParkingLot, Vehicle, ParkingSpace, ParkingTicket, User, Payment

# Register your models here.
admin.site.register(ParkingLot)
admin.site.register(Vehicle)
admin.site.register(ParkingSpace)
admin.site.register(ParkingTicket)
admin.site.register(User)
admin.site.register(Payment)
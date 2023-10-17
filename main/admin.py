from django.contrib import admin
from .models import Brands,Auto_Washing_Machine_models, Dishwasher_models, Twin_Washing_Machine_models, Vacuum_Cleaner_models, Refrigerator_models, Accessory_models

# Register your models here.
admin.site.register(Brands)
admin.site.register(Auto_Washing_Machine_models)
admin.site.register(Dishwasher_models)
admin.site.register(Twin_Washing_Machine_models)
admin.site.register(Vacuum_Cleaner_models)
admin.site.register(Refrigerator_models)
admin.site.register(Accessory_models)

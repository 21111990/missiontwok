from django.contrib import admin
from . models import Productinshop,Product,BuyProducts
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_id','name','price','stock','image')
class ProductinshopAdmin(admin.ModelAdmin):
    list_display = ('Product_name','image')
class BuyProductsAdmin(admin.ModelAdmin):
        list_display = ('Client_name', 'client_mobile','Products_name','Quantity','price1')
admin.site.register(Product,ProductAdmin)
admin.site.register(Productinshop,ProductinshopAdmin)
admin.site.register(BuyProducts,BuyProductsAdmin)

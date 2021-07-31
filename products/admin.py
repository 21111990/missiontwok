from django.contrib import admin
from . models import Productinshop,Product,BuyProducts,ClientDetailLog,BillDetails,PaymentDone,Client_details
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('Product_id','name','price','stock','image','image1')
class ProductinshopAdmin(admin.ModelAdmin):
    list_display = ('Product_name','image','image1')
class BuyProductsAdmin(admin.ModelAdmin):
        list_display = ('Client_name', 'client_mobile','Products_name','Quantity','price1')
class ClientDetailLogAdmin(admin.ModelAdmin):
    list_display = ('Client_name', 'client_mobile', 'randid')
class BillDetailsAdmin(admin.ModelAdmin):
    list_display = ('Userid','Client_name', 'client_mobile', 'randId','BillDate','BillConfirmDate','TotalAmt','BillCheck')
class PaymentDoneAdmin(admin.ModelAdmin):
    list_display = ('Userid','Client_name', 'client_mobile', 'randId','BillConfirmDate','paymentDate','TotalAmt','DonePayment')
class Client_detailsAdmin(admin.ModelAdmin):
    list_display = ('Userid','Client_name', 'client_mobile', 'Client_Add1','Client_add2','Client_add3','Client_pin','randId')
admin.site.register(Product,ProductAdmin)
admin.site.register(Productinshop,ProductinshopAdmin)
admin.site.register(BuyProducts,BuyProductsAdmin)
admin.site.register(ClientDetailLog,ClientDetailLogAdmin)
admin.site.register(BillDetails,BillDetailsAdmin)
admin.site.register(PaymentDone,PaymentDoneAdmin)
admin.site.register(Client_details,Client_detailsAdmin)

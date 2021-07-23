from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.shortcuts import HttpResponse
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='index'),
    path('index1',views.index1,name='index1'),
    path('ProductId',views.ProductId,name='ProductId'),
    path('add',views.add,name='add'),
    path('Buy',views.Buy,name='Buy'),
    path('Confirm', views.Confirm, name='Confirm'),
    path('NewPro', views.NewPro, name='NewPro'),
    path('AdminLog', views.AdminLog, name='AdminLog'),
    path('BillInfo', views.BillInfo, name='BillInfo'),
    path('DoneBilling', views.DoneBilling, name='DoneBilling'),
    path('Billinglnfo', views.Billinglnfo, name='Billinglnfo'),
    path('BillIDetailnfo', views.BillIDetailnfo, name='BillIDetailnfo'),
    path('ConfBill', views.ConfBill, name='ConfBill'),
    path('PaymentDetailnfo', views.PaymentDetailnfo, name='PaymentDetailnfo'),
    path('ConfPayment', views.ConfPayment, name='ConfPayment'),
    path('DoneList', views.DoneList, name='DoneList'),
    path('Cart', views.Cart, name='Cart'),
    path('History', views.History, name='History')
] + static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

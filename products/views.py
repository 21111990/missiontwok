import os

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm,ImageForm_shop
from .models import Product,Productinshop,BuyProducts,ClientDetailLog,BillDetails,PaymentDone,Client_details
import random
from django import forms


# Create your views here.



def index(request):
    value1 = random.randint(1,10000000)
    request.session['id2'] = value1
    return render(request,'index1.html',{'rand1':value1})

def index1(request):
    if request.session.has_key('id2'):
        if request.method == 'POST':
            val1 = int(request.POST["userid"])
            val2 = str(request.POST["username"])
            val3 = int(request.POST["userMobile"])
            val4 = request.POST["Logid"]

        else:
            val1 = int(request.GET["userid"])
            val2 = str(request.GET["username"])
            val3 = int(request.GET["userMobile"])
            val4 = ""
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            ClientDetailLog_info = ClientDetailLog(Client_name=val2, client_mobile=val3, randid=val1)
            # data1 = ClientDetailLog.objects.raw('SELECT randid FROM products_clientdetaillog WHERE randid = %s', params=[val1])
            if not ClientDetailLog.objects.filter(randid=val1, Client_name=val2, client_mobile=val3).exists():
                ClientDetailLog_info.save()
            UserDetails1 = ClientDetailLog.objects.filter(randid=val1, Client_name=val2, client_mobile=val3)
            ShopProduct = Productinshop.objects.all()
            if val4 == 'ADMIN':
                BillSum = BillDetails.objects.all()
                # return render(request, 'BillDetails.html',{'BillInfo': BillSum})
                BillSum_count = BillDetails.objects.filter(BillCheck="").count()
                Payment_count = PaymentDone.objects.filter(DonePayment="").count()
                Done_count = PaymentDone.objects.filter(DonePayment="Done").count()
                return render(request, 'Adminpage.html',
                              {'count1': BillSum_count, 'count2': Payment_count, 'count3': Done_count})
            else:

                return render(request, 'index.html',
                              {'userId1': val1, 'username': val2, 'userMobile': val3, 'products': ShopProduct,
                               'UserDetailslog': UserDetails1})
        else:
            return redirect('index')

    else:
        return redirect('index')


def ProductId(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            productsID = Product.objects.all()
            val1 = request.POST["prId"]
            val2 = int(request.POST["RandId"])
            val3 = str(request.POST["UserName"])
            val4 = int(request.POST["UserMobile"])
            val5 = int(request.POST["UserId"])
            return render(request, 'PRODUCT.html',
                          {'result': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'UserId': val5,
                           'products': productsID})
        else:
            return redirect('index')
    else:
        return redirect('index')



def add(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            products = Product.objects.all()
            val1 = request.POST["prname1"]
            val2 = int(request.POST["RandId"])
            val3 = str(request.POST["UserName"])
            val4 = int(request.POST["UserMobile"])
            val5 = int(request.POST["UserId"])
            return render(request, 'prdata.html',
                          {'result': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'UserId': val5,
                           'products': products})
        else:
            return redirect('index')

    else:
        return redirect('index')

def Buy(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            products = Product.objects.all()
            val1 = request.POST["Qname"]
            val2 = float(request.POST["Qnty"])
            val3 = float(request.POST["Qprice"])
            res = val2 * val3
            val4 = int(request.POST["RandId"])
            val5 = str(request.POST["UserName"])
            val6 = int(request.POST["UserMobile"])
            val7 = int(request.POST["UserId"])
            val8 = int(request.POST["id"])
            val9 = int(request.POST["stock"])
            a = Product.objects.get(id=val8, name=val1, price=val3)
            a.stock = val9 - val2
            a.save()
            return render(request, 'Quntity.html',
                          {'result': val1, 'result1': val2, 'result2': res, 'userId1': val4, 'username': val5,
                           'userMobile': val6, 'UserId': val7, 'products': products})
        else:
            return redirect('index')

    else:
        return redirect('index')

def Confirm(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            if request.method == 'POST':
                products = Product.objects.all()
                val1 = request.POST["CnClient_Name"]
                val2 = int(request.POST["CnClient_Mobile"])
                val3 = request.POST["CnFname"]
                val4 = float(request.POST["CnFQty"])
                val5 = float(request.POST["CnfPrice"])
                val6 = int(request.POST["CnClient_id"])
                val7 = int(request.POST["UserId"])
                BuyProducts_info = BuyProducts(Client_name=val1, client_mobile=val2, Products_name=val3, Quantity=val4,
                                               price1=val5, randid=val6, Userdid=val7)
                if not BuyProducts.objects.filter(Client_name=val1, client_mobile=val2, Products_name=val3,
                                                  Quantity=val4,
                                                  price1=val5, randid=val6, Userdid=val7).exists():
                    BuyProducts_info.save()
                BuyProducts1 = BuyProducts.objects.all()
                return render(request, 'Confirm.html',
                              {'username': val1, 'userMobile': val2, 'Prname': val3, 'Prqty': val4, 'prPice': val5,
                               'userId1': val6, 'UserId': val7, 'Buyproducts': BuyProducts1})
            else:
                val1 = int(request.GET["id"])
                val2 = request.GET["username"]
                val3 = int(request.GET["userMobile"])
                val4 = int(request.GET["UserId"])
                val5 = int(request.GET["userId1"])
                if BuyProducts.objects.filter(id=val1).exists():
                    DeleteList = BuyProducts.objects.get(id=val1)
                    DeleteList.delete()
                BuyProducts1 = BuyProducts.objects.filter(Client_name=val2, client_mobile=val3, Userdid=val4,
                                                          randid=val5)
                return render(request, 'Confirm.html',
                              {'username': val2, 'userMobile': val3, 'UserId': val4, 'userId1': val5,
                               'Buyproducts': BuyProducts1})
        else:
            return redirect('index')
    else:
        return redirect('index')


def NewPro(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            ShopProduct = Productinshop.objects.all()
            if request.method == 'POST':
                val1 = request.POST["CnClient_Name"]
                val2 = int(request.POST["CnClient_Mobile"])
                val3 = request.POST["CnFname"]
                val4 = float(request.POST["CnFQty"])
                val5 = float(request.POST["CnfPrice"])
                val6 = int(request.POST["CnClient_id"])
                val7 = int(request.POST["UserId"])
                BuyProducts_info = BuyProducts(Client_name=val1, client_mobile=val2, Products_name=val3, Quantity=val4,
                                               price1=val5, randid=val6, Userdid=val7)
                if not BuyProducts.objects.filter(Client_name=val1, client_mobile=val2, Products_name=val3,
                                                  Quantity=val4,
                                                  price1=val5, randid=val6, Userdid=val7).exists():
                    BuyProducts_info.save()
                BuyProducts1 = BuyProducts.objects.all()
                return render(request, 'NewPro.html',
                              {'username': val1, 'userMobile': val2, 'Prname': val3, 'Prqty': val4, 'prPice': val5,
                               'userId1': val6, 'UserId': val7, 'products': ShopProduct, 'Buyproducts': BuyProducts1})
            else:
                val1 = int(request.GET["id"])
                val2 = request.GET["username"]
                val3 = int(request.GET["userMobile"])
                val4 = int(request.GET["UserId"])
                val5 = int(request.GET["userId1"])
                val6 = float(request.GET["Qnty"])
                val7 = request.GET["PName"]
                if BuyProducts.objects.filter(id=val1).exists():
                    DeleteList = BuyProducts.objects.get(id=val1)
                    DeleteList.delete()
                    AddQnty = Product.objects.get(name=val7)
                    AddQnty.stock = AddQnty.stock + val6
                    print(AddQnty.stock + val6)
                    AddQnty.save()
                BuyProducts1 = BuyProducts.objects.filter(Client_name=val2, client_mobile=val3, Userdid=val4,
                                                          randid=val5)
                return render(request, 'NewPro.html',
                              {'username': val2, 'userMobile': val3, 'UserId': val4, 'userId1': val5,
                               'products': ShopProduct,
                               'Buyproducts': BuyProducts1})
        else:
            return redirect('index')

    else:
        return redirect('index')


def BillInfo(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["BillNo"])
            val2 = int(request.POST["BClient_id"])
            val3 = request.POST["BClient_Name"]
            val4 = int(request.POST["BClient_Mobile"])
            val5 = request.POST["BillAmnt"]
            BillDetails_info = BillDetails(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                           TotalAmt=val5)

            if not BillDetails.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                              TotalAmt=val5).exists():
                BillDetails_info.save()
            BillDetails1 = BillDetails.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                                      TotalAmt=val5)
            BuyProducts1 = BuyProducts.objects.filter(Client_name=val3, client_mobile=val4, randid=val2, Userdid=val1)
            if not Client_details.objects.filter(Client_name=val3, client_mobile=val4).exists():
                return render(request, 'BillInfo_address.html',
                              {'BillNo': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'BillTotal': val5,
                               'ClientBillDetails': BillDetails1, 'Buyproducts': BuyProducts1})
            else:
                return render(request, 'BillInfo.html',
                              {'BillNo': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'BillTotal': val5,
                               'ClientBillDetails': BillDetails1, 'Buyproducts': BuyProducts1})
        else:
            return redirect('index')
    else:
        return redirect('index')


def BillInfoaddress(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["BillNo"])
            val2 = int(request.POST["BClient_id"])
            val3 = request.POST["BClient_Name"]
            val4 = int(request.POST["BClient_Mobile"])
            val5 = request.POST["BillTotal"]
            val6 = str(request.POST["Add1"])
            val7 = str(request.POST["Add2"])
            val8 = str(request.POST["Add3"])
            val9 = int(request.POST["pincode"])
            ClientDetails_Info = Client_details(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                                Client_Add1=val6, Client_add2=val7, Client_add3=val8, Client_pin=val9)
            ClientDetails_Info.save()
            BuyProducts1 = BuyProducts.objects.filter(Client_name=val3, client_mobile=val4, randid=val2, Userdid=val1)
            BillDetails1 = BillDetails.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                                      TotalAmt=val5)
            return render(request, 'BillInfo.html',
                          {'BillNo': val1, 'userId1': val2, 'username': val3, 'userMobile': val4,
                           'ClientBillDetails': BillDetails1, 'Buyproducts': BuyProducts1})
        else:
            return redirect('index')


    else:
        return redirect('index')


def AdminLog(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            BillSum_count = BillDetails.objects.filter(BillCheck="").count()
            Payment_count = PaymentDone.objects.filter(DonePayment="").count()
            Done_count = PaymentDone.objects.filter(DonePayment="Done").count()
            return render(request, 'Adminpage.html',
                          {'count1': BillSum_count, 'count2': Payment_count, 'count3': Done_count})
        else:
            return redirect('index')

    else:
        return redirect('index')

def Billinglnfo(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            BillSum = BillDetails.objects.filter(BillCheck="")
            return render(request, 'BillDetails.html', {'BillInfo': BillSum})
        else:
            return redirect('index')
    else:
        return redirect('index')

def DoneBilling(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            PaymentPend = PaymentDone.objects.filter(DonePayment="")
            return render(request, 'PendingPayment.html', {'PaymentPending': PaymentPend})
        else:
            return redirect('index')
    else:
        return redirect('index')

def DoneList(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            PaymentPend = PaymentDone.objects.filter(DonePayment="Done")
            return render(request, 'DoneList.html', {'PaymentPending': PaymentPend})
        else:
            return redirect('index')

    else:
        return redirect('index')

def BillIDetailnfo(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["UserId"])
            val2 = int(request.POST["RandId"])
            val3 = request.POST["UserName"]
            val4 = int(request.POST["UserMobile"])
            val5 = request.POST["UserTotal"]
            val6 = request.POST["BillDAte"]
            Client_details_info = Client_details.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4)
            Billing1 = BuyProducts.objects.filter(Userdid=val1, randid=val2, Client_name=val3, client_mobile=val4)
            return render(request, 'Billing.html',
                          {'BillNo': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'BillTotal': val5,
                           'BillDate': val6, 'BillingDetail': Billing1,'cldetailinfo':Client_details_info})
        else:
            return redirect('index')
    else:
        return redirect('index')


def ConfBill(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["UserId"])
            val2 = int(request.POST["RandId"])
            val3 = request.POST["UserName"]
            val4 = int(request.POST["UserMobile"])
            val5 = request.POST["UserTotal"]
            a = BillDetails.objects.get(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4)
            a.BillCheck = "Done"
            a.save()
            BillConfirm_info = PaymentDone(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                           TotalAmt=val5)
            if not PaymentDone.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4,
                                              TotalAmt=val5).exists():
                BillConfirm_info.save()
            BillSum_count = BillDetails.objects.filter(BillCheck="").count()
            Payment_count = PaymentDone.objects.filter(DonePayment="").count()
            Done_count = PaymentDone.objects.filter(DonePayment="Done").count()
            return render(request, 'Adminpage.html',
                          {'count1': BillSum_count, 'count2': Payment_count, 'count3': Done_count})
        else:
            return redirect('index')
    else:
        return redirect('index')

def PaymentDetailnfo(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["UserId"])
            val2 = int(request.POST["RandId"])
            val3 = request.POST["UserName"]
            val4 = int(request.POST["UserMobile"])
            val5 = request.POST["UserTotal"]
            val6 = request.POST["BillConfdate"]
            Client_details_info = Client_details.objects.filter(Userid=val1, randId=val2, Client_name=val3,
                                                                client_mobile=val4)
            PaymentSum = PaymentDone.objects.filter(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4)
            Billing1 = BuyProducts.objects.filter(Userdid=val1, randid=val2, Client_name=val3, client_mobile=val4)
            return render(request, 'PaymentDetail.html',
                          {'BillNo': val1, 'userId1': val2, 'username': val3, 'userMobile': val4, 'BillTotal': val5,
                           'BillDate': val6, 'PaymentDetails': PaymentSum, 'BillDetail': Billing1,'cldetailinfo':Client_details_info})
        else:
            return redirect('index')
    else:
        return redirect('index')


def ConfPayment(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.POST["UserId"])
            val2 = int(request.POST["RandId"])
            val3 = request.POST["UserName"]
            val4 = int(request.POST["UserMobile"])
            val5 = request.POST["UserTotal"]
            a = PaymentDone.objects.get(Userid=val1, randId=val2, Client_name=val3, client_mobile=val4)
            a.DonePayment = "Done"
            a.save()
            BillSum_count = BillDetails.objects.filter(BillCheck="").count()
            Payment_count = PaymentDone.objects.filter(DonePayment="").count()
            Done_count = PaymentDone.objects.filter(DonePayment="Done").count()
            return render(request, 'Adminpage.html',
                          {'count1': BillSum_count, 'count2': Payment_count, 'count3': Done_count})
        else:
            return redirect('index')
    else:
        return redirect('index')

def Cart(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = request.GET["username"]
            val2 = int(request.GET["userMobile"])
            val3 = int(request.GET["userid1"])
            Clientdata = ClientDetailLog.objects.filter(Client_name=val1, client_mobile=val2, randid=val3)
            BuyProducts1 = BuyProducts.objects.filter(Client_name=val1, client_mobile=val2, randid=val3)
            return render(request, 'Cart.html',
                          {'username': val1, 'userMobile': val2, 'userId1': val3, 'Buyproducts': BuyProducts1,
                           'Clientdata1': Clientdata})
        else:
            return redirect('index')

    else:
        return redirect('index')

def History(request):

    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = request.GET["username"]
            val2 = int(request.GET["userMobile"])
            val3 = int(request.GET["userid1"])
            val4 = request.GET["Id"]
            val5 = int(request.GET["UId"])
            Billing1 = BuyProducts.objects.filter(randid=val5, Client_name=val1, client_mobile=val2)
            BillSum = BillDetails.objects.filter(Client_name=val1, client_mobile=val2)
            DonePay = PaymentDone.objects.filter(Client_name=val1, client_mobile=val2)
            BillSum_count = BillDetails.objects.filter(BillCheck="", Client_name=val1, client_mobile=val2).count()
            Done_count = PaymentDone.objects.filter(Client_name=val1, client_mobile=val2).count()
            return render(request, 'History.html',
                          {'username': val1, 'userMobile': val2, 'userId1': val3, 'Id1': val4, 'UId': val5,
                           'count1': BillSum_count,
                           'count2': Done_count, 'BillInfo': BillSum, 'BillingDetail': Billing1, 'DonePay1': DonePay})
        else:
            return redirect('index')
    else:
        return redirect('index')


def shopproduct(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.GET["id"])
            val2 = str(request.GET["Mod"])
            if val2 == 'Delete':
                DeleteList = Productinshop.objects.get(id=val1)
                DeleteList.delete()
            Shopproducts_all = Productinshop.objects.all()
            return render(request, 'Shopproduct.html', {'id': val1, 'Mod': val2, 'Shopproducts': Shopproducts_all})
        else:
            return redirect('index')

    else:
        return redirect('index')


def prdouctlist(request):
    if request.session.has_key('id2'):
        if 'id2' in request.session:
            id2 = request.session['id2']
            request.session.modified = True
            val1 = int(request.GET["id"])
            val2 = str(request.GET["Mod"])
            if val2 == 'Delete':
                DeleteList = Product.objects.get(id=val1)
                DeleteList.delete()
            Shopproducts_all = Productinshop.objects.all()
            Product_all = Product.objects.all()
            return render(request, 'prdouctlist.html',
                          {'id': val1, 'Mod': val2, 'Productall': Product_all, 'Shopproducts': Shopproducts_all})
        else:
            return redirect('index')

    else:
        return redirect('index')

def logout(request):
    del request.session['id2']
    return redirect('index')

def image1(request):
    if request.method == "POST":
        val1 = int(request.POST["id"])
        val2 = str(request.POST["Mod"])
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            Shopproducts_all = Productinshop.objects.all()
            Product_all = Product.objects.all()
            return render(request, 'prdouctlist.html',
                          {'id': val1, 'Mod': val2, 'Productall': Product_all, 'Shopproducts': Shopproducts_all})
def image2(request):
    if request.method == "POST":
        val1 = int(request.POST["id"])
        val2 = str(request.POST["Mod"])
        if val1 != 0:
            Editlist = Product.objects.get(id=val1)
            if len(request.FILES) !=0:
                if len(Editlist.image1) > 0:
                    os.remove(Editlist.image1.path)
                Editlist.image1 = request.FILES['image1']
                Editlist.Product_id = request.POST.get('Product_id')
                Editlist.name = request.POST.get('name')
                Editlist.price = request.POST.get('price')
                Editlist.stock = request.POST.get('stock')
                Editlist.image = request.POST.get('image')
                Editlist.save()
                Shopproducts_all = Productinshop.objects.all()
                Product_all = Product.objects.all()
                return render(request, 'prdouctlist.html',
                              {'id': val1, 'Mod': val2, 'Productall': Product_all, 'Shopproducts': Shopproducts_all})
def shopimage1(request):
    if request.method == "POST":
        val1 = int(request.POST["id"])
        val2 = str(request.POST["Mod"])
        if val1 != 0:
            Editshop = Productinshop.objects.get(id=val1)
            if len(request.FILES) !=0:
                Editshop.image1 = request.FILES['image1']
                Editshop.Product_id = request.POST.get('Product_id')
                Editshop.save()
        Shopproducts_all = Productinshop.objects.all()
        return render(request, 'Shopproduct.html', {'id': val1, 'Mod': val2, 'Shopproducts': Shopproducts_all})
def shopimage2(request):
    if request.method == "POST":
        val1 = int(request.POST["id"])
        val2 = str(request.POST["Mod"])
        form = ImageForm_shop(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
        Shopproducts_all = Productinshop.objects.all()
        return render(request, 'Shopproduct.html', {'id': val1, 'Mod': val2, 'Shopproducts': Shopproducts_all})



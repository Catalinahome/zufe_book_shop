from django.db import models
import datetime


# 创建购物车模型
class t_cart(models.Model):
    cart_uid = models.IntegerField()
    cart_bid = models.IntegerField()
    cart_num = models.IntegerField()
    cart_time = models.DateTimeField(auto_now_add=True)


# 创建购物车模型
class v_cart(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(null=False, max_length=20)
    book_pic = models.ImageField(upload_to='static/book_images/')
    book_price = models.FloatField()
    cart_uid = models.IntegerField()
    cart_bid = models.IntegerField()
    cart_num = models.IntegerField()

    class Meta:
        app_label = "cart"
        managed = False  # django不管理该model的生成和销毁。
        db_table = "cart_book_view"  # 指定视图名称


# 增加一条购物车记录的方法
def add_cart(uid, bid, num):
    mycart = t_cart.objects.create(cart_uid=uid, cart_bid=bid, cart_num=num)
    mycart.save()


# 通过uid查询购物车记录的方法
def get_cart_by_user(uid):
    mycart = v_cart.objects.filter(cart_uid=uid)
    return mycart


# 通过tid查询购物车记录的方法
def get_cart_by_list(tid):
    order_list = v_cart.objects.filter(id=tid)
    return order_list


# 查询是否存在
def get_cart_by_user_book(uid, bid):
    return t_cart.objects.filter(cart_uid=uid, cart_bid=bid).exists()


# 更新数量
def update_cart_by_book(uid, bid, num):
    cartitem = t_cart.objects.get(cart_uid=uid, cart_bid=bid)
    cartitem.cart_num += int(num)
    cartitem.save()


# 删除购物车
def delete_cart_by_id(cid):
    t_cart.objects.get(id=cid).delete()


# 创建order模型
class t_order(models.Model):
    order_uid = models.IntegerField(default=0)
    order_name = models.CharField(max_length=30)
    order_address = models.CharField(max_length=100)
    order_tel = models.CharField(max_length=20)
    order_payment = models.CharField(max_length=10)
    order_status = models.CharField(max_length=10)
    order_time = models.DateTimeField(auto_now_add=True)
    order_valid = models.BooleanField()

    def __str__(self):
        return self.order_name + '[' + datetime.datetime.strftime(self.order_time, '%Y-%m-%d %H:%M:%S') + ']'


# 添加订单信息
def add_order(uid, name, add, tel, pay):
    myorder = t_order.objects.create(order_uid=uid, order_name=name, order_address=add,
                                     order_tel=tel, order_payment=pay, order_status='已下单', order_valid=True)
    myorder.save()


# 获取最新的订单id
def get_id_by_user(uid):
    order_list = t_order.objects.filter(order_uid=uid).latest('id')
    return order_list.id


# 创建orderitem模型
class t_orderitem(models.Model):
    order_oid = models.IntegerField()
    order_bid = models.IntegerField()
    order_num = models.IntegerField()


# 增加orderitem的方法
def add_orderitem(oid, bid, num):
    myorderitem = t_orderitem.objects.create(order_oid=oid, order_bid=bid, order_num=num)
    myorderitem.save()

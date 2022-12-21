from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.views.decorators.csrf import csrf_protect


# 加入购物车函数
def add_to_cart(request):
    user_id = request.session.get('uid', 0)
    books_id = request.GET['bid']
    number = request.GET['num']
    # 记录已存在
    if get_cart_by_user_book(user_id, books_id):
        update_cart_by_book(user_id, books_id, number)
    else:
        add_cart(user_id, books_id, number)
    return HttpResponse('成功加入购物车！')


# 查看购物车函数
@csrf_protect
def get_cart(request):
    user_id = request.session.get('uid', 0)
    username = request.session.get('user', 0)
    cart = get_cart_by_user(user_id)
    return render(request, 'cart/cart.html', {
        'cartinfo': cart,
        'user': username,
    })


# 删除购物车函数
def delete_cart(request):
    cart_id = request.GET['cid']
    delete_cart_by_id(cart_id)
    return redirect('/cart/')


# 返回订单数据渲染订单确认前端页面
@csrf_protect
def conforder(request):
    clist = request.POST.getlist('sel', 0)  # 获取下单的商品编号（购物车id）
    cart_list = get_cart_by_list(clist)  # 获取购物车记录
    num = sum = 0  # 统计下单商品总数量及总金额
    blist = nlist = []  # 记录商品编号及数量
    for c in cart_list:
        num += c.cart_num
        sum += c.cart_num * c.book_price
        blist.append(c.cart_bid)
        nlist.append(c.cart_num)

    return render(request, 'cart/orderconfirm.html', {
        'cartlist': cart_list, 'num': num, 'sum': sum, 'clist': clist, 'blist': blist, 'nlist': nlist,
    })


# 提交订单函数
@csrf_protect
def finalorder(request):
    uid = request.session.get('uid', 0)
    clist = eval(request.POST['clist'])  # 购物购物车项目列表
    blist = eval(request.POST['blist'])  # 商品id列表
    nlist = eval(request.POST['nlist'])  # 商品数量列表
    rname = request.POST['recname']
    addr = request.POST['address']
    tel = request.POST['tel']
    pay = request.POST['payment']
    add_order(uid, rname, addr, tel, pay)  # 添加新订单
    oid = get_id_by_user(uid)  # 获取订单id
    for i, b in enumerate(blist):  # 添加订单项目商品id列表
        add_orderitem(oid, b, nlist[i])
    try:
        for c in clist:  # 删除购物车项目
            delete_cart_by_id(c)
    except:
        pass
    return redirect('/index/')

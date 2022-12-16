from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import authenticate
from .models import add_user, check_uname

# Create your views here.


class loginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码')


def login(request):
    if request.method == 'POST':
        loginform = loginForm(request.POST)
        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is not None:
            request.session['user'] = username = user.get_username()
            request.session['uid'] = user.id
            return redirect('/index/')
        msg = '用户名或密码错误！'
    else:
        user = request.session.get('user', '')
        loginform = loginForm()
        msg = '请登录！'
    username = request.session.get('user', '')

    return render(request, 'user/login.html', {'form': loginform, 'msg': msg, 'user': user, 'uname': username})


def logout(request):
    request.session.clear()
    return redirect('/index/')


class regForm(forms.Form):
    username = forms.CharField(label='用户名', label_suffix='：', initial='username', help_text='必填',
                               error_messages={'required': '必须提供username'})
    password = forms.CharField(label='密码', label_suffix='：', widget=forms.PasswordInput, help_text='包含大小写字母、数字和特殊符号')
    email = forms.CharField(label='邮箱', label_suffix='：', initial='email@server', widget=forms.EmailInput,
                            help_text='要符合email格式')
    gen_option = [('1', 'male'), ('2', 'female')]
    gender = forms.ChoiceField(label='性别', widget=forms.RadioSelect, choices=gen_option, required=False)
    occ_option = [('1', '公务人员'), ('2', '专业技术人员'), ('3', '办事人员'), ('4', '商业服务业人员'), ('5', '农林牧渔从业人员'), ('6', '生产运输从业人员'),
                  ('7', '军人'), ('8', '其他从业人员')]
    occupation = forms.ChoiceField(label='职业', widget=forms.Select, choices=occ_option, required=False)
    salary = forms.IntegerField(label='薪资', widget=forms.NumberInput, required=False)
    prov_option = [('1', '北京'), ('2', '天津'), ('3', '上海'), ('4', '重庆'), ('5', '浙江'), ('6', '江苏'), ('7', '四川'),
                   ('8', '湖南'), ('9', '河北'), ('10', '山东')]
    place = forms.ChoiceField(label='生源地', widget=forms.Select, choices=prov_option, required=False)
    hob_option = [('1', '政治'), ('2', '军事'), ('3', '科技'), ('4', '财经'), ('5', '体育'), ('6', '娱乐'), ('7', '教育'),
                  ('8', '社会')]
    hobby = forms.MultipleChoiceField(label='兴趣爱好', required=False, widget=forms.CheckboxSelectMultiple,
                                      choices=hob_option)
    logo = forms.ImageField(label='头像', required=False)
    profile = forms.CharField(label='简介', widget=forms.Textarea, required=False)


def register(request):
    if request.method == 'POST':
        regform = regForm(request.POST)
        if not check_uname(uname=request.POST['username']):
            add_user(uname=request.POST['username'], upass=request.POST['password'], uemail=request.POST['email'])
            return redirect('/index/')
        else:
            msg = '用户名已存在！'
    else:
        regform = regForm()
        msg = '请输入基本信息！'
    return render(request, 'user/register.html', {
        'form': regform,
        'msg': msg,
    })



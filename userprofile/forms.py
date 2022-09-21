# 引入表单类
from django import forms
# 引入 User 模型
from django.contrib.auth.models import User
# 引入 Profile 模型
from .models import Profile


# 登录表单，继承了 forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    # 复写 User 的密码
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data = self.cleaned_data
        print(f'password: {data.get("passoword")}\npassword2: {data.get("password2")}')
        if data.get('password') == data.get('password2'):
            return data.get('passoword')
        else:
            raise forms.ValidationError("密码输入不一致，请重试！")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')

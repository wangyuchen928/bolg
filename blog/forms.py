from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    # email 和 to 两个字段要获取两个正确的邮箱地址 否则会抛出 forms.ValidationError 异常 并且对应的表单将不会验证
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 显示用户需要填写的字段
        fields = ('name', 'email', 'body')

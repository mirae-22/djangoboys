from django import forms
from .models import Post
# PostForm : 만들 폼의 이름(Post Model과 연결되는 폼이다.)
# forms.ModelForm은 ModelForm이라는 것을 알려주는 구문


class PostForm(forms.ModelForm):
    # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문
    class Meta: # PostForm과 관련된 정보 설정
        model = Post # Post 모델과 연결된다.
        fields = ('title', 'text',) # 이 폼에 나타낼 필드를 지정
from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        '''
        fields = [
            'title',
            'content'] 
        이거는 특정 필드만 선택할 때

        exclude = [
            '뭐시기',
            '뭐시기기']
        이거는 특정 필드만 제외할 때
        '''
        fields = [
            'title',
            'content',
            'image',
        ]
        labels = {
            'title': ('제목'),
            'content': ('내용'),
            'image': ('이미지'),
        }
        help_texts = {
            'title': ('제목을 입력하세용.'),
            'content': ('내용을 입력하세용.'),
        }


def save(self, **kwargs):
        post = super().save(commit=False) # Views.py에서 작성자 데이터도 입력된 다음에 save()가 돼야하므로 commit=False (commit은 DB에 곧바로 저장한다는 뜻)
        post.writer = kwargs.get('user', None)
        post.save()
        return post
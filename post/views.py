from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Post

# Create your views here.
def post_list(request):
    return render(request, 'post/post_list.html')


def create_post(request):

    if request.method == 'POST':
        post = Post.objects.create( #post 객체 생성
            title = request.POST.get('title'), # 폼에서 title 가져와서 title 변수에 저장
            content = request.POST.get('content') 
        )
        return redirect(reverse('detail_post', args=[post.pk])) #detail_post에 pk를 같이 넘기면서 리다이렉트
    return render(request, 'post/create_post.html')

def detail_post(request, pk):
    detail_post = Post.objects.get(id=pk) #pk가 일치한 게시물 객체를 불러온뒤 detail_post 변수에 저장

    context={
        'detail_post': detail_post 
    }

    return render(request, 'post/detail_post.html', context) # context = detail_post 정보, Context는 확장성을 위한것임

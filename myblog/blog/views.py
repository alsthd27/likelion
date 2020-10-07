from django.shortcuts import render # "django.shortcuts 패키지에 있는 render 함수를 사용하로독 하겄따잉!"

def main(request): # "이걸 main이라는 함수로 명명하겠다! request를 인자로 받는다!"
    return render(request, 'blog/main.html') # "render 함수를 활용해 request를 blog/main.html으로 return하겠다!"
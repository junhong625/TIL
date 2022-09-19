# Django Form

> 데이터에 대한 유효성 검증 과정을 단순화하고 자동화 할 수 있게 만들어 주는 도구
> 
- Django 서버에 들어오는 요청 중에 비정상적인 혹은 악의적인 요청이 있다는 것을 생각해야 함
- 그렇기에 원하는 데이터 형식이 맞는지에 대한 유효성 검증이 반드시 필요
- 일반적인 유효성 검증 과정은 복잡하고 생산성을 떨어뜨림

## Django는 Form에 관련된 작업의 세 부분을 처리

1. 렌더링을 위한 데이터 준비 및 재구성
2. 데이터에 대한 HTML forms 생성
3. 클라이언트로부터 받은 데이터 수신 및 처리

## Django Form Class

### Form Class 선언

- model 클래스와 마찬가지로 상속을 통해 선언
    - 앱 폴더에 `forms.py`를 생성
        - `forms.py`에 Form Class를 작성하는 것은 규약이 아님
        하지만 더 나은 유지 보수의 관점에서 `forms.py`안에 작성하는 것이 효율적
        - 사용자로부터 받을 input만 설정
        
        ### forms.py
        
        ```python
        # 앱/forms.py
        
        from django import forms
        
        class ArticleForm(forms.Form):
            title = forms.CharField(max_length=10) # 각 필드 설정
            content = forms.CharField()
        ```
        
        ### views.py
        
        ```python
        # 앱/views.py
        
        from .......
        from .forms import ArticleForm
        
        def new(request):
            form = ArticleForm() # 생성한 ModelForm클래스인 ArticleForm을 form에 할당 -> 즉, 내가 설정해둔 form을 그대로 가져옴
            context = {
                'form': form,
            }
            return render(request, 'articles/new.html', context)
        ```
        
        ### new.html
        
        ```python
        # 앱/articles/new.html
        
        {% extends 'base.html' %}
        
        {% block content %}
          <h1>NEW</h1>
          <form action="{% url 'articles:create' %}" method="POST">
            {% csrf_token %}
            {{ form.as_p }} # as_p를 통해 각 field를 p태그로 감싸기
            <input type="submit">
          </form>
          <hr>
          <a href="{% url 'articles:index' %}">뒤로가기</a>
        {% endblock content %}
        ```
        

### From Rendering option

> <label> & <input> 쌍에 대한 출력 옵션
> 
1. `as_p()`
    - 각 필드가 `<p>` 태그로 감싸져서 렌더링
2. `as_ul()`
    - 각 필드가 `<li>` 태그로 감싸져서 렌더링
    - `<ul>` 태그는 직접 작성
3. `as_table()`
    - 각 필드가 `<tr>` 태그로 감싸져서 렌더링

## Django의 2가지 HTML input 표현

### Form fields

- 입력에 대한 유효성 검사 로직을 처리
- 템플릿에서 직접 사용

### Widgets

- 웹 페이지의 HTML input 요소 렌더링을 담당
    - input 요소의 단순한 출력 부분을 담당
- Widgets은 반드시 form fields에 할당

# Widget

> 단순히 HTML 렌더링을 처리하며 유효성 검증과 관계 X
> 
- 예시
    
    ```python
    # 앱/forms.py
    
    from django import forms
    
    class ArticleForm(forms.Form):
    		NATION_A = 'kr'
    		NATION_B = 'ch'
    		NATION_C = 'jp'
    		NATION_CHOICES = [
    				(NATION_A , '한국'),
    				(NATION_B , '중국'),
    				(NATION_C , '일본'),
    		]
    		title = forms.CharField(max_length=10)
    		content = forms.CharField(widget=forms.Textarea)
    		nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
    ```
    
    - Django에서 `choices`를 사용하게 된다면 위와 같은 구조로 작성하길 권장하고 있음

# ModelForm

> 생성한 Model 클래스의 필드를 가져와 알맞게 Form을 생성해주는 클래스
> 
- ModelForm은 Form과 마찬가지로 views.py에서 사용

## ModelForm선언

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속
- 정의한 ModelForm 클래스 안에 Meta 클래스 선언
    - Meta 클래스를 통해 기반이 될 model을 지정
        - `__all__` 을 통해서 (입력 받아야 하는)모든 필드를 fields에 할당 가능
        - `exclude`  에 필드를 지정하여 해당 필드만 제외할 수 있음
        - fields와 exclude를 함께 사용하는 것은 권장하지 않음
- 예시)
    
    ```python
    # 앱/forms.py
    
    from django import forms
    from .modles import Article
    
    class ArticleForm(forms.ModelForm):
    		
    		class Meta:
    				model = Article # 반환 값이 아닌 참조 값을 할당하고 있음
    				fields = '__all__'
    				# exclude = ('title',)
    ```
    
    ### 참조 값
    
    ```python
    def greeting():
    		return '안녕하세요'
    # 참조
    print(greeting) # <function greeting at 0x00000240AEA63E20> 
    # 호출
    print(greeting()) # 안녕하세요 
    ```
    
    - 참조 값
        - 함수를 호출하지 않고 함수 자체를 전달하여 다른 함수에서 “**필요한 시점**”에 호출하는 경우
            - 예시)
                
                ```python
                # 앱/urls.py 중
                
                urlpatterns = [
                		path('', views.index, name='index'),
                ]
                ```
                
                - 이와 같이 views의 index 함수의 참조 값을 그대로 넘김으로써 필요한 시점에 index함수를 사용하도록 할 수 있음

## ModelForm 사용 시 주의 사항

- Meta클래스가 내부에 있다? 즉, 파이썬의 Inner Class, Nested Class인가? 라고 문법적으로 접근 X
- 단순히 ModelForm에서 설계를 할 시 Meta라는 이름의 내부 클래스에 모델 정보를 저장하도록 설계했을 뿐 문법적으로 접근해서는 안됨

## ModelForm으로 인한 views.py의 변화

- 기존에는 일일이 model에 형태에 맞게 변수에 할당하고 model클래스에 인수로 집어넣어 db에  반영했던 것을 form을 통해 간단한 코드로 db에 반영 가능
- 매우 복잡한 유효성 검사를  ModelForm에 기반한 `is_valid()` 함수를 통해 간단하게 유효성 검사가 가능

### Create

```python
# 앱/views.py

from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST) # POST로 받은 데이터를 form클래스에 인수로 집어넣어 데이터가 반영된 form 인스턴스 생성
    if form.is_valid(): # 유효성 검사 실시
        article = form.save() # 유효성 검사 통과 시 DB에 저장
        return redirect('articles:detail', article.pk) # 저장된 페이지로 이동
    return redirect('articles:new') # 유효성 검사 실패 시 다시 현재 페이지로 이동
```

- `reqeust.POST`
    - 사용자가 form을 통해 전송한 데이터
- `is_valid()`
    - 유효성 검사를 실행하고 데이터가 유효한지 boolean으로 반환
    - 반환 값이 `False`인 경우 `form`인스턴스의 `errors` 속성에 유효성 검사를 실패한 원인이 딕셔너리 형태로 저장됨
    - 이를 활용하여 아래와 같이 `context`에 `form`을 저장하여 render로 `context`를 html에 전달하면 오류 메세지를 출력 할 수 있음
        
        ```python
        # 앱/views.py
        
        def create(request):
            form = ArticleForm(request.POST) # POST로 받은 데이터를 form클래스에 인수로 집어넣어 데이터가 반영된 form 인스턴스 생성
            if form.is_valid(): # 유효성 검사 실시
                article = form.save() # 유효성 검사 통과 시 DB에 저장
                return redirect('articles:detail', article.pk) # 저장된 페이지로 이동
            context = {
                'form':form
            }
            return render(request, 'articles/new.html', context)
        ```
        
- `save()`
    - form 인스턴스에 바인딩(할당)된 데이터를 통해 데이터베이스 객체를 만들고 저장
    - ModelForm의 하위 클래스(ModelForm을 상속받아 생성한 클래스 `ArticleForm`)의 키워드 인자 `instance`여부를 통해 생성, 수정이 결정됨
        - `instance`에 data를 할당 시 수정
        - `instance`에 data를 할당하지 않을 시 생성

### UPDATE

```python
# 앱/views.py

from .models import Article
from .forms import ArticleForm

def edit(request, pk):
		article = Article.objects.get(pk=pk) # Article model에서 pk에 해당하는 데이터를 가져와 article에 할당
		form = ArticleForm(instance = article) # article에 저장한 데이터를 form클래스의 instance 인수로 집어넣어 데이터가 반영된 form 인스턴스 생성
																					 # instance에 article을 할당하지 않으면 기존의 데이터가 form에 할당되지 않아 edit페이지에서 빈 form만 보여짐
		context = { # context에 article과 form dictionary형태로 저장
				'article':article,
				'form':form,
		}
		return render(requset, 'articles/edit.html', context) # templates/articles/edit.html에 context 전송
```

```html
# templates/앱/edit.html

{% extends 'base.html' %}

{% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a>
{% endblock content %}
```

```python
# 앱/views.py

from .models import Article
from .forms import ArticleForm

def update(request, pk):
    article = Article.objects.get(pk=pk) # Article model에서 pk에 해당하는 데이터를 가져와 article에 할당
    form = ArticleForm(request.POST, instance=article) # article의 데이터를 requset.POST의 데이터로 덮어씌움
    if form.is_valid(): # 유효성 검사
        form.save() # 유효성 검사 통과 시 저장
		    return redirect('articles:detail', article.pk) # 수정 완료 후 해당 페이지로 이동
		context = { # 유효성 검사 실패 시 실패 이유를 담은 form과 article을 context에 저장
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context) # 실패 시 다시 update페이지로 이동하며 context를 전송
```

- `reqeust.POST`
    - 사용자가 form을 통해 전송한 데이터

## Form과 ModelForm

> ModelForm이 Form보다 더 좋은 것이 아니라 각자 역할이 다름
> 

### Form

- 사용자로부터 받는 데이터가 DB와 연관되어 있지 않는 경우에 사용
- DB에 영향을 미치지 않고 단순 데이터만 사용
    - 예시 - 로그인

### ModelForm

- 사용자로부터 받는 데이터가 DB와 연관되어 있는 경우에 사용
- 데이터의 유효성 검사가 끝나면 데이터를 어떤 레코드에 맵핑해야 할지 알고 있기에 save()호출이 가능

## Widgets

> 유효 검사에는 전혀 영향을 주지 않고 렌더에 영향을 주는 속성
> 
- 필요한 arguments는 필요 시에 공식 문서를 참조하여 작성

### 위젯 작성 방법

> Django에서는 첫 번째 방법을 권장
> 
- 첫 번째 방법
    
    ```python
    # 앱/models.py
    
    from django import forms
    from .models import Article
    
    class ArticleForm(forms.ModelForm):
        title = forms.CharField( 
            label='제목',
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title', 
                    'placeholder': 'Enter the title',
                    'maxlength': 10,
                }
            )
        )
    		class Meta:
    				model = Article
    				fields = '__all__'
    ```
    
- 두 번째 방법

    ```python
    # 앱/models.py

    from django import forms
    from .models import Article

    class ArticleForm(forms.ModelForm):
            
            class Meta:
                    model = Article
                    fields = '__all__'
                    widget= {
                            'title': forms.TextInput(attrs={
                                    'class': 'my-title', 
                                    'placeholder': 'Enter the title',
                                    'maxlength': 10,
                                }
                            )
                        }
    ```

## HTTP request에 따른 view 함수 구조 변화

> views.py 내의 new-create, edit-update에는 공통점과 차이점이 존재
> 

### 공통점

- new-create는 모두 CREATE 로직을 구현하기 위한 공통 목적
- edit-update는 모두 UPDATE로직을 구현하기 위한 공통 목적

### 차이점

- new와 edit은 GET요청에 대한 처리
- create와 update는 POST요청에 대한 처리

> 이 공통점과 차이점을 기반으로 views.py에서 method에 따라 로직이 분리 되도록 변경
> 

### Create(+new)

```python
# 앱/views.py

def create(request):
    if request.method == 'POST': # 요청이 POST일 경우 -> CREATE
        form = ArticleForm(request.POST) #  form 변수에 데이터를 입력받은 ArticleForm 할당
        if form.is_valid(): # 유효성 검사
            article = form.save() # 유효성 검사 통과시 form저장
            return redirect('articles:detail', article.pk) # 저장한 페이지의 detail로 이동
    else: # 요청이 GET일 경우 -> NEW
        form = ArticleForm() # form 변수에 데이터가 빈 ArticleForm 할당
    context = { # 요청에 맞게 저장된 form을 context에 저장
        'form' : form
    }
    return render(request, 'articles/create.html', context) # create.html에 context전달
```

### Update(+edit)

```python
# 앱/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk) # article 변수에 pk에 해당하는 데이터 가져와서 할당
    if request.method == 'POST': # 요청이 POST일 경우 -> UPDATE
        form = ArticleForm(request.POST, instance=article) # form 변수에 article의 데이터를 POST로 받은 데이터로 덮어 씌운 ArticleForm을 할당
        if form.is_valid(): # 유효성 검사
            form.save() # 유효성 검사 통과 시 데이터베이스에 반영
            return redirect('articles:detail', article.pk) # 저장한 페이지의 detail로 이동
    else: # 요청이 GET일 경우 -> EDIT
        form = ArticleForm(instance=article) # form 변수에 article의 데이터 반영되어 있는 ArticleForm을 할당
    context = { # 각 요청에 맞게 저장된 form을 article과 함께 context에 저장
        'article': article,
        'form' : form
    }
    return render(request, 'articles/update.html', context) # update.html에 context를 전달
```

> 코드의 간결화와 유효성 검사를 실패했을 시에 반환하는 `form`을 `context`에 할당하기 위해 `context`에 대한 indentation을 `if`, `else`와 같은 라인에 위치
> 

### urls.py

```python
from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.create, name='new'), # new함수 필요 X 
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'), # edit함수 필요 X 
    path('<int:pk>/update/', views.update, name='update'),
]
```

### new.html → create.html로 이름 변경

```python
# templates/앱/create.html

{% extends 'base.html' %}
{% load bootstrap5 %}

{% block content %}
    <h1>CREATE</h1>
    <form action="{% url 'articles:create' %}" method="POST"> # articles urls.py의 create로 전송
        {% csrf_token %} # POST요청을 위한 토큰
        {{ form.as_p }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a> # articles urls.py의 index로 이동
{% endblock content %}
```

### edit.html → update.html로 이름 변경

```python
{% extends 'base.html' %}

{% block content %}
    <h1>UPDATE</h1>
    <form action="{% url 'articles:update' article.pk %}" method="POST"> # articles urls.py의 article.pk와 update로 전송
        {% csrf_token %} # POST요청을 위한 토큰
        {{ form.as_p }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">BACK</a> # articles urls.py의 index로 이동
{% endblock content %}
```

# View Decorators

## 데코레이터(Decorator)

> 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
> 
- Django는 다양한 HTTP 기능을 지원하기 위해 views.py 내의 함수에 적용할 수 있는 여러 데코레이터를 제공
- HTTP decorator 메서드 목록
    - `require_http_methods()` ****
        - 특정한 요청 method만 허용하도록 하는 데코레이터
    - `require_POST()`
        - POST 요청 method만 허용하도록 하는 데코레이터
    - `require_safe()`
        - GET 요청 method만 허용하도록 하는 데코레이터
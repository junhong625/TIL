# Django_REST API

# HTTP

> HyperText Transfer Protocol
> 
- HTML 문서와 같은 리소스(resource, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
- 웹 상에서 컨텐츠를 전송하기 위한 약속
- 웹에서 이루어지는 모든 데이터 교환의 기초가 됨
- “클라이언트 - 서버 프로토콜”이라고도 부름
- 클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통시
    - 요청(request)
        - 클라이언트에 의해 전송되는 메시지
    - 응답(response)
        - 서버에서 응답으로 전송되는 메시지

## HTTP 특징

### Stateless(무상태)

- 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
- 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
- 이는 특정 페이지와 일관되게 상호작용 하려는 사용자에게 문제를 야기
    - 쿠키와 세션을 사용하여 해결이 가능

### HTTP Request Methods

1. GET
- 서버에 리소스의 표현을 요청
- 데이터 검색
1. POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태 변경
1. PUT
- 요청한 주소의 리소스를 수정
1. DELETE
- 지정된 리소스를 삭제

### HTTP response status codes

> 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
> 
1. Informational responses(100-199)
2. Successful responses(200-299)
3. Redirection messages(300-399)
4. Client error responses(400-499)
5. Server error responses(500-599)

### URI

> Uniform Resource Identifier(통합 자원 식별자)
> 
- 인터넷에서 하나의 리소스를 가리키는 문자열
- 가장 일반적인 URI는 웹 주소로 알려진 URL
- URN
    - 특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 URN

### URL

> Uniform Resource Locator(통합 자원 위치)
> 
- 웹에서 주어진 리소스의 주소
- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
    - 리소스 : HTML, CSS, 이미지 등이 될 수 있음

### URL의 구조

- Scheme(or protocol)
    - 브라우저가 리소스를 요청하는데 사용해야 하는 프로토콜
    - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
    - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기 위한 `mailto:`,
    파일을 전송하기 위한 `ftp:` 등 다른 프로토콜도 존재
- Authority
    - Scheme 다음은 문자 패턴 `://`으로 구분된 Authority(권한)이 작성됨
    - Authority는 domain과 port를 모두 포함하며 둘은 `:`(콜론)으로 구분됨
    1. Domain Name
        - 요청 중인 웹 서버를 나타냄
        - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능
        - 하지만, IP 주소를 사람이 외우기 어렵기 때문에 Domain Name으로 사용
    2. Port
        - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
        - HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능
            - HTTP - 80
            - HTTPS - 443
        - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음
- Path
    - 웹 서버의 리소스 경로
    - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 
    오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현
- Parameters
    - 웹 서버에 제공하는 추가적인 데이터
    - 파라미터는 `&` 기호로 구분되는 key-value 쌍 목록
    - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
- Anchor
    - 리소스의 다른 부분에 대한 앵커
    - 리소스 내부 일종의 “북마크”를 나타내며 브라우저에 대한 해당 북마크 지점에 있는 콘텐츠를 표시
        - 예를 들어 HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤 함
    - fragment identifier(부분 식별자)라고 부르는 `#` 이후 부분은 서버에 전송되지 않음
    

### 요약

- 자원의 식별자(URI)
    - 자원의 위치로 식별(URL)
    - 자원의 이름으로 식별(URN)

## API

> Application Programming Interface
> 
- 애플리케이션과 프로그래밍으로 소통하는 방법
    - 개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
- API를 제공하는 애플리케이션과 다른 소프트웨어 및 하드웨어 등의 것들 사이의 간단한 계약(인터페이스)이라고 볼 수 있음
- API는 복잡한 코드를 추상화하여 쉽게 사용 가능한 구문을 제공

### WEB API

> 웹 서버 또는 웹 브라우저를 위한 API
> 
- 현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
- 대표적인 Third Party Open API 서비스 목록
    - Youtube API
    - Naver Papago API
    - Kakao Map API
- API는 다양한 타입의 데이터를 응답
    - HTML, XML, JSON 등

### REST(Representational State Transfer)

> 자원을 정의하고 자원에 대한 주소를 지정하는 방법의 모음
> 
- API server를 개발하기 위한 일종의 소프트웨어 설계 방법론
    - 2000년 로이 필딩이 설게
- RESTful : REST의 원리를 따르는 시스템
- REST의 기본 아이디어는 리소스 즉, 자원
    - 자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술

### REST에서의 자원 정의 및 주소 지정

1. 자원의 식별 
- **URL**
1. 자원의 행위
- **HTTP Method**
1. 자원의 표현
- 자원과 행위를 통해 궁극적으로 표현되는 결과물
- **JSON**으로 표현된 데이터를 제공

### JSON

> JavaScript의 표기법을 따른 단순 문자열
> 
- 파이썬의 dictionary, 자바스크립트의 object처럼 C계열의 언어가 갖고 있는 자료구조로 쉽게 변환할 수 있는 key-value 형태의 구조를 갖고 있음
- 사람이 읽고 쓰기 쉽고 기계가 파싱(해석&분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입

# Response JSON

### 4가지 방법으로 JSON 데이터 응답

1. HTML 응답
2. `JsonResponse()`를 사용한 JSON 응답
3. Django Serializer를 사용한 JSON 응답
4. Django REST framework를 사용한 JSON 응답

### 1. HTML 응답

- 문서(HTML) 한 장을 응답하는 서버 확인
- Content-type
    - 리소스의 media type을 나타내기 위해 사용
    - 실제 컨텐츠의 유형 확인 가능
    
    ```python
    def article_html(request):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'articles/article.html', context)
    ```
    

### 2. JsonResponse()를 사용한 JSON 응답

- `JsonResponse()`
    - JSON-encoded response를 만드는 클래스
    - `safe` parameter
        - 기본 값 True(dict 인스턴스만 허용)
        - False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
    
    ```python
    from django.http.response import JsonResponse, HttpResponse
    
    def article_json_1(request):
        articles = Article.objects.all()
        articles_json = []
    
        for article in articles:
            articles_json.append(
                {
                    'id': article.pk,
                    'title': article.title,
                    'content': article.content,
                    'created_at': article.created_at,
                    'updated_at': article.updated_at
                }
            )
        return JsonResponse(articles_json, safe=False)
    ```
    

### 3. Django Serializer를 사용한 JSON 응답

- `Serialization`
    - 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고,
    나중에 재구성할 수 있는 포맷으로 변환하는 과정
        - 즉, 어떠한 언어나 환경에서도 **나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정**
    - 변환 포맷은 대표적으로 json, xml, yaml이 있으며 json이 가장 보편적
    
    ```python
    from django.http.response import JsonResponse, HttpResponse
    from django.core import serializers
    
    def article_json_2(request):
        articles = Article.objects.all()
        data = serializers.serialize('json', articles)
        return HttpResponse(data, content_type='application/json')
    ```
    

### 4. Django REST framework를 사용한 JSON 응답

- Django REST framework(DRF)
    - DRF 사용을 위해서는 설치가 필요
        
        ```bash
        pip install djangorestframework
        ```
        
        - 이후 settings.py에 등록
            
            ```bash
            INSTALLED_APPS = [
            	...,
            	'rest_framework',
            	...,
            ]
            ```
            
    - Django에서 Resful API서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
    - Web API 구축을 위한 강력한 toolkit을 제공
    - REST framework를 작성하기 위한 여러 기능을 제공
    - DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
    
    ```python
    # 앱/serializers.py
    
    from rest_framework import serializers
    from .models import Article
    
    class ArticleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Article
            fields = '__all__'
    ```
    
    ```python
    # 앱/views.py
    from .serializers import ArticleSerializer
    
    @api_view()
    def article_json_3(request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    ```
    

## ModelSerializer

> 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
> 
1. Model 정보에 맞춰 자동으로 필드를 생성
2. serializer에 대한 유효성 검사기를 자동으로 생성(`is_valid()`)
3. `.create()` 및 `.update()` 의 간단한 기본 구현이 포함

### ModelSerializer 작성

- 앱/serializers.py 생성
    - serializers.py의 위치나 파일명은 자유

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```

### shell_plus에서 구조 및 동작 확인

- shell_plus 실행

```python
python manage.py shell_plus
```

- 인스턴스 구조 확인
    - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 할 때는 `many=True` 옵션 필수!

```bash
>> from articles.serializers import ArticleListSerializer
>> serializer = ArticleListSerializer()
>> serializer
ArticleListSerializer():
	id = IntegerField(label='ID', read_only=True)
	title = CharField(max_length=10)
	content = CharField(style={'base_template': 'textarea.html'})

## 단일 모델
>> article = Article.objects.get(pk=1)
>> serializer = ArticleListSerializer(article)
>> serializer.data
{'id':1, 'title': 'Site economic if two country science.' ...}

## QuerySet 모델
>> articles = Article.objects.all()
>> serializer = ArticleListSerializer(articles, many=True)
>> serializer.data
[OrderedDict([('id', 1), ('title', 'Live left research.'), ('content', 'Small drive until back board drive...]'
```

# Build RESTful API - Article

## GET-List

> 게시글 데이터 목록 조회
> 
- DRF에서 `api_view` 데코레이터 작성은 필수

### urls.py

```python
# 앱/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]
```

### views.py

- `api_view` decorator
    - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
    - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

```python
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```

## GET - Detail

> 단일 게시글 데이터 조회
> 
- 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

### serializers.py

```python
# 앱/serializers.py

class ArticleSerializer(serializers.ModelSerializer):

	class Meta:
		model = Article
		fields = '__all__'
```

## POST

> 게시글 데이터 생성하기
> 
- 요청에 대한 데이터 생성이 성공했을 경우는 `201 Created` 상태 코드를 응답하고 실패 했을 경우는 `400 Bad request`를 응답
    - `400 Bad request` 는 유효성 검사 시 `raise_exception=True` 을 통해 생략이 가능하다.
- rest_framework의 status를 import하여 간단하게 모든 상태 코드를 불러올 수 있다.
- form을 사용할 때와 똑같은 구조로 serialize를 가능
    1. data를 serialize작업(`request.POST`가 아닌 `request.data`를 사용)
    2. 유효성 검사(`is_valid()`)
    3. 저장(`save()`)
    4. 응답 전달(`Response()`)

### views.py

```python
# 앱/views.py
from rest_framework import status
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
```

## DELETE

> 게시글 데이터 삭제하기
> 
- 요청에 대한 데이터 삭제가 성공했을 경우는 `204 No Content` 상태 코드 응답
(명령을 수행했고 더 이상 제공할 정보가 없는 경우)

### views.py

```python
# 앱/views.py

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## PUT

> 게시글 데이터 수정하기
> 
- 요청에 대한 데이터 수정이 성공했을 경우는 `200 OK` 상태코드 응답
    - `200 OK` 상태 코드는 default 응답이기에 따로 상태 코드 설정을 하지 않음
- 기존에 사용하던 form들은 form(data, instance=instance)와 같은 구조로 입력 받았지만 serializer는 serializer(instance, data=data)와 같은 구조로 입력해야 한다.

### views.py

```python
# 앱/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
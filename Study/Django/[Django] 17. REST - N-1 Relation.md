# Django_REST - N : 1 Relation

> 게시글에 댓글 기능 생성
> 

## CommentSerializer

> serializers.py에 댓글을 위한 serializer 생성
> 

### serializers.py

```python
# 앱/serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article',)
```

## GET - List

> 댓글 데이터 목록 조회하기
> 
- Article List와 비교하며 작성해보기

### urls.py

```python
# 앱/urls.py

from django.urls import path
from . import views

urlpatterns = [
    ...,
    path('comments/<int:comment_pk>/', views.comment_detail),
    ...,
]
```

### views.py

```python
# 앱/views.py

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
```

## GET - Detail

> 단일 댓글 데이터 조회하기
> 
- Article과 달리 단일, QuerySet 모두 같은 serializer 사용

### views.py

```python
# 앱/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
```

## POST

> 단일 댓글 데이터 생성하기
> 
- form에서는 save 시 `commit`옵션을 통해 반환된 인스턴스에 article을 지정해주는 방식
- 하지만 serializer에서는 `commit` 옵션 없이 article 필드에 바로 article을 인자로 할당해주는 방식 사용

### urls.py

```python
# 앱/urls.py

urlpatterns = [
    ...,
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
```

### views.py

```python
# 앱/views.py

from rest_framework import status
from .models import Article
from .serializers import CommentSerializer

@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- 이후 댓글 작성을 시도하면 에러 발생
    - 외래 키로 설정한 article을 유효성 검사(`is_valid()`)시에는 비어있기 때문
    - 따라서 해당 필드를 유효성 검사에서는 제외 시키고 데이터 조회 시에는 출력 시켜야 한다.
    - `serializers.py`에서 `read_only_fields`를 사용해 **읽기 전용 필드**로 설정
        
        ```python
        # 앱/serializers.py
        
        class CommentSerializer(serializers.ModelSerializer):
        
            class Meta:
                model = Comment
                fields = '__all__'
                read_only_fields = ('article',)
        ```
        

## DELETE & PUT

> 댓글 데이터 삭제 및 수정 구현
> 

```python
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```

# N : 1 관계 - 역참조 데이터 조회

1. 특정 게시글에 작성된 댓글 목록 출력
    - 기존 필드 override
2. 특정 게시글에 작성된 댓글의 개수 출력하기
    - 새로운 필드 추가
    

## 1. 특정 게시글에 작성된 댓글 목록 출력

> 기존 필드 override - Article Detail
> 
> - 게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력
> - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

### 1-1 PrimaryKeyRelatedField 사용

> 댓글들의 PK만 조회 가능
> 
- 단일 게시물에서 댓글들을 조회
    - `ArticleSerializer`에 필드 추가
- 1:N 관계에서 N을 가져오는 필드
    - `many=True` 옵션 필수
- 유효성 검사 제외 및 데이터 조회 시 출력
    - `read_only=True` 옵션 필수
- comment_set의 이름 변경을 원할 시
    1. models.py에서 외래키 related manager의 이름을 `related_name`옵션으로  변경
    2. serializers.py에서도 같은 이름으로 변경 

### serializers.py

```python
# 앱/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

### 1-2 Nested relationships 사용

> 댓글들의 내용까지 조회 가능
> 
- `CommentSerializer` 사용을 위해 해당 클래스의 위치를 `ArticleSerializer`의 위쪽에 위치하도록 이동

### serializers.py

```python
# 앱/serializers.py

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article',)

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```

## 2. 특정 게시글에 작성된 댓글의 개수 출력하기

> 새로운 필드 추가 - Article Detail
> 
> - 게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기
- `serializers.IntegerField()`를 사용하여 댓글 개수 필드 추가
    - `source`
        - 필드를 채우는 데 사용할 속성의 이름
        - 점 표기법을 사용하여 속성 탐색 가능
        - ORM 명령어를 집어 넣어 SQL 연산이 가능
    - `read_only`
        - 유효성 제외 및 데이터 조회 시 출력
        - 새로 추가 된 필드이기에 옵션으로 설정

### serializers.py

```python
# 앱/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
```
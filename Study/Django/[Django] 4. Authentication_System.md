# Django_Authentication_System

> Django 인증 시스템은 인증(Authentication)과 권한(Authorization) 부여를 함께 제공
> 
- 필수 구성은 settings.py에 포함
    - INSTALLED_APPS에서 확인 가능(django.contrib.auth)

## 사전 설정

- 계정들을 관리할 수 있는 accounts 앱 생성 및 등록
    
    ```bash
    python manage.py startapp accounts
    ```
    
    ```python
    # 프로젝트/settings.py
    
    ...
    INSTALLED_APPS = [
    		'accounts',
    		```
    ]
    ```
    
    - auth와 관련한 경로나 키워드들은 Django에서 내부적으로 accounts라는 이름으로 사용하고 있기 때문에 accounts로 사용하는 것을 권장
- url 분리 및 매핑
    
    ```python
    # 앱(accounts)/urls.py
    
    from django.urls import path
    from . import views
    
    app_name = 'accounts'
    urlpatterns = [
    
    ]
    ```
    
    ```python
    # 프로젝트/urls.py
    
    from django.urls import path, include
    
    urlpatters = [
    		...,		
    		path('accounts/', include('accounts.urls')),
    ]
    ```
    

## User를 Custom User로 대체하기

- 개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구 사항이 적절하지 않을 수 있음
- Django는 현재 프로젝트에서 사용할 User Model을 결정하는 `프로젝트/setting.py`의 **AUTH_USER_MODEL** 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함
- Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분하더라도 CustomUser 모델을 설정하는 것을 **강력하게 권장**
    - **CustomUser 모델은 기본 User모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**

### AUTH_USER_MODEL

- 프로젝트에서 User를 나타날 때 사용하는 모델
- **프로젝트가 진행되는 동안(마이그레이션 진행 후) 변경할 수 없음**
    - 즉, 첫 번째 마이그레이션을 통해 확정
- 기본값
    
    ```python
    # settings.py
    
    AUTH_USER_MODEL = 'auth.user' # 'django.contrib.auth'안에 존재
    ```
    
    - 생성한 Custom User로 직접 할당 가능하나 기본값일 경우 settings.py에서 보이지 않음

### 프로젝트 초기에 User를 대체하지 못 했을 경우

> DB초기화 후 다시 마이그레이션
> 
1. migrations 파일 삭제
    - migrations 폴더 및 __init__.py는 삭제 X
    - 번호가 붙은 파일만 삭제(ex : 0001, 0002)
2. db.sqlite3 삭제
3. migrations 진행
    - python manage.py makemigrations
    - python manage.py migrate

## Custom User model로 대체하기 3단계

### 1. 대체할 User클래스 생성하기

```python
# accounts/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- 기존 User클래스도 AbstractUser를 상속 받기 때문에 CustomUser와 기존 User는 같은 모습을 가지고 있음
- 핵심 기능을 AbstractUser가 가지고 있기에 간단히 상속만 하면 됨
- AbstractUser
    - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스
- Abstract base classes(추상 기본 클래스)
    - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
    - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨

### 2. 생성한 CustomUser로 대체하기

```python
# settings.py

AUTH_USER_MODEL = 'accounts.user'
```

### 3. admin.py에 CustomUser 등록

```python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

- 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음
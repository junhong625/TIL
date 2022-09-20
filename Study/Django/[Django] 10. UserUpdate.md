# Django_UserUpdate

# 회원 정보 수정

> User를 Update하는 것이며 UserChangeForm built-in Form을 사용
> 

### UserChangeForm

> 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
> 
- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일

### urls.py

```python
# accounts/urls.py

from django.urls import path
from. import views

app_name = 'accounts'
urlpatterns = [
    ...
    path('update/', views.update, name='update'),
    ...
    ]
```

### views.py

- ArticleForm과 같은 부모를 상속 받았기에 똑같이 instance에 유저 정보 할당

```python
# accounts/views.py

from .forms import CustomUserChangForm

def update(request):
    if request.method == 'POST': # 회원 정보 수정 반영
        form = CustomUserChangeForm(request.POST, instance=request.user) 
        if form.is_valid():
            form.save()
        return redirect('articles:index')
    else: # 회원 정보 수정 페이지로 이동
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request, 'accounts/update.html', context)
```

### forms.py

- forms.py에서 UserCreationForm을 Custom해주지 않으면 일반 유저가 스스로 관리자 권한을 부여할 수 있는 치명적인 결함이 있음
    - admin 인터페이스에서 사용되는 ModelForm이기 때문
- 따라서 forms.py에서 필드를 Custom을 해준 후 사용해야 함

```python
# accounts/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm): # 기본 UserCreationForm 상속
    
    class Meta(UserCreationForm.Meta):# UserCreationForm.Meta 상속
        model = get_user_model() # 간접 참조하기 위한 함수를 사용
        fields = UserCreationForm.Meta.fields + ('email',)

class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = get_user_model() # 간접 참조하기 위한 함수를 사용
        fields = ('email', 'first_name', 'last_name')
```

### update.html

```html
{% templates/accounts/update.html %}

{% extends 'base.html' %}

{% block content %}
    <h1>회원정보수정</h1>
    <form action="{% url 'accounts:update' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit">
    </form>
{% endblock content %}
```

### base.html

```html
{% templates/base.html %}

...
<a href="{% url 'accounts:update' %}">회원정보수정</a>
...
```
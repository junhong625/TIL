# Django_Day_2

# Database

> 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
> 
- 체계화된 데이터의 모임

## Database의 구조

### 스키마(Schema)

> 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조
> 
- 간단히 얘기하여 데이터베이스의 뼈대(Structure)
- 

| column | datatype |
| --- | --- |
| id | Int |
| name | Text |

### 테이블(Table)

> 필드와 레코드를 사용해 조작된 데이터 요소들의 집합
> 
- 필드(field)
    - 속성, 열(column)
    - 각 필드에는 고유한 데이터 타입이 지정
- 리코드(record)
    - 튜플, 행(row)
    - 테이블의 데이터는 레코드에 저장

### PK(Primary Key)

> 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(Unique)
> 
- 기본 키
- 고유한 값
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용
- ex) 주민등록번호

### 쿼리(Query)

> 데이터를 조회하기 위한 명령어
> 

---

# Django Model

> Django에서 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구
> 
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
    - 모델 클래스 1개 == 데이터베이스 테이블 1개

## Model 작성

- 앱 내의 models.py 작성
    - 모델 클래스를 작성하는 것은 데이터베이스 **테이블의 스키마를 정의**하는 것
    - id 컬럼(pk)은 테이블 생성 시 Django가 자동으로 생성
    
    ```python
    from django.db import models
    
    class Article(models.Model): # models.Model클래스를 상속
    		title = models.CharField(max_length=10) # title 필드 정의
    		content = models.TextField() # content 필드 정의
    ```
    
    - models.CharField(max_length=10)
        - CharField타입
            - 길이의 제한이 있는 문자열(최대 길이 : 255)
            - `max_length` attribute 필수로 작성
    - models.TextField()
        - TextField타입
            - 많은 문자열 입력이 필요할 시 사용
                - database에 따라 최대 크기가 달라지기에 위와 같이 설명
            - 필수 attribute가 없음
- 위와 같이 클래스 상속 기반 형태의 Django를 사용함으로써 더욱 편리하게 기능을 생성 가능

# Migrations

> Model을 작성하고 난 이후 이를 적용하기 위한 필수 과정
> 

## 주요 명령어

### makemigrations

> Model의 변경사항에 대해 새로운 migration을 만들 때 사용
> 

```bash
python manage.py makemigrations
```

### migrate

> makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정(db.sqlite3 파일에 반영)
> 
- 모델의 변경 사항과 데이터베이스를 동기화

```bash
python manage.py migrate
```

## 데이터베이스 확인

### sqlite 다운(vs code)

- db.sqlite3파일 우클릭 후 open database 클릭
- SQLITE EXPLORER를 통해 동기화된 데이터베이스를 확인 가능
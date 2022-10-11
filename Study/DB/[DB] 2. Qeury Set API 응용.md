# QuerySet API 응용

## Sorting data

### order_by()

> QuerySet API를 활용한 정렬 함수
> 
- `.order_by(*fields)`
- 기본적으로 오름차순으로 정렬
    - 필드명에 ‘-’을 작성하면 내림차순으로 정렬
    - 인자로 ‘?’를 입력하면 랜덤으로 정렬

### values()

> 해당 레코드의 필드들을 확인하는 함수
> 
- `.values(*fields, **expressions)`
- 모델 인스턴스가 아닌 딕셔너리 요소들을 가진 QuerySet을 반환
- `*fields`는 선택 인자이며 조회하고자 하는 필드 명을 가변 인자로 입력 받음
    - 지정하지 않을 경우 모든 필드에 대한 key와 value를 반환

## Filtering data

### distinct()

> 중복 없이 원하는 필드 조회하기
> 
- `distinct()`
- 같은 컬럼에서 중복을 제외하고 하나의 값들만 반환

## Field lookups

> SQL WHERE절의 상세한 조건을 지정하는 방법
> 
- QuerySet 메서드 `filter()`, `exclude()` 및 `get()`에 대한 키워드 인자로 사용됨
- 문법 규칙
    - 필드명 뒤에 “double-underscore” 이후 작성
    
    ```python
    field__lookuptype=value
    ```
    
- “django field lookup“ 검색을 통해 사용 가능한 문법들 파악 가능

## Q object

> 기본적으로 filter()와 같은 메서드의 키워드 인자는 AND statement를 따름
> 
- 만약 더 복잡한 쿼리를 실행해야 할 경우 Q객체가 필요함
- `from django.db.models import Q` 로 임포트
- `&` 및 `|` 와 결합하여 사용 가능
- 조회를 하면서 여러 Q 객체를 제공할 수도 있음

## Aggregation(Grouping data)

### aggregate()

> 전체 queryset에 대한 값을 계산
> 
- 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용
- 딕셔너리를 반환

### annotate()

> 쿼리의 각 항목에 대한 요약 값을 계산
> 
- SQL의 `GROUP BY`에 해당
- ‘주석을 달다’라는 사전적 의미를 가지고 있음
# Django_fixtures

> Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
> 
- Django가 직접 만들기 때문에 데이터베이스 구조에 맞추어 작성되어 있음

## fixtures 기본 경로

> app_name/fixtures/
> 
- Django는 설치된 모든 app 의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾는다.

## fixtures 생성 및 로드

- 생성(추출)
    - dumpdata
- 로드(불러오기)
    - loaddata

### dumpdata

> 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력
> 
- 여러 모델을 하나의 json 파일로 만들 수 있음
- dumpdata 뒤에 `--indent 4` 를 추가 함으로써 정렬하여 생성 가능

```python
python manage.py dumpdata articles.article > articles.json
# python manage.py dumpdata 앱.모델 > 생성할 이름.json
```

### loaddata

> db에 dumpdata를 모두 불러오기
> 
- utf-8 오류가 발생할 경우
    - python 뒤에 -Xutf8을 추가하여 다시 dumpdata를 생성 후 load를 하면 해결 가능
- 따로 따로 할 경우 연관성을 생각해 순서를 올바르게 해야 함

```python
python manage.py loaddata ~.json ~.json
```
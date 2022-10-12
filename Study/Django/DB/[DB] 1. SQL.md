# 데이터베이스

## 데이터베이스가 등장하기 이전의 저장 방법

### 1. 파일을 이용한 데이터 관리

- 일반적으로 데이터는 파일에 저장
- 장점
    - 운영 체제에 관계 없이 어디에서나 쉽게 사용 가능
    - 이메일이나 메신저를 이용해 간편하게 전송 가능
- 단점
    - 성능과 보안적 측면에서 한계가 명확
    - 대용량 데이터를 다루기에 적합하지 않음
    - 데이터를 구조적으로 정리하기에 어려움
    - 확장이 불가능한 구조

### 2. 스프레드 시트를 이용한 데이터 관리

- 스프레드 시트(엑셀 시트)를 사용
- 스프레드 시트는 컬럼(열)을 통해 데이터의 유형을 지정하고 레코드(행)를 통해 구체적인 데이터 값을 포함
- 스프레드 시트 자체를 데이터 베이스라고 부를 수는 없지만 데이터베이스의 틀? 길목? 정도로 이야기 할 수 있음

# 데이터 베이스

> 체계화된 데이터의 모임
> 
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 검색, 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
    - 내용을 고도로 구조화 함으로써 검색과 갱신의 효율화를 노림
    - 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 구조화하여 기억시켜 놓은 자료의 집합체

## DBMS(DataBase Management System)

> DB를 조작하는 프로그램
> 
- Oracle, MySQL, SQLite 모두 DBMS
- **SQL** : DBMS에서 Database를 조작하기 위해 사용하는 언어
- 웹 개발에서 대부분의 DB는 관계형 데이터베이스(RDBMS)를 사용

## 관계형 데이터베이스(RDB)

> 데이터를 테이블, 행, 열 등으로 나누어 구조화 하는 방식
> 
- 자료를 여러 테이블로 나누어서 관리하고, 이 테이블 간 관계를 설정해 여러 데이터를 쉽게 조작할 수 있다는 장점이 존재
- SQL을 사용하여 데이터를 조회 및 조작

## RDB 기본 구조

### 스키마(Schema)

> 테이블의 구조(Structure)
> 
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것

### 테이블(Table)

> 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
> 
- 관계(Relation)라고도 부름
1. 필드(field)
    - 속성, 컬럼(column)
2. 레코드(record)
    - 튜플, 행(row)
    - 테이블의 데이터는 레코드에 저장

### PK(Primary Key)

> 각 레코드의 고유한 값(기본 키)
> 
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)

### RDB의 장점

- 데이터를 직관적으로 표현 가능
- 관련한 데이터에 쉽게 접근 가능
- 대량의 데이터 효율적 관리 가능

## RDBMS(Relational DataBase Management System)

> 관계형 데이터베이스를 만들고 업데이트하고 관리하는데 사용하는 프로그램
> 

### SQLite

> 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터베이스
> 
- Django Framework의 기본 데이터 베이스
- `안드로이드`, `iOS`, `macOS`에 기본적으로 탑재, 임베디드 소프트웨어에서 많이 활용
- 오픈 소스 프로젝트이기에 자유롭게 사용 가능
- 장점
    - 어떤 환경에서나 실행 가능한 호환성
    - 데이터 타입이 비교적 적고 강하지 않기에 유연한 학습환경을 제공
- 단점
    - 대규모 동시 처리 작업에는 적합하지 않음
    - 다른 RDBMS에서 지원하는 SQL기능을 지원하지 않을 수 있음

# SQL(Structured Query Language)

> RDBMS의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어
> 
- 데이터 베이스와 상호 작용
- RDBMS에서 데이터베이스 스키마를 생성 및 수정할 수 있으며, 테이블에서의 자료 검색 및 관리도 할 수 있음
- 데이터베이스 객체에 대한 처리를 관리하거나 접근 권한을 설정하여 허가된 사용자만 RDMBS를 관리할 수 있도록 할 수 있음
- 대부분의 DB관련 프로그램들이 SQL을 표준으로 채택

## SQL Commands 종류

### DDL(Data Definition Language) - 데이터 정의 언어

> 관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어
> 
- CREATE
- DROP
- ALTER

### DML(Data Manipulation Language) - 데이터 조작 언어

> 데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어
> 
- INSERT
- SELECT
- UPDATE
- DELETE

### DCL(Data Control Language) - 데이터 제어 언어

> 데이터의 보안, 수행 제어, 사용자 권한 부여 등을 정의 하기 위한 명령어
> 
- SQLite에는 DCL을 지원하지 않음
- GRANT
- REVOKE
- COMMIT
- ROLLBACK

## SQL Syntax

> 모든 SQL문(statement)는 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작, 세미콜론(;)으로 끝남
> 
- SQL 키워드는 대소문자를 구분하지 않지만 가독성을 위해 대문자로 작성하는 것을 권장
- statement(문) & clause(절)
    - statement는 독립적으로 실행할 수 있는 완전한 코드를 이야기 함
    - statement는 clause로 구성됨
    

## SQLite Data 특징

### 1. 다른 SQL DB엔진과 다르게 **동적 타입 시스템(dynamic type system)**을 사용

- 즉, 기존과 다르게 컬럼에 저장된 값에 따라 데이터 타입이 결정됨
- 따라서 테이블 생성 시 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨
- 이를 통해 다른 데이터베이스에서 불가능한 작업을 유연하게 수행 가능
- 또한 다른 SQL DB엔진에서 작동하는 SQL문도 동일하게 사용 가능
- **다만 이로 인해 다른 데이터베이스와 호환성 문제가 있기에 데이터 타입을 지정하는 것을 권장**

### 2. 데이터 타입을 지정하게 되면 SQLite는 입력된 데이터의 타입을 지정된 데이터 타입으로 변환

- 파이썬과 유사하게 데이터 형변환이 이루어짐

## SQLite Data Types

### 1. Null

- NULL value
- 정보가 없거나 알 수 없음을 의미

### 2. INTEGER

- 정수
- 크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐

### 3. REAL

- 실수
- 8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수

### 4. TEXT

- 문자 데이터

### 5. BLOB(Binary Large Object)

- 입력된 그대로 저장된 데이터 덩어리
- 바이너리 등 멀티미디어 파일
- 이미지 파일

### 6. 날짜와 Boolean

- SQLite에는 날짜와 Bool 타입이 X
- 0(False) 1(True)로 Bool 대체

### 7. Binary Data

- 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일

### SQLite 데이터 타입 결정 규칙

- INTEGER : 값에 둘러싸는 따옴표와 소수점 또는 지수가 없으면
- TEXT : 값이 작은 따옴표나 큰 따옴표로 묶이면
- REAL : 값에 따옴표나 소수점, 지수가 없으면
- NULL : 값이 따옴표 없이 NULL이면

## Type Affinity(타입 선호도)

> 특정 컬럼에 저장된 데이터에 권장되는 타입
> 
- 다른 데이터베이스 엔진 간의 호환성을 위해
- 데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터 타입을 선언한다면, 내부적으로 각 타입의 지정된 선호도에 따라 5가지 선호도로 인식됨
1. INTEGER
2. TEXT
3. BLOB
4. REAL
5. NUMERIC

# 제약 조건(Constraints)

> 사용자가 원하는 조건의 데이터만 유지하기 위해 데이터의 무결성을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약
> 

### 데이터의 무결성

- 데이터베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
    - 무결성 = 데이터의 정확성, 일관성
- 데이터베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적

## Constraints 종류

### 1. NOT NULL

- 컬럼이 NULL 값을 허용하지 않도록 지정

### 2. UNIQUE

- 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함

### 3. PRIMARY KEY

- 테이블에서 행의 고유성을 식별하는데 사용되는 컬럼
- 각 테이블에 하나의 기본 키만 존재
- 암시적으로 `NOT NULL` 제약 조건이 포함
- `INTEGER` 타입에만 사용 가능

### 4. AUTOINCREMENT

- 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
- `INTEGER PRIMARY KEY` 다음에 작성하면 해당 `rowid`를 다시 재사용하지 못하도록 함
- Django에서 테이블 생성 시 `id` 컬럼에 기본적으로 사용하는 제약조건

# DDL

> 테이블 구조를 관리하는 명령어
> 

## CREATE TABLE문

> 데이터베이스에 새 테이블을 생성
> 
- id 컬럼은 기본 키 역할의 컬럼을 정의하지 않으면 자동으로 `rowid`라는 컬럼을 생성함

```sql
CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);
```

### rowid의 특징

> 테이블을 생성할 때마다 `rowid`라는 암시적 자동 증가 컬럼이 자동으로 생성됨
> 
- 테이블의 행을 고유하게 식별하는 64비트 부호 있는 정수 값
- 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
- 시작 값 = 1
- 데이터 삽입 시에 `rowid` 또는 `INTEGER PRIMARY KEY` 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 `rowid`보다 하나 큰 다음 순차 정수를 자동으로 할당(`AUTOINCREMENT`와 관계없이)
- `INTEGER PRIMARY KEY` 키워드를 가진 컬럼을 직접 만들면 해당 컬럼은 `rowid`의 별칭(alias)이 됨
- 꽉 찼을 경우 SQLite가 사용되지 않은 정수를 찾을 수 없으면 `SQLITE_FULL` 에러가 발생
    - 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid 값을 재사용 시도

## ALTER TABLE

> 기본 테이블의 구조를 수정(변경)
> 
- SQLite에서 사용 가능한 `ALTER` 테이블의 기능 4가지
    1. Rename a table
        
        ```sql
        -- DDL.sql
        
        ALTER TABLE contacts RENAME TO new_contacts;
        ```
        
    2. Rename a column
        
        ```sql
        -- DDL.sql
        
        ALTER TABLE new_contacts RENAME COLUMN name to last_name;
        ```
        
    3. Add a new column to a table
        
        ```sql
        -- DDL.sql
        ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;
        ```
        
        - 기존에 데이터가 존재할 경우 DEFAULT 제약 조건을 사용하여 해결 필요
        - 해결 방법 예시
            
            ```sql
            -- DDL.sql
            ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
            ```
            
    4. Delete a column
        
        ```sql
        -- DDL.sql
        ALTER TABLE new_contacts DROP COLUMN address
        ```
        
        - 삭제가 불가능한 경우 3가지가 존재
            1. 컬럼이 다른 부분에서 참조되는 경우
            2. PRIMARY KEY인 경우
            3. UNIQUE 제약 조건이 있는 경우

## DROP TABLE

> 데이터베이스에서 테이블을 제거
> 
- 한 번에 하나의 테이블만 삭제 가능
- 실행 취소, 복구 불가

```sql
-- DDl.sql

DROP TABLE table_name;
```

# DML

## READ data

### SELECT statement

> 특정 테이블에서 데이터를 조회하기 위해 사용
> 
- 다양한 절과 함께 사용할 수 있음
- 규칙
    1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
    2. FROM 절에서 데이터를 가져올 테이블을 지정

```sql
-- DML.sql

SELECT column1, column2 FROM table_name;
```

### ORDER BY clause

> `SELECT` 문에 추가하여 결과를 정렬
> 
- `ORDER BY` 절은 `FROM` 뒤에 위치
- 하나 이상의 컬럼을 기준으로 결과를 오름차순, 내림차순으로 정렬
- `ASC` : 오름차순 (기본값)
- `DESC` : 내림차순
- 아래와 같이 두 가지의 조건으로 정렬할 경우 첫번째 조건으로 정렬한 이후 두번째 조건으로 정렬 진행
- SQLite에서 `NULL`은 가장 작은 값으로 간주

```sql
-- DML.sql

SELECT first_name, age, balance FROM users 
ORDER BY age ASC, balance DESC; 
```

## Filtering Data

### SELECT DISTINCT

> 조회 결과에서 중복된 행을 제거
> 
- `DISTINCT` 절은 `SELECT`에서 선택적으로 사용 가능
- 두 개의 컬럼을 조회할 경우 각각의 중복을 제거하는 것이 아닌 두 컬럼을 하나의 집합으로 보고 중복 제거
- SQLite는 `NULL` 값 끼리도 중복으로 간주
- 규칙
    - `DISTINCT` 절은 `SELECT` 키워드 바로 뒤에 나타나야 함
    - `DISTINCT`키워드 위에 컬럼 또는 컬럼 목록을 작성

```sql
-- DML.sql

SELECT DISTINCT select_list FROM table_name;
```

### WHERE clause

> 조회 시 특정 검색 조건을 지정
> 
- `WHERE` 절은 `SELECT` 문에서 선택적으로 사용할 수 있는 절
    - `SELECT` 문 외에도 `UPDATE` 및 `DELETE` 문에서  `WHERE` 절을 사용할 수 있음
- `FROM` 절 뒤에 작성

```sql
-- DML.sql

WHERE column_name 조건
```

### LIKE operator

> 패턴 일치를 기반으로 데이터를 조회
> 
- `SELECT`, `DELETE`, `UPDATE` 문의 `WHERE` 절에서 사용
- 기본적으로 대소문자를 구분하지 않음
    - ex) ‘A’ `LIKE` ‘a’는 true
- SQLite는 두 개의 와일드카드(wildcards)를 제공
    1. %(percent)
    - 0개 이상의 문자가 올 수 있음을 의미
    - ex) `영%` → 영, 영어, 영어권
    1. _(underscore)
    - 단일 (1개) 문자가 있음을 의미
    - ex) `영_` → 영미, 영어, 영국
- ‘홍’으로 끝나는 이름을 가진 데이터를 조회

```sql
-- DML.sql
SELECT first_name FROM users
WHERE first_name LIKE '%홍';
```

### IN operator

> 값이 값 목록 결과에 있는 값과 일치하는지 확인
> 
- 표현식이 값 목록의 값과 일치하는지 여부에 따라 `true` 또는 `false`를 반환
- `IN` 연산자의 결과를 부정하려면 `NOT IN` 연산자를 사용
- 강원도 또는 경기도에 사는 사람들의 이름과 지역을 조회

```sql
-- DML.sql

SELECT first_name, country FROM users
WHERE country in ('강원도', '경기도');
```

### BETWEEN operator

> 값이 값 범위에 있는지 확인
> 
- 값이 지정된 범위에 있으면 `true`를 반환
- `SELECT`, `DELETE`, 및 `UPDATE` 문의 `WHERE` 절에서 사용할 수 있음
- `BETWEEN` 연산자의 결과를 부정하려면 `NOT BETWEEN` 연산자를 사용
- `A BETWEEN B` = A이상 B이하
- 나이가 20살 이상 30살 이하인 사람들의 이름과 지역을 조회

```sql
-- DML.sql

SELECT first_name, country FROM users
WHERE age BETWEEN 20 AND 30;
```

### LIMIT clause

> 쿼리에서 반환되는 행 수를 제한
> 
- SELECT 문에서 선택적으로 사용할 수 있는 절
- row_count는 반환되는 행 수를 지정하는 양의 정수를 의미

```sql
-- DML.sql

SELECT column_list FROM table_name LIMIT row_count;
```

### OFFSET keyword

> LIMIT 절을 사용하면 첫 번째 데이터부터 지정한 수 만큼의 데이터를 받아올 수 있지만 OFFSET과 함께 사용하면 지정된 위치에서부터 데이터를 조회할 수 있음
> 
- 11번째부터 20번째 데이터의 rowid와 이름 조회

```sql
-- DML.sql

SELECT rowid, first_name FROM users
LIMIT 10 OFFSET 10;
```

## Grouping data

### GROUP BY

> 특정 그룹으로 묶인 결과를 생성
> 
- 선택된 컬럼 값을 기준으로 데이터들의 공통 값을 묶어서 결과로 나타냄
- SELECT 문에서 선택적으로 사용 가능한 절
- SELECT 문의 FROM 절 뒤에 작성
    - WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 함

```sql
-- DML.sql

SELECT country, COUNT(*) FROM users GROUP BY country
```

### 집계 함수(Aggregate function)

> 각 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
> 
- 각 집합에 대한 계산을 수행하고 단일 값을 반환
- `SELECT` 문의 `GROUP BY` 절과 함께  종종사용 됨
- 제공되는 함수 목록
    - `AVG(), COUNT(), MAX(), MIN(), SUM()`
- `AVG, MAX, MIN, SUM` 은 숫자를 기준으로 계산이 이루어지기에 반드시 컬럼의 데이터 타입이 `INTEGER`일때만 사용 가능
- 이름을 기준으로 그룹을 생성하고 각 이름을 가진 인원들의 수를 조회(AS 를 사용하여 표시되는 콜럼의 이름 변경)

```sql
-- DML.sql

SELECT last_name, COUNT(*) AS number_of_name
FROM users GROUP BY last_name
```

## Changing data

### INSERT statement

> 새 행을 테이블에 삽입
> 
- 규칙
    - 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
    - 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
    - VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가
        - 만약 컬럼 목록을 생략하는 경유 값 목록의 모든 컬럼에 대한 값을 지정해야 함
        - 컬럼의 개수가 value의 개수와 같아야 함

```sql
-- DML.sql

INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

### UPDATE statement

> 테이블에 있는 기존 행의 데이터를 업데이트한다.
> 
- 규칙
    - UPDATE 절 이후에 업데이트 할 테이블을 지정
    - SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
    - WHERE 절의 조건을 사용하여 업데이트할 행을 지정
        - 생략 시 모든 행의 데이터를 변경하는 심각한 실수를 저지를 수 있음
    - 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수를 지정 가능
- rowid가 2번인 데이터의 `name`을 `김철수한무두루미로` `address`를 `제주도`로 변경

```sql
-- DML.sql

UPDATE classmates
SET name='김철수한무두루미', 
    address='제주도'
WHERE rowid = 2;
```

### DELETE statement

> 테이블에서 행을 제거
> 
- 테이블의 한 행, 여러 행 및 모든 행을 삭제 할 수 있음
- 규칙
    - DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
    - WHERE 절에 검색 조건을 추가하여 제거할 행을 식별
        - WHERE 절은 생략 가능하나 UPDATE와 마찬가지로 모든 행을 삭제하는 심각한 실수가 발생할 수 있음
    - 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행을 지정 가능

```sql
-- DML.sql

DELETE FROM table_name
WHERE search_condition;
```
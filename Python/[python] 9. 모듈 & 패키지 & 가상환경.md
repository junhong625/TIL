# Python_9 🖥️

# 모듈과 패키지

### 모듈

> 다양한 기능을 하는 코드를 하나의 파일(.py) 단위로 묶은 것
> 

### 패키지

> 다양한 모듈을 하나의 폴더로 묶은 것
> 

### 라이브러리

> 다양한 패키지를 하나의 묶음으로 묶은 것
> 

### PIP

> 라이브러리를 관리하는 관리자
> 

### 가상 환경

> 패키지의 활용 공간
> 

## 모듈과 패키지 불러오기

- 예시

```python
import module
from module import var, function
from module import * # * 은 모두 불러온다의 의미

from package import module
from package.module import var, function, Class
```

## 파이썬 패키지 관리자(pip)

- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템

### 패키지 관리자 명령어

- 패키지 설치
    - 최신 버전 / 특정 버전 / 최소 버전을 명시하여 설치할 수 있음
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음

```bash
pip install package
```

> 모두 bash, cmd 환경에서 사용되는 명령어
> 
- 패키지 삭제
    - pip는 패키지 업그레이드를 하는 경우 과거 버전을 자동으로 지워줌

```bash
pip uninstall package
```

- 패키지 목록 및 특정 패키지 정보

```bash
pip list

pip show package
```

- 패키지 관리하기
    - 아래의 명령어들을 통해 패키지 목록을 관리[1]하고 설치할 수 있음[2]
    - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의함
    - requirements.txt를 바탕으로 설치
    - 다양한 프로젝트에서 사용됨

```bash
pip freeze > requirements.txt # [1]

pip install -r requirements.txt # [2]
```

---

# 사용자 모듈과 패키지

## 패키지 만들기

---

# 가상 환경

- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치를 해야 함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
    - 이러한 경우 가상 환경을 만들어 프로젝트 별로 독립적인 패키지 관리 가능
- 가상 환경을 만들고 관리하는데 사용되는 모듈
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    1. 특정 폴더에 가상 환경 존재
    2. 실행 환경(예: bash)에서 가상 환경을 활성화
    3. 해당 폴더에 있는 패키지를 관리/사용
    

### 가상 환경 생성

```bash
python -m venv 폴더명
```

### 가상 환경 활성화/비활성화

```bash
source venv/Scripts/activate
source venv/Scripts/deactivate
```

- 가상환경 \ Lib\ site-packages 에서 설치된 패키지 확인 가능
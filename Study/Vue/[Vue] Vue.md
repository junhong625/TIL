> `JavaScript`를 활용하여 `Web App(SPA)`을 만들 때 사용하는 `Front-end Framework`
> 

### Web App이란?

- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
- 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것
- 웹 페이지가 디바이스에 맞는 적절한 `UX`/`UI`로 표현되는 형태

### SPA(Single Page Application)

- `Web App`과 함께 자주 등장할 용어 `SPA`
- 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template을 반환
- `SPA`는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식
    - `CSR(Client Side Rendering)` 방식으로 요청을 처리하기 때문

### SSR과 CSR

**SSR** 

- 기존의 요청 처리 방식
- Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
- 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

**CSR**

- 각 요청에 대한 대응을 `JavaScript`를 사용하여 필요한 부분만을 다시 렌더링
- Server로 부터 받아오는 문서는 빈 html  문서
1. 필요한 페이지를 서버에 `AJAX`로 요청
2. 서버는 화면을 그리기 위해 필요한 데이터를 `JSON` 방식으로 전달
3. `JSON` 데이터를 `JavaScript`로 처리, `DOM` 트리에 반영(렌더링)

### CSR 방식 사용 이유

1. 모든 `HTML` 페이지를 서버로부터 받아서 표시하지 않아도 됨
    
    == `클라이언트 - 서버` 간 통신 즉, 트래픽 감소
    
    == 응답  속도 UP
    
2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
    - SNS에서 추천을 누를 때 마다 첫 페이지로 이동 = 끔 찍….
    - 요청이 자연스럽게 진행이 된다 = `UX` 향상
3.  `BE`와 `FE`의 작업 영역을 명확히 분리 가능
    - 각자 맡은 역할을 명확히 분리 = 협업 용이

### CSR 단점

- 첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
- 검색 엔진 최적화(`SEO, Search Engine Optimization`)가 어려움
    - 서버가 제공하는 것은 텅 빈 `HTML`
    - 내용을 채우는 것은 `AJAX` 요청으로 얻은 `JSON` 데이터로 클라이언트(브라우저)가 진행
- 대체적으로 `HTML`에 작성된 내용을 기반으로 하는 검색 엔진에 빈 `HTML`을 공유하는 `SPA` 서비스가 노출되기는 어려움

### SEO(Search Engine Optimization)

- `google`, `bing`과 같은 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
- 검색 = 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
- 검색 엔진 = 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
    - 정보의 대상은 주로 `HTML`에 작성된 내용
    - `JavaScript`가 실행된 이후의 결과를 확인하는 과정이 없음
- 최근 `SPA`, 즉 `CSR`로 구성된 서비스의 비중이 증가
    - `SPA`서비스도 검색 대상으로 넓히기 위해 `JS`를 지원하는 방식으로 발전
- 단, 단순 `HTML` 만을 분석하는 것보다 몇 배의 리소스가 필요한 작업이기에 여전히 `CSR`의 검색 엔진 최적화 문제가 모두 해결된 것은 아님

# Why Vue?

1. 사용이 쉽다.
    - 타 Framework에 비해 입문자가 시작하기에 좋은 Framework
    - 구글의 `Angular` 개발자 출신 `Evan You`가 가겹고, 간편하게 사용할 수 있는 Framework를 목표로 개발
2. 구조가 매우 직관적
    - `template` → `script` → `style` 총 3가지의 구조로 이루어져 있음

## 사전 준비

- VSCode `Vetur` extension 설치
- Chrome `Vue.js devtools` extension 설치
    - 확장 프로그램 관리 - 파일 URL에 대한 액세스 허용
- Vue3가 출시 됐으나 여전히 Vue2를 사용한 레거시 코드가 많고 안정적인 측면에서 Vue2가 아직 우세하기에 Vue2를 사용

## Vue로 코드 작성 방법

1. `Vue CDN` 가져오기
2. `Vue instance` 생성
    - `Vue instance` - 1개의 Object
    - 미리 정해진 속성명을 가진 Object
3. `el, data, methods` 작성
    - `el (element)`
        - `Vue instance`와 `DOM`을 mount하는 옵션
            - View와 Model을 연결하는 역할
            - HTML id 혹은 class와 마운트 가능
        - `Vue instance`와 연결되지 않은 `DOM` 외부는 `Vue`의 영향을 받지 않음
            
            ```html
            <div id="app">
              {{ message }}
            </div>
            
            <div>
              {{ message }}
            </div>
            
              <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
              <script>
                const app = new Vue({
                  el: '#app',
                  data: {
                    message: 'Hello, Vue!'
                  },
            ...
            ```
            
            > 위와 같이 작성 시 `id`가 `app`인 `div`에만 `‘Hello, Vue!’`가 출력됨
            > 
            - `Vue` 속성 및 메서드 사용 불가
    - `data`
        - `Vue instance`의 데이터 객체 혹은 인스턴스 속성
        - 데이터 객체는 반드시 기본 객체 `{ }(Object)` 여야 함
        - 객체 내부의 아이템들은 `value`로 모든 타입의 객체를 가질 수 있음
        - 정의된 속성은 `interpolation {{ }}` 을 통해 `view`에 렌더링 가능함
    - `methods`
        - `Vue instance`의 `method`들을 정의하는 곳
        - 메서드를 정의할 때, Arrow Function 사용 X
        - `methods` 객체 정의
            
            ```html
            <script>
            ...
            methods: {
                    print: function () {
                      console.log(this.message)
                    },
                }
            ...
            </script
            ```
            
        - `method`를 호출하여 `data` 변경 가능
            
            ```html
            <script>
            ...
            methods: {
                    bye: function () {
                      this.message = 'Bye, Vue!'
                    },
                }
            ...
            </script
            ```
            
4. 선언적 렌더링{[]}
    - `Vue data`를 화면에 렌더링
        - 데이터 변경이 이루어졌을 시 화면에서 연쇄적으로 수정이 이루어져야 하는 부분들을 `Vue data`를 이용한다면 수월하게 작업 가능

## Vue의 Pattern

**MVVM Pattern**

- 소프트웨어 아키텍처 패턴의 일종
- `MVC Pattern`에서 `Controller`를 제외하고 `View Model`을 넣은 패턴
- `View` 와 `Model` 간의 의존성 Down, 독립성 Up
- `MarkUp` 언어로 구현하는 그래픽 사용자 인터페이스(`view`)의 개발을 Back-end(`model`)로부터 분리시켜 `view`가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
- `View`
    - 우리 눈에 보이는 부분 == `DOM`
- `Model`
    - 실제 데이터 == `JSON`
- `View Model (Vue)`
    - `View`를 위한 `Model`
    - `View`와 연결(binding)되어 Action을 주고 받음
    - `Model`이 변경되면 `View Model`도 변경되고 바인딩된 `View`도 변경됨
    - `View`에서 사용자가 데이터를 변경하면 `View Model`의 데이터가 변경되고 바인딩된 다른 `View`도 변경됨

```html
<script>
#####################################
#  const app = new Vue({            #
#    el: '#app',                    #
# #######################           #
# #    data: {          #           #
# #      message: '',   # <- Model  # <- View Model
# #    }                #           #
# #######################           #
#  })                               #
#####################################
</script>
```

## Vue instance

1. `Vue CDN` 가져오기

```html
<!-- Vue CDN -->
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
```

1. `new` 연산자를 사용한 생성자 함수 호출하여 새로운 객체 생성

> vue instance 생성
> 

```html
<script>
  const vm = new Vue()
</script>
```
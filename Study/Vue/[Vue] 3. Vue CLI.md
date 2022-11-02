## Node.js

- 자바스크립트는 브라우저를 조작하는 유일한 언어
    - 하지만 브라우저 밖에서는 구동할 수 없었음
- 자바스크립트를 구동하기 위한 런타임 환경인 `Node.js`로 인해 브라우저가 아닌 환경에서도 구동할 수 있게 됨
    - `Chrome V8` 엔진을 제공하여 여러 OS 환경에서 실행할 수 있는 환경을 제공
    - `Browser`만 조작 가능했으나, `Server-Side-Programming` 또한 가능

### NPM (Node Package Manage)

- 자바스크립트 패키지 관리자
    - `Python`에 `pip`가 있다면 `Node.js`에는 `npm`
    - `pip`와 마찬가지로 다양한 의존성 패키지를 관리
- `Node.js`의 기본 패키지 관리자
- `Node.js` 설치 시 함께 설치됨

## Vue CLI

- `Vue` 개발을 위한 표준 도구
- 프로젝트의 구성을 도와주는 역할
- 확장 플러그인, `GUI`, `Babel` 등 다양한 tool 제공

- **설치**
    
    ```bash
    npm install -g @vue/cli
    ```
    

- **프로젝트 생성**
    - `vscode` terminal에서 진행
    
    ```bash
    vue create vue-cli
    ```
    
    - 버전 선택(`Vue2`)후 시작

- **프로젝트 실행**
    
    ```bash
    cd vue-cli
    npm run serve
    ```
    

## Vue CLI 프로젝트 구조

### node_modules

- `node.js` 환경의 여러 의존성 모듈
- `python`의 `venv`와 비슷한 역할을 함
    - 따라서 `.gitignore`에 넣어주어야 하며, `Vue` 프로젝트를 생성하면 자동으로 추가됨
    

### Babel

- JavaScript compiler
- 자바스크립트의 `ES6+`코드를 구버전으로 변역/변환 해주는 도구
- 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
    - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생
    - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구
    - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서   코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않는다.
    

### Webpack

- `static module bundler`
- 모듈 간의 의존성 문제를 해결하기 위한 도구
- 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

### Module

- 개발하는 어플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐
- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이때 분리된 파일 각각이 모듈(`module`) 즉, js 파일 하나가 하나의 모듈
- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨
- 여러 모듈 시스템
    - `ESM(ECMA Script Module)`, `AMD`, `CommonJS`, `UMD`

### Module 의존성 문제

- 모듈의 수가 많아지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움
    - `Webpack`은 이 모듈 간의 의존성 문제를 해결하기 위해 등장
    

### Bundler

- 모듈 의존성 문제를 해결해주는 작업이 `Bundling`
- 이러한 일을 해주는 도구가 `Bundler`이고, `Webpack`은 다양한 `Bundler` 중 하나
- 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
- `Bundling`된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨
- `snowpack`, `parcel`, `rollup.js` 등의 `webpack` 이외에도 다양한 모듈 번들러 존재
- `Vue CLI`는 이러한 `Babel`, `Webpack`에 대한 초기 설정이 자동으로 되어

### package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

### package-lock.json

- `node_modules`에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
- 사용 할 패키지의 버전을 고정
- 개발 과정 간의 의존성 패키지 충돌 방지
- python의 `requirements.txt`

### public/index.html

- `Vue` 앱의 뼈대가 되는 `html`파일
- `Vue` 앱과 연결될 요소가 있음

### src/

- `src/assets`
    - 정적 파일을 저장하는 디렉토리
- `src/components`
    - 하위 컴포넌트들이 위치
- `src/App.vue`
    - 최상위 컴포넌트
    - `public/index.html` 과 연결됨
- `src/main.js`
    - `webpack`이 빌드를 시작할 때 가장 먼저 불러오는 entry point
    - `public/index.html`과 `src/App.vue`를 연결시키는 작업이 이루어지는 곳
    - `Vue`전역에서 활용 할 모듈을 등록할 수 있는 파일

## SFC

### Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것
    - 즉, 기능별로 분화한 코드 조각
- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임
    - Web HTML 요소들의 중첩과 유사
        - `Body` tag를 root node로 하는 tree의 구조
        - 마찬가지로 `Vue`에서는 `src/App.vue`를 root node로 하는 tree의 구조를 가짐
- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공
- 우리가 사용하는 웹 서비스도 여러 개의 컴포넌트로 이루어져 있음
- 하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리 가능
- **특징**
    - 관리가 용이
        - 유지/보수 비용 감소
    - 재사용성
    - 확장 가능
    - 캡슐화
    - 독립적

### Component in Vue

- 결국 `Vue`에서 말하는 component == `Vue instance`
    - ex) `const app = new Vue()` 에서의 `app`이 component

### SFC(Single File Component)

- 하나의 `.vue` 파일이 하나의 `Vue instance`이고, 하나의 컴포넌트이다.
    - 즉, `Single File Component`
- `Vue instance`에서는 HTML, CSS, JavaScript 코드를 한 번에 관리
    - `Vue instance`를 기능 단위로 작성하는 것이 핵심
- 컴포넌트 기반 개발의 핵심 기능

### Vue component 구조

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 구성
- root에 해당하는 최상단의 component가 `App.vue`
- `App.vue`를 `index.html`과 연결
- 결국 `index.html` 파일 하나만을 rendering == SPA
- 템플릿(HTML)
    - HTML의 `body` 부분
    - 눈으로 보여지는 요소 작성
    - 다른 컴포넌트를 HTML 요소처럼 추가 가능
    - `template` 안에는 반드시 하나의 요소만 추가 가능
        - `template` tag는 단지 영역에 대한 표시일 뿐 실제 적용이 되는 칸이 아니기 때문에 반드시 최상위 태그 필수
        - 비어있어도 안됨
    
    ```html
    <template>
      <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
      </div>
    </template>
    ```
    
- 스크립트(JavaScript)
    - JavaScript 코드가 작성되는 곳
    - 컴포넌트 정보, 데이터, 메서드 등 `Vue instance`를  구성하는 대부분이 작성 됨
    
    ```html
    <script>
    import HelloWorld from './components/HelloWorld.vue'
    
    export default {
      name: 'App',
      components: {
        HelloWorld
      }
    }
    </script>
    ```
    
- 스타일(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당
    
    ```html
    <style>
    #app {
      font-family: Avenir, Helvetica, Arial, sans-serif;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      text-align: center;
      color: #2c3e50;
      margin-top: 60px;
    }
    </style>
    ```
    

### component 등록 3단계

> **순서 절대 까먹지 말기!**
> 
1. **불러오기**
2. **등록하기**
3. **보여주기**

```html
// App.vue

<template>
<!-- 3. 보여주기 -->
  <div id="app">
    <h1>이곳은 App.vue 입니다.</h1>
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="SSAFY 여러분을 응원합니다!"/>
  </div>
</template>

<script>
// 1. 불러오기
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    // 2. 등록하기
    HelloWorld,
  }
}
</script>
```

### 1.  component 등록 - 불러오기

- `import {instance name} from {위치}`
- instance name은 instance 생성 시 작성한 name
- `@`는 src(`./`)의 shortcut
- 위치에 `.vue` 생략 가능

```html
<script>
import HelloWorld from './components/HelloWorld.vue'
import MyComponentVue from '@components/MyComponent' // 불러오기
```

### 2. component 등록 - 등록하기

```html
export default {
  name: 'App',
  components: {
    HelloWorld,
    MyComponentVue, // 등록하기
  }
}
</script>
```

### 3. component 등록 - 보여주기

- 닫는 태그(`</>`)만 있는 요소처럼 사용

```html
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <MyComponentVue/>
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>
```
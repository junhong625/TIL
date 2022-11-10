# Routing

- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
    - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

## Routing in SSR

- Server가 모든 라우팅을 통제
- URL로 요청이 들어오면 응답으로 완성된 `HTML` 제공
    - `Django`로 보낸 요청의 응답 `HTML`은 완성본인 상태였음
- 결론적으로 `Routing(URL)`에 대한 결정권을 서버가 가짐

## Routing in SPA / CSR

- 서버는 하나의 `HTML(index.html)` 만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 `JavaScript` 코드를 활용
    - `DOM`을 그리는데 필요한 추가적인 데이터가 있다면 `axios`와 같은 `AJAX` 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉, **하나의 URL만 가질 수 있음**

## Why routing?

- 동작에 따라 반드시 URL이 바뀔 필요는 없음
    - 단, 유저의 사용성 관점에서는 필요함
- Routing이 없다면,
    - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
        - 새로고침 시 처음 페이지로 돌아감
        - 링크를 공유할 시 처음 페이지만 공유 가능
    - 브라우저의 뒤로 가기 기능을 사용할 수 없음

## Vue Router

- `Vue`의 공식 라우터
- `SPA` 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌틍를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    - 즉, `SPA`를 `MPA`처럼 URL을 이동하면서 사용 가능
        - `MPA`(Multiple Page Application)
            - 여러 개의 페이지로 구성된 애플리케이션
            - `SSR` 방식으로 렌더링
    - `SPA`의 단점 중 하나인 “**URL이 변경되지 않는다.”** 를 해결

### Vue Router 시작

- `Vuex`와 마찬가지의 방식으로 설치 및 반영

```jsx
vue create vue-router-app
cd vue-router-app
vue add router
```

- `History mode` 여부 → Yes
    - `History mode`
        - 브라우저의 `History API`를 활용한 방식
            - 새로고침 없이 URL 이동 기록을 남길 수 있음
        - 우리에게 익숙한 URL 구조로 사용 가능(`/`)
        - `History mode`를 사용하지 않으면 Default 값인 `hash mode`로 설정됨 (`#`을 통해 URL을 구분하는 방식)
- 변화된 부분이 발생
    - `App.vue`
        - `router-link` 요소 및 `router-view`가 추가됨
    - `router/index.js` 생성됨
    - `views` 폴더 생성됨

### `router-link`

- `a`태그와 비슷한 기능 → URL을 이동시킴
    - `routes`에 등록된 컴포넌트와 매핑됨
    - 히스토리 모드에서 `router-link`는 클릭 이벤트를 차단하여 `a` 태그와 달리 브라우저가 페이지를 다시 로드 하지 않도록 함
- 목표 경로는 `to` 속성으로 지정
- 기능에 맞게 HTML에서 `a` 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

### `router-view`

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
- 실제 `component`가 `DOM`에 부착되어 보이는 자리를 의미
- `router-link`를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- `Django`에서의 `block tag`와 유사
    - `App.vue`는 `base.html`의 역할
    - `router-view`는 `block`태그로 감싼 부분

### `src/router/index.js`

- 라우터와 관련된 정보 및 설정이 작성되는 곳
- `Django`에서의 urls.py에 해당
- routes에 URL과 컴포넌트를 매핑

### `src/Views`

- `router-view`에 들어갈 `component` 작성
- 기존에 컴포넌트를 작성하던 곳은 `components` 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
- 각 폴더 안의 `.vue` 파일들이 기능적으로 다른 것은 아님
- 각 폴더의 역할
    - `views` : routes에 매핑되는 컴포넌트들을 모아두는 폴더
        - 다른 컴포넌트와 구분하기 위해 이름이 View로 끝나도록 만드는 것을 권장
    - `components` : routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

## 주소를 이동하는 2가지 방법

1. 선언적 방식 네비게이션
2. 프로그래밍 방식 네비게이션

### 1. 선언적 방식 네비게이션

- `router-link`의 `to`속성으로 주소 전달
    - routes에 등록된 주소와 매핑된 컴포넌트로 이동
- `Named routes`
    - 이름을 가지는 routes
        - `Django`에서 path 함수의 name인자의 활용과 같은 방식
- 동적인 값을 사용하기 때문에 `v-bind`를 사용해야 정상적으로 작동

### 2. 프로그래밍 방식 네비게이션

- `Vue 인스턴스` 내부에서 `라우터 인스턴스`에 `$router`로 접근할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
    - `history stack`에 이동한 ULR을 넣는(push) 방식
    - `history stack`에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수있음
- 즉, `<router-link :to="">`를 클릭하는 것과 `$router.push()`를 호출하는 것은 같은 동작
    
    ```jsx
    <template>
      <div class="about">
        <h1>This is an about page</h1>
        <router-link :to="{ name:'home' }">Home</router-link>
        <button @click="toHome">홈으로!</button>
      </div>
    </template>
    <script>
    export default {
      name: 'AboutView',
      methods: {
        toHome() {
          this.$router.push({ name: 'home' })
        }
      }
    }
    </script>
    ```
    

### Dynamic Route Matching

- 동적 인자 전달
    - URL의 특정 값을 변수처럼 사용할 수 있음
- `Django`에서의 `variable routing`
- `HelloView.vue` 작성 및 route 추가
    - route를 추가할 때 동적 인자를 명시
    - `HelloView.vue`
        
        ```jsx
        <template>
          <div></div>
        </template>
        
        <script>
        export default {
          name: 'HelloView',
        }
        </script>
        
        <style>
        
        </style>
        ```
        
    - `index.js`
        
        ```jsx
        import Vue from 'vue'
        import VueRouter from 'vue-router'
        import HomeView from '../views/HomeView.vue'
        import HelloView from '@/views/HelloView' // import
        
        Vue.use(VueRouter)
        
        const routes = [
          {
            path: '/',
            name: 'home',
            component: HomeView
          },
          {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (about.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
          },
        // 추가
          {
            path: '/hello/:userName/',
            name: 'hello',
            component: HelloView,
          }
        ]
        
        const router = new VueRouter({
          mode: 'history',
          base: process.env.BASE_URL,
          routes
        })
        
        export default router
        ```
        
- `$route.params`로 data에 데이터를 넣어서 variable routing을 사용하는 것을 권장
    
    ```jsx
    <template>
      <div>
        <h1>hello, {{ userName }}</h1>
      </div>
    </template>
    
    <script>
    export default {
      name: 'HelloView',
      data() {
        return {
          userName: this.$route.params.userName
        }
      }
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- `params`를 이용하여 동적 인자 전달 가능
    
    ```jsx
    <template>
      <div id="app">
        <nav>
          <router-link :to="{ name: 'home' }">Home</router-link> |
          <router-link :to="{ name: 'about' }">About</router-link> |
          <router-link :to="{ name: 'hello', params: { userName: 'ssafy' }}">Hello</router-link>
        </nav>
        <router-view/>
      </div>
    </template>
    ```
    

### lazy-loading

- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
    - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
    - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

```jsx
// router/index.js

const routes = [
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue'),
  }
]
```
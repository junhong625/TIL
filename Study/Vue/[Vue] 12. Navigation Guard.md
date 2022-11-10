# Navigations Guard

- `Vue router`를 통해 특정 URL에 접근할 때 다른 url로 `redirect`를 하거나 해당 URL로의 접근을 막는 방법

## 네비게이션 가드의 종류

- 전역 가드
    - 애플리케이션 전역에서 동작
- 라우터 가드
    - 특정 URL에서만 동작
- 컴포넌트 가드
    - 라우터 컴포넌트 안에 정의

## 전역 가드(Global Before Guard)

- 다른 url 주소로 이동할 때 항상 실행
- `router/index.js`에 `router.beforeEach()`를 사용하여 설정
- 콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
    - `to` : 이동할 URL 정보가 담긴 `Route`객체
    - `from` : 현재 URL 정보가 담긴 `Route`객체
    - `next` : 지정한 URL로 이동하기 위해 호출하는 함수
        - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
        - 기본적으로 `to`에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 `router.beforeEach()`가 호출됨
    - 화면이 전환되지 않고 대기 상태가 됨
- 변경된 URL로 라우팅하기 위해서는 `next()`를 호출해줘야 함
    - `next()`가 호출되기 전까지 화면이 전환되지 않음

```jsx
const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  console.log('to', to)
  console.log('from', from)
  console.log('next', next)
  next() // 호출을 해야 화면 전환이 이루어짐
})

export default router
```

### Login 여부에 따른 라우팅 처리

- Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가
    - `views/LoginView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>로그인 페이지</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'LoginView',
        }
        </script>
        ```
        
    - `router/index.js`
        
        ```jsx
        import LoginView from '@/views/LoginView'
        
        Vue.use(VueRouter)
        
        const routes = [
          ...
          {
            path: '/login',
            name: 'login',
            component: LoginView,
          }
        ]
        ```
        
- `LoginView`에 대한 라우터 링크 추가
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <nav>
              <router-link :to="{ name: 'login'}">Login</router-link>
            </nav>
            <router-view/>
          </div>
        </template>
        ```
        
- HelloView에 로그인을 해야만 접근 가능하도록 설정
    - 로그인 여부에 대한 임시 변수 생성
    - 로그인이 필요한 페이지를 저장
    - 앞으로 이동할 제이지(to)가 로그인이 필요한 사이트인지 확인
    - `isAuthRequired` 값에 따라 페이지 이동
        - 로그인이 되어있다면 기존 루트로 이동
        - 로그인이 되어있지 않다면 Login 페이지로 이동
    - `next()`인자가 없을 경우 to로 이동
    - `router/index.js`
        
        ```jsx
        router.beforeEach((to, from, next) => {
          // 로그인 여부
          const isLoggedIn = true
        
          // 로그인이 필요한 페이지
          const authPage = ['hello']
        
          // 로그인이 필요한 사이트인지 확인
          const isAuthRequired = authPage.includes(to.name)
        
          if (isAuthRequired && !isLoggedIn) { // isAuthRequired 값에 따라 이동
            next({ name: 'login'})
          }else {  
            next()
          }
        })
        ```
        

## 라우터 가드

- 전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
- `beforeEnter()`
    - route에 진입했을 때 실행됨
    - 라우터를 등록한 위치에 추가
    - 단 매개변수, 쿼리, 해시 값이 변경되 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    - 콜백 함수는 `to`, `from`, `next`를 인자로 받음

### Login 여부에 따른 라우팅 처리

- 라우터 가드 실습을 위해 전역 가드 실습 주석 처리
- 로그인 여부에 대한 임시 변수 생성
- 로그인 여부에 따라 `home` or `login` 으로 이동
    - `router/index.js`
        
        ```jsx
        import LoginView from '@/views/LoginView'
        
        Vue.use(VueRouter)
        const isLoggedIn = true
        
        const routes = [
          ...,
          {
            path: '/login',
            name: 'login',
            component: LoginView,
            beforeEnter(to, from, next) {
              if (isLoggedIn === true) {
                next({ name: 'home' })
              } else {
                next()
              }
            }
          }
        ]
        ```
        

## 컴포넌트 가드

- 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
- `beforeRouteUpdate()`
    - 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

### Params 변화 감지

- `about`에서 `input`에 입력하여 `Hello` 페이지로 이동
- `navbar`에 있는 Hello를 눌러 인사하는 페이지로 이동
    - URL은 변하지만 페이지는 변하지 않음
- 변화하지 않는 이유
    - 컴포넌트가 재사용되었기 때문
    - 기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
        - 단, `lifecycle hook`이 호출되지 않음
        - 따라서 `$route.params`에 있는 데이터를 새로 가져오지 않음
- `beforRouteUpdate()`를 사용해서 처리
    - `userName`을 이동할 `params`에 있는 `userName`을 재할당

## 404 Not Found

- 사용자가 요청한 리소스가 존재하지 않을 때 응답

### 요청한 리소스가 존재하지 않는 경우

- 모든 경로에 대해서 404 page로 `redirect`시키기
    - 기존에 명시한 경로가 아닌 모든 경로가 404 page로 `redirect`됨
    - **이때, routes에 최하단부에 작성해야 함**
    - `router/index.js`
        
        ```jsx
        const routes = [
          ...
          {
            path: '*',
            redirect: '/404',
          }
        ]
        
        const router = new VueRouter({
          mode: 'history',
          base: process.env.BASE_URL,
          routes
        })
        ```
        

### 형식은 유효하지만 특정 리소스를 찾을 수 없는 경우(Dog API 활용)

- `Axios` 설치
    
    ```bash
    npm i axios
    ```
    
- `DogView` 컴포넌트 작성
    - `views/DogView.vue`
        
        ```jsx
        <template>
          <div>
          </div>
        </template>
        
        <script>
        import axios from 'axios'
        
        export default {
          name: 'DogView',
        }
        ```
        
- `routes`에 등록
    - `*` 보다 상단에 등록
        
        ```jsx
        import DogView from '@/views/DogView'
        
        Vue.use(VueRouter)
        const isLoggedIn = true
        
        const routes = [
          ...
          {
            path: '/dog/:breed',
            name: 'dog',
            component: DogView,
          },
          {
            path: '*',
            redirect: '/404',
          },
        ]
        ```
        
- `axios` 로직을 작성
    - `views/DogView.vue`
        
        ```jsx
        <template>
          <div>
            <p v-if="!imgSrc">{{ message }}</p>
            <img :src="imgSrc" alt="">
          </div>
        </template>
        
        <script>
        import axios from 'axios'
        
        export default {
          name: 'DogView',
          data() {
            return {
              imgSrc: null,
              message: '로딩 중...',
            }
          },
          methods: {
            getDogImage() {
              const breed = this.$route.params.breed
              const dogImageUrl = `https://dog.ceo/api/breed/${breed}/images/random`
              axios({
                method: 'get',
                url: dogImageUrl,
              })
                .then((response) => {
        
                  // console.log(response)
                  const imgSrc = response.data.message
                  this.imgSrc = imgSrc
                })
                .catch((error) => {
                  // this.message = `${this.$route.params.breed}는 없는 품종입니다.`
                  this.$router.push('/404')
                  console.log(error)
                })
            }
          },
          created() {
            this.getDogImage()
          }
        }
        </script>
        ```
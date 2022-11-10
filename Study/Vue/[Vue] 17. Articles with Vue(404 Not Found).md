# Articles with Vue(404 Not Found)

- 구현 기능
    - Index
    - Create
    - Detail
    - Delete
    - **404 Not Found**

## 404 Not Found

- `article`이 존재하지 않을 경우 이동할 컴포넌트 작성

### 404 Not Found구현

- `NotFound404` 컴포넌트 및 라우터 작성
- `Detail`에 대한 `route`보다 먼저 등록해줘야 함
    - 또한, `/404`로 등록하면 404번째 게시글과 혼동할 수 있으니 부가적인 문자를 추가가 필요
    - 요청한 리소스가 존재하지 않는 경우 없는 `id`가 아닌 전혀 다른 요청에도 대비하여 `404 page`로 `redirect` 시킬 수 있도록 `(*)asterisk` 를 `routes`에 추가
        - **최하단에 작성해야 함**
    - `views/NotFound404.vue`
        
        ```jsx
        <template>
          <div>
            <h1>404 Not Found</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'NotFound404'
        }
        </script>
        ```
        
    - `router/index.js`
        
        ```jsx
        import NotFound404 from '../views/NotFound404.vue'
        
        const routes = [
          ...
          {
            path: '/404-not-found',
            name: 'NotFound404',
            component: NotFound404
          },
          {
            path: '/:id',
            name: 'detail',
            component: DetailView,
          },
          {
            path: '*',
            redirect: { name: 'NotFound404' }
          }
        ]
        ```
        
- `DetailView` 컴포넌트에 `id`에 해당하는 `article`이 없으면 404 페이지로 이동
    - `views/DetailView.vue`
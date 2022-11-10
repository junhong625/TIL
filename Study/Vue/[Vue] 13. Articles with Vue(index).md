# Articles with Vue(Index)

- 구현 기능
    - **Index**
    - Create
    - Detail
    - Delete
    - 404

## 사전 준비

- 프로젝트 시작

```jsx
vue create articles
cd articles
vue add vuex
vue add router
```

- `App.vue`는 아래 코드만 남김 (CSS 코드 유지)
    
    ```jsx
    <template>
      <div id="app">
        <router-view/>
      </div>
    </template>
    ```
    

## Index

- `articles`의 목록을 보여주는 `index` 페이지 작성

### Index 구현

- `state`
- 게시글의 필드는 `id, 제목, 내용, 생성일자`
- DB의 `AUTO INCREMENT`를 표현하기 위해 `article_id`를 추가로 정의해줌
- `store/index.js`
    
    ```jsx
    export default new Vuex.Store({
      state: {
        article_id: 3,
        articles: [
          {
            id: 1,
            title: 'title1',
            content: 'content1',
            createdAt: new Date().getTime(),
          },
          {
            id: 2,
            title: 'title2',
            content: 'content2',
            createdAt: new Date().getTime(),
          }
        ]
      },
    ```
    
- `IndexView` 컴포넌트 및 라우터 작성
    - `views/IndexView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Articles</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'IndexView',
        ```
        
    - `router/index.js`
        
        ```jsx
        import Vue from 'vue'
        import VueRouter from 'vue-router'
        import IndexView from '../views/IndexView.vue'
        
        Vue.use(VueRouter)
        
        const routes = [
          {
            path: '/',
            name: 'index',
            component: IndexView,
          },
        ```
        
- `state`에서 불러온 `articles` 출력하기
    - `views/IndexView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Articles</h1>
            {{ articles }}
          </div>
        </template>
        
        <script>
        export default {
          name: 'IndexView',
          computed: {
            articles() {
              return this.$store.state.articles
            }
          },
        }
        </script>
        ```
        
- `ArticleItem` 컴포넌트 작성
    - `ArticleItem.vue`
        
        ```jsx
        <template>
          <div>
          </div>
        </template>
        
        <script>
        export default {
          name: 'ArticleItem',
        }
        </script>
        ```
        
- `IndexView` 컴포넌트에서 `ArticleItem` 컴포넌트 등록 및 `props` 데이터 전달
    - `views/IndexView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Articles</h1>
            <ArticleItem 
              v-for="article in articles"
              :key="article.id"
              :article="article"
            />
          </div>
        </template>
        
        <script>
        import ArticleItem from '@/components/ArticleItem';
        
        export default {
          name: 'IndexView',
          components: {
            ArticleItem,
          },
          computed: {
            articles() {
              return this.$store.state.articles
            }
          },
        }
        </script>
        ```
        
- `props` 데이터 선언 및 게시글 출력
    - `components/ArticleItem.vue`
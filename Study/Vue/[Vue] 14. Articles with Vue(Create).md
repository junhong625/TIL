# Articles with Vue(Create)

- 구현 기능
    - Index
    - **Create**
    - Detail
    - Delete
    - 404

## Create

- `articles`을 생성하는 `create` 페이지 작성

### Create 구현

- CreateView 컴포넌트 및 라우터 작성
    - `views/CreateView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>게시글 작성</h1>
          </div>
        </template>
        
        <script>
        export default {
          name: 'CreateView',
        }
        </script>
        ```
        
    - `router/index.js`
        
        ```jsx
        import Vue from 'vue'
        import VueRouter from 'vue-router'
        import IndexView from '../views/IndexView.vue'
        import CreateView from '../views/CreateView.vue'
        
        Vue.use(VueRouter)
        
        const routes = [
          ...
          {
            path: '/create',
            name: 'create',
            component: CreateView,
          },
        ]
        ```
        
- Form 생성 및 데이터 정의
    - `v-on:{event}.prevent`를 활용하여 `submit` 이벤트 동작을 취소하기
    - `v-model.trim`을 활용하여 입력 값의 공백을 제거
    - `CreateView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>게시글 작성</h1>
            <form>
              <label for="title">제목 : </label>
              <input type="text" id ="title" v-model="title"><br>
              <label for="content">내용 : </label>
              <textarea 
                id="content" cols="30" rows="10"
                v-model.trim="content"  
              ></textarea><br>
              <input type="submit">
            </form>
          </div>
        </template>
        
        <script>
        export default {
          name: 'CreateView',
          data() {
            return {
              title: null,
              content: null,
            }
          },
        }
        </script>
        ```
        
- `actions`에 여러 개의 데이터를 넘길 때 하나의 `object`로 만들어서 전달
    - 데이터가 없는 경우 `alert` & 데이터가 있는 경우 `actions`로 전달
    - 게시글 생성 후 Index 페이지로 이동하도록 네비게이터 작성
    - `views/CreateView.vue`
        
        ```jsx
        <script>
        export default {
          ...
          methods: {
            createArticle() {
              const title = this.title
              const content = this.content
              if (!title) {
                alert('제목을 입력해주세요!')
              } else if (!content) {
                alert('내용을 입력해주세요!')
              } else {      
                const payload = {
                  title, content
                }
                .this.$store.dispatch('createArticle', payload)
                .this.$store.push({ name: 'index'})
            }
          }
        }
        </script>
        ```
        
- `actions`에서는 넘어온 데이터를 활용하여 `article` 생성 후 `mutations` 호출
    - 이때 `id`로 `article_id` 활용
    - `views/CreateView.vue`
        
        ```jsx
        import Vue from 'vue'
        import Vuex from 'vuex'
        
        Vue.use(Vuex)
        
        export default new Vuex.Store({
          ...
          mutations: {
            CREATE_ARTICLE(state, article) {
              state.articles.push(article)
              state.article_id = state.article_id + 1
            },
          },
          actions: {
            createArticle(context, payload) {
              const article = {
                id: context.state.article_id,
                title: payload.title,
                content: payload.content,
                createdAt: new Date().getTime(),
              }
              context.commit('CREATE_ARTICLE', article)
            }
          },
          modules: {
          }
        })
        ```
        
- `CreateView` 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가
    - `views/CreateView.vue`
        
        ```jsx
        <template>
          <div>
            ...
            <router-link :to="{ name: 'index' }">뒤로가기</router-link>
          </div>
        </template>
        ```
        
- `IndexView` 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가
    - `views/IndexView.vue`
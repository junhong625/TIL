# Articles with Vue(Delete)

- 구현 기능
    - Index
    - Create
    - Detail
    - **Delete**
    - 404

## Delete

- `article`을 삭제하는 `delete` 버튼 생성

### Delete 구현

- `DetailView` 컴포넌트에 삭제 버튼을 만들고 `mutations`를 호출
    - 굳이 `actions`에서 작업을 할 필요가 없으니 바로 `mutations`를 호출하여 작업 수행
    - `views/DetailView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Detail</h1>
            ...
            <button @click="deleteArticle">삭제</button><br>
            <router-link :to="{ name: 'index' }">뒤로가기</router-link>
          </div>
        </template>
        
        <script>
        export default {
          ...
          methods: {
            ...
            deleteArticle() {
              this.$store.commit('DELETE_ARTICLE', this.article.id)
              this.$router.push({ name: 'index'})
            }
          },
          created() {
            this.getArticleById(this.$route.params.id)
          }
        }
        </script>
        ```
        
- `mutations`에서 `id`에 해다하는 게시글을 삭제
    - `store/index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          mutations: {
            ...
            DELETE_ARTICLE(state, id) {
              state.articles = state.articles.filter((article) => {
                return !(article.id === id)
              })
            }
          },
          ...
        })
        ```
        
- 삭제 후 `Index` 페이지로 이동하도록 네비게이션 작성
    - `views/DetailView.vue`
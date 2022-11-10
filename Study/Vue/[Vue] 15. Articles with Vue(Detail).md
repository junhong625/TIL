# Articles with Vue(Detail)

- 구현 기능
    - Index
    - Create
    - **Detail**
    - Delete
    - 404

## Detail

- `articles`상세 페이지로 이동하는 `detail` 페이지 작성

### Detail 구현

- `DetailView` 컴포넌트 및 라우터 작성
    - `id`를 동적 인자로 전달
    - `views/DetailView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Detail</h1>
            <p>글 번호 : {{ article.id }}</p>
            <p>글 제목 : {{ article.title }}</p>
            <p>글 내용 : {{ article.content }}</p>
            <p>글 작성시간 : {{ articleCreatedAt }}</p>
          </div>
        </template>
        
        <script>
        export default {
          name: 'DetailView',
        }
        </script>
        ```
        
    - `router/index.js`
        
        ```jsx
        ...
        import DetailView from '../views/DetailView.vue'
        
        Vue.use(VueRouter)
        
        const routes = [
          ...
          {
            path: '/:id',
            name: 'detail',
            component: DetailView,
          },
        ]
        ```
        
- `article` 정의 및 `state`에서 `articles` 가져오기
    - `views/DetailView.vue`
        
        ```jsx
        <script>
        export default {
          name: 'DetailView',
          data() {
            return {
              article: null,
            }
          },
          computed: {
            articles() {
              return this.$store.state.articles
            },
          },
        ```
        
- `articles`에서 동적인자를 통해 받은 `id`에 해당하는 `article` 가져오기
    - 이때 동적인자를 통해 받은 `id`는 `str`이므로 형변환을 해서 비교
    - `views/DetailView.vue`
        
        ```jsx
        methods: {
            getArticleById(id) {
              for (const article of this.articles) {
                if (article.id === Number(id)) {
                  this.article = article
                  break
                }
              }
            },
        ```
        
- `created lifecycle hook`을 통해 인스턴스가 생성되었을 때 `article`을 가져오는 함수 호출
    - `views/DetailView.vue`
        
        ```jsx
        <script>
        export default {
          name: 'DetailView',
          ...
          created() {
            this.getArticleById(this.$route.params.id)
          }
        }
        </script>
        ```
        
- `optional chaining(?.)`을 통해 `article`객체가 있을 때만 출력되도록 수정
    - `optional chaining(?.)`
        - 앞의 평가 대상이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환
    - ex) `views/DetailView.vue`
        
        ```jsx
        <template>
          <div>
            <h1>Detail</h1>
            <p>글 번호 : {{ article?.id }}</p>
            <p>글 제목 : {{ article?.title }}</p>
            <p>글 내용 : {{ article?.content }}</p>
            <p>글 작성시간 : {{ article?.createdAt }}</p>
          </div>
        </template>
        ```
        
- 뒤로가기 링크 추가
    - `views/DetailView.vue`
        
        ```
        <template>
          <div>
            ...
            <router-link :to="{ name: 'index' }">뒤로가기</router-link>
          </div>
        </template>
        ```
        
- 각 게시글을 클릭하면 `detail`페이지로 이동하도록 `ArticleItem`에 이벤트 추가
    - `v-on` 이벤트 핸들러에도 인자 전달 가능
    - `components/ArticleItem.vue`
        
        ```jsx
        <template>
          <div @click="goDetail(article.id)">
            <p>글 번호 : {{ article.id }}</p>
            <p>제목 : {{ article.title }}</p>
            <hr>
          </div>
        </template>
        
        <script>
        export default {
          name: 'ArticleItem',
          props: {
            article:Object
          },
          methods: {
            goDetail(id) {
              this.$router.push({ name:'detail', params: {id}})
              // this.$router.push({ name:'detail', params: {id: `${this.article.id}`}})
            }
          }
        }
        </script>
        ```
        

### Date in JavaScript

- `JavaScript`에서 시간을 나타내는 `Date`객체는 1970년 1월 1일 UTC(협정 세계시) 자정과의 시간 차이를 밀리초로 나타내는 정수 값을 담음
    - `Date().toLocaleString()`을 사용하여 변환
- 로컬 시간으로 변환해주는 `computed` 값 작성 및 출력
    - `viewsDetailView.vue`
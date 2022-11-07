# Local Storage

> 브라우저의 `Local Storage`에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터를 보존
> 

## Local Stoarge 속성값

### window.localStorage

- 브라우저에서 제공하는 저장공간 중 하나인 `Local Storage`에 관련된 속성
- 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
- 데이터가 문자열 형태로 저장됨
- 관련 메서드
    - `setItem(key, value)` - key, value 형태로 데이터 저장
    - `getItem(key, value)` - key에 해당하는 데이터 조회

## Local Storage 실습

- todos 배열을 `Local Storage`에 저장하기
- 데이터가 문자열 형태로 저장되어야 하기 때문에 `JSON.stringify`를 사용해 문자열로 변환해주는 과정 필요
- `state`를 변경하는 작업이 아니기 때문에 `mutations`가 아닌 `actions`에 작성
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          actions: {
            ...
            loadTodos(context) {
              context.commit('LOAD_TODOS')
            }
          },
          modules: {
          }
        })
        ```
        
- todo 생성, 삭제, 수정 시에 모두 `saveTodosToLocalStorage` `action` 메서드가 실행 되도록 함
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          actions: {
            createTodo(context, todoTitle) {
              // Todo 객체 만들기
              const todoItem = {
                title: todoTitle,
                isCompleted: false,
              }
              context.commit('CREATE_TODO', todoItem)
              context.dispatch('saveTodosToLocalStorage')
            },
            deleteTodo(context, todoItem) {
              context.commit('DELETE_TODO', todoItem)
              context.dispatch('saveTodosToLocalStorage')
            },
            updateTodoStatus(context, todoItem) {
              context.commit('UPDATE_TODO_STATUS', todoItem)
              context.dispatch('saveTodosToLocalStorage')
            },
            saveTodosToLocalStorage(context) {
              const jsonTodos = JSON.stringify(context.state.todos)
              localStorage.setItem('todos', jsonTodos)
            },
          },
          modules: {
          }
        })
        ```
        
- 개발자 도구 - `Application` - `Storage` - `Local Storage` 에서 todos 생성 확인
- 불러오기 버튼 작성
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            ...
            <button @click="loadTodos">불러오기</button>
          </div>
        </template>
        ```
        
- `loadTodos` 작성
    - `App.vue`
        
        ```jsx
        <script>
        import TodoList from '@/components/TodoList'
        import TodoForm from '@/components/TodoForm'
        
        export default {
          name: 'App',
          components: {
            TodoList,
            TodoForm,
          },
          ...
          methods: {
            loadTodos() {
              this.$store.dispatch('loadTodos')
            }
          },
        ...
        ```
        
- `loadTodos` `action` 메서드 작성
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          actions: {
            ...
            loadTodos(context) {
              context.commit('LOAD_TODOS')
            }
          },
          modules: {
          }
        })
        ```
        
- `LOAD_TODOS` `mutation` 메서드 작성
- 문자열 데이터를 다시 object 타입으로 변환(`JSON.parse`)하여 저장
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          mutations: {
            ...
            LOAD_TODOS(state) {
              const localStorageTodos = localStorage.getItem('todos')
              const parsedTodos = JSON.parse(localStorageTodos)
              state.todos = parsedTodos
            },
          },
        ```
        

## vuex-persistedstate

- `Vuex state`를 자동으로 브라우저의 `Local Storage`에 저장해주는 라이브러리 중 하나
- 페이지가 새로고침 되어도 `Vuex state`를 유지시킴
- `Local Storage`에 저장된 `data`를 자동으로 `state`로 불러옴

### 설치

```jsx
npm i vuex-persistedstate
```

### 적용

- `index.js`
    
    ```jsx
    import createPersistedState from 'vuex-persistedstate'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      plugins: [
        createPersistedState(),
      ],
      ...
    })
    ```
    

### 주석처리

> `vuex-persistedstate`를 통해 대체할 기능들을 모두 주석처리
> 
- `App.vue`
    - 불러오기 버튼
    
    - `loadTodos` 메서드
- `index.js`
    - `LOAD_TODOS mutation` 메서드
    - `saveTodosToLocalStorage action` 메서드
    - `loadTodos action` 메서드
    - `context.dispatch('saveTodoToLocalStorage')` 코드 3줄
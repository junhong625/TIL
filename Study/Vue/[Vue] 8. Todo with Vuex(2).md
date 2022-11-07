# Todo with Vuex (2)

## 상태별 todo 개수 계산

### 전체 todo 개수

- `allTodosCount` `getters` 작성
- `state`에 있는 `todos` 배열의 길이 계산
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          getters: {
            allTodosCount(state) {
              return state.todos.length
            }
          },
        ```
        
- `getters`에 계산된 값을 각 컴포넌트의 `computed`에서 사용하기
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>Todo List</h1>
            <h2>모든 Todo 개수: {{ allTodosCount }}</h2>
            <TodoList/>
            <TodoForm/>
          </div>
        </template>
        
        <script>
          ...
          },
          computed: {
            allTodosCount() {
              return this.$store.getters.allTodosCount
            },
          }
        }
        </script>
        ```
        

### 완료된 todo 개수

- `completedTodosCount` `getters` 작성
- `isCompleted`가 true인 todo들만 필터링한 배열을 만들고 길이 계산
- `filter`를 활용하여 완료 여부에 따른 새로운 객체 목록을 작성 후 길이 반환
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          state: {
            todos: []
          },
          getters: {
            allTodosCount(state) {
              return state.todos.length
            },
            completedTodosCount(state) {
              const completedTodos = state.todos.filter((todo) => {
                return todo.isCompleted
              })
              return completedTodos.length
            },
          }
        })
        ```
        
- `getters`에 계산된 값을 각 컴포넌트의 `computed`에서 사용
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>Todo List</h1>
            <h2>완료된 Todo 개수: {{ completedTodosCount }}</h2>
            <TodoList/>
            <TodoForm/>
          </div>
        </template>
        
        <script>
        import TodoList from '@/components/TodoList'
        import TodoForm from '@/components/TodoForm'
        
        export default {
          name: 'App',
          components: {
            TodoList,
            TodoForm,
          },
          computed: {
            completedTodosCount() {
              return this.$store.getters.completedTodosCount
            },
          }
        }
        </script>
        ```
        

### 미완료된 todo 개수

- 미완료된 todo 개수 === 전체 개수 - 완료된 개수
- `getters`가 두번째 인자로 `getters`를 받는 것을 활용하기
- `unCompletedTodosCount` `getters` 작성
    - `index.js`
        - 
        
        ```
        export default new Vuex.Store({
          state: {
            todos: []
          },
          getters: {
            unCompletedTodosCount(state, getters) {
              return getters.allTodosCount - getters.completedTodosCount
            }
          },
        ```
        
- `getters`에 계산된 값을 각 컴포넌트의 `computed`에서 사용
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>Todo List</h1>
            <h2>미완료된 Todo 개수: {{ unCompletedTodosCount }}</h2>
            <TodoList/>
            <TodoForm/>
          </div>
        </template>
        
        <script>
        import TodoList from '@/components/TodoList'
        import TodoForm from '@/components/TodoForm'
        
        export default {
          name: 'App',
          components: {
            TodoList,
            TodoForm,
          },
          computed: {
            unCompletedTodosCount() {
              return this.$store.getters.unCompletedTodosCount
            },
          }
        }
        </script>
        ```
# Todo with Vuex (1)

## 구현 기능

- Todo CRUD
- Todo 개수 계산
    - 전체 Todo
    - 완료된 Todo
    - 미완료된 Todo

## Init Project

1. 프로젝트 생성 및 `vuex` 플러그인 추가
    
    ```jsx
    vue create todo-vuex-app
    cd todo-vuex-app
    vue add vuex
    ```
    
2. HelloWorld 컴포넌트 및 관련 코드 삭제
    - `App.vue`의 CSS 코드는 남김

## 컴포넌트 작성

- `TodoListItem.vue`
    
    ```jsx
    <template>
      <div>Todo</div>
    </template>
    
    <script>
    export default {
      name: 'TodoListItem',
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- `TodoList.vue`
    
    ```jsx
    <template>
      <div>
        <TodoListItem/>
      </div>
    </template>
    
    <script>
    import TodoListItem from '@/components/TodoListItem';
    
    export default {
      name: 'TodoList',
      components: {
        TodoListItem,
      }
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- `TodoForm.vue`
    
    ```jsx
    <template>
      <div>Todo Form</div>
    </template>
    
    <script>
    export default {
      name: 'TodoForm'
    }
    </script>
    
    <style>
    
    </style>
    ```
    
- `App.vue`
    
    ```jsx
    <template>
      <div id="app">
        <h1>Todo List</h1>
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
      }
    }
    </script>
    ```
    

## Read Todo

### State 세팅

- 출력을 위한 기본 todo 작성
- `index.js`
    
    ```jsx
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        todos: [
            {
              title: '할 일 1',
              isCompleted: false,
            },
            {
              title: '할 일 2',
              isCompleted: false,
            },
        ]
      ...
    })
    ```
    

### State 데이터 가져오기

- 컴포넌트에서 `Vuex Store`의 `state`에 접근(`$store.state`)
- `computed`로 계산된 todo 목록을 가져올 수 있도록 설정
- `TodoList.vue`

```jsx
<template>
  <div>
    <TodoListItem
      v-for="(todo, index) in todos"
      :key="index"
      :todo="todo"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem';

export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    }
  }
}
</script>
```

- `v-for`의 key는 배열의 각 요소 간의 유일한 식별자 값을 사용해야 하지만 `vuex` 흐름에 집중하기 위해 index를 key로 사용

### Pass Props

- `TodoList.vue` → `TodoListItem.vue`
- todo 데이터 내려받기
- `TodoListItem.vue`
    
    ```jsx
    <template>
      <div>{{ todo.title }}</div>
    </template>
    
    <script>
    export default {
      name: 'TodoListItem',
      props: {
        todo: Object,
      }
    }
    </script>
    ```
    

## Create Todo

### Todo Form

- `todoTitle`을 입력 받을 `input`태그 생성
- `todoTitle`을 저장하기 위해 `data`를 정의하고 `input`과 `v-model`을 이용해 양방향 바인딩
- `enter` 이벤트를 사용해 `createTodo`메서드 출력 확인
- `TodoForm.vue`
    
    ```jsx
    <template>
      <div>
        <input 
        type="text"
        v-model="todoTitle"
        @keyup.enter="createTodo"
        >
      </div>
    </template>
    
    <script>
    export default {
      name: 'TodoForm',
      data() {
        return {
          todoTitle: null,
        }
      },
    }
    </script>
    ```
    

### Actions

- `createTodo` 메서드에서 `actions`를 호출(`dispatch`)
- `todoTitle`까지 함께 전달하기
    - `TodoForm.vue`
        
        ```
        <template>
          <div>
            <input 
            type="text"
            v-model="todoTitle"
            @keyup.enter="createTodo"
            >
          </div>
        </template>
        
        <script>
        export default {
          name: 'TodoForm',
          data() {
            return {
              todoTitle: null,
            }
          },
          methods: {
            createTodo() {
              console.log(this.todoTitle)
              this.$store.dispatch('createTodo', this.todoTitle)
              this.todoTitle = null
            }
          }
        }
        </script>
        ```
        
- `actions`에는 보통 비동기 관련 작업이 진행 되지만 현재 별도의 비동기 관련 작업이 불필요하기 때문에 입력 받은 todo 제목(`todoTitle`)을 todo 객체(`todoItem`)로 만드는 과정을 `Actions`에서 작성할 예정
- `createTodo`에서 보낸 데이터를 수신 후 `todoItem object`를 생성
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          state: {
            todos: []
          },
          ...
          actions: {
            createTodo(context, todoTitle) {
              // Todo 객체 만들기
              const todoItem = {
                title: todoTitle,
                isCompleted: false,
              }
          ...
          }
        })
        ```
        

### mutations

- `CREATE_TODO` `mutations` 메서드에 `todoItem`을 전달하며 호출(`commit`)
    - `index.js`
        
        ```
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
            }
          },
          modules: {
          }
        })
        ```
        
- `mutations`에서 `state`의 `todos`에 접근해 배열에 요소를 추가
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          },
          mutations: {
            CREATE_TODO(state, todoItem) {
              state.todos.push(todoItem)
            }
          }
        })
        ```
        

## Delete Todo

### TodoListItem

- `TodoListItem` 컴포넌트에 삭제 버튼 및 `deleteTodo` 메서드 작성
    - `TodoListItem.vue`
        
        ```jsx
        <template>
          <div>
            {{ todo.title }}
            <button @click="deleteTodo">Delete</button>
          </div>
        </template>
        
        <script>
        export default {
          name: 'TodoListItem',
          props: {
            todo: Object,
          },
          methods: {
            deleteTodo() {
              console.log('삭제 메서드 호출')
            }
          }
        }
        </script>
        ```
        

### Actions

- `deleteTodo` 메서드에서 `deleteTodo actions` 메서드 호출(`dispatch`)
- 삭제되는 `todo`를 함께 전달
    - `TodoListItem.vue`
        
        ```jsx
        <template>
          <div>
            {{ todo.title }}
            <button @click="deleteTodo">Delete</button>
          </div>
        </template>
        
        <script>
        export default {
          name: 'TodoListItem',
          props: {
            todo: Object,
          },
          methods: {
            deleteTodo() {
              console.log('삭제 메서드 호출')
              this.$store.dispatch('deleteTodo', this.todo)
              // this.$store.commit('DELETE_TODO', this.todo)
            }
          }
        }
        </script>
        ```
        
- `deleteTodo actions` 메서드에서 `DELETE_TODO` `mutations` 메서드 호출(`commit`)
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
            },
            deleteTodo(context, todoItem) {
              context.commit('DELETE_TODO', todoItem)
          }
          ...
        })
        ```
        

### Mutations

- `DELETE_TODO` 메서드 작성
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          mutations: {
            CREATE_TODO(state, todoItem) {
              state.todos.push(todoItem)
            },
            DELETE_TODO(state, todoItem) {
              console.log(todoItem)
            }
          }
        }
        ```
        
- 전달된 `todoItem`에 해당하는 todo 삭제
- 작성 후 삭제 테스트
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          mutations: {
            CREATE_TODO(state, todoItem) {
              state.todos.push(todoItem)
            },
            DELETE_TODO(state, todoItem) {
              const index = state.todos.indexOf(todoItem)
              state.todos.splice(index, 1)
            }
          },
        ```
        

## Update Todo

### TodoListItem

- todo를 클릭하면 완료 표시의 의미로 취소선 스타일을 적용하는 기능 구현
    - 즉, todo의 `isCompleted` 값 토글하기
- `TodoListItem` 컴포넌트에 클릭 이벤트를 추가 후 관련 `actions` 메서드 호출
    - `TodoListItem.vue`
        
        ```jsx
        <template>
          <div>
            <span 
              @click="updateTodoStatus"
            >{{ todo.title }}</span>
            <button @click="deleteTodo">Delete</button>
          </div>
        </template>
        
        <script>
        export default {
          name: 'TodoListItem',
          props: {
            todo: Object,
          },
          methods: {
            ...
            updateTodoStatus() {
              this.$store.dispatch('updateTodoStatus', this.todo)
            }
          }
        }
        </script>
        ```
        

### Actions

- `updateTodoStatus` 메서드 작성
- 관련 `mutations` 메서드 호출
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
            },
            deleteTodo(context, todoItem) {
              context.commit('DELETE_TODO', todoItem)
            },
            updateTodoStatus(context, todoItem) {
              context.commit('UPDATE_TODO_STATUS', todoItem)
            }
          },
          ...
        })
        ```
        

### Mutations

- `UPDATE_TODO_STATUS` 메서드 작성
- `map`메서드를 활용해 선택된 todo의 `isCompleted`를 반대로 변경 후 기존 배열 업데이트
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          mutations: {
            ...
            UPDATE_TODO_STATUS(state, todoItem) {
              state.todos = state.todos.map((todo) => {
                if (todo === todoItem) {
                  todo.isCompleted = !todo.isCompleted
                }
                return todo
              })
            }
          },
        })
        ```
# Vuex

## State Management

- Web 에서의 **상태(state)란?**
    - 현재 **앱이 가지고 있는 정보(data)**
- 각 component는 독립적이기 때문에 각각의 상태(data)를 가짐
- 이 component들이 모여 하나의 App을 구성
    - 즉, 여러 개의 component가 같은 상태(data)를 유지할 필요가 있음
    → 상태 관리(State Management) 필요!

### Pass Props & Emit Event

- **props와 event를 이용하여 상태 관리를 할 경우**
    - 같은 데이터를 공유하고 있으며, 각 컴포넌트는 독립적으로 데이터를 관리
    - 데이트의 흐름 직관적으로 파악 가능
    - 그러나 `component`의 중첩이 깊어지면 데이터 전달이 쉽지 않음
    - 이를 해결하기 위해 등장한 것이 `Vuex`

### Centralized Store

- 중앙 저장소(store)에 데이터를 모아서 상태 관리
- 각 component는 중앙 저장소의 데이터를 사용
- component의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
- 중앙 저장소의 데이터가 변경되면 각각의 component는 해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영함
- 규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

### Vuex

- `state management pattern + Library` for vue.js
(상태 관리 패턴 + 라이브러리)
- 중앙 저장소를 통해 관리를 할 수 있도록 하는 라이브러리
- 데이터가 예측 가능한 방식으로만 변경 될 수 있도록 하는 **규칙을 설정**, `Vue`의 반응성을 효율적으로 사용하는 **상태 관리 기능을 제공**
- `Vue`의 공식 도구로써 다양한 기능을 제공
- `Vuex`에서도 여전히 `pass props, emit event`를 사용하여 상태 관리 가능

## Vuex

### Vuex 시작

```bash
vue create vuex-app    // Vue 프로젝트 생성
cd vuex-app            // 디렉토리 이동
vue add vuex           // Vue CLI를 통해 vuex plugin 적용
```

- **vuex-app**
    - `src` / `store` / `index.js` 가 생성됨
    - vuex의 핵심 컨셉 4가지
        1. `state` == `Vue axios의 'data'`
        2. `getters` == `Vue axios의 ‘gettrs’`
        3. `mutations` == `Vue axios의 ‘methods' (1)`
        4. `actions` == `Vue axios의 ‘methods' (2)`
    

### Vuex의 흐름

- `component`에서 데이터를 조작하기 위한 데이터의 흐름
    - `component ⇒ (actions) ⇒ mutations ⇒ state`
- `component`에서 데이터를 사용하기 위한 데이터의 흐름
    - `state => (getters) => component`

### 1. state

- `vue instance`의 `data`에 해당
- **중앙에서 관리하는 모든 상태 정보**
- 개별 component는 `state`에서 데이터를 가져와서 사용
    - 개별 component가 관리하던 `data`를 `중앙 저장소(Vuex Store의 state)`에서 관리하게 됨
- `state`의  데이터가 변화하면 해당 데이터를 사용(공유)하는 component가 자동으로 다시 렌더링
- `$store.state`로 `state` 데이터에 접근 가능

### 2. mutations

- **실제로 state를 변경하는 유일한 방법**
- `vue instance`의 `methods`에 해당하지만 `Mutations`에서 호출되는 핸들러(handler) 함수는 반드시 **동기적**이어야 함
    - 비동기 로직으로 `mutations`를 사용해서 `state`를 변경하는 경우, `state`의 변화의 시기를 특정할 수 없기 때문
- 첫 번째 인자로 `state`를 받으며, component 혹은 `Actions`에서 `commit()`메서드로 호출됨
- **mutation, action에서 호출되는 함수를 `handler 함수`라고 함**

### 3. actions

- **state 변경을 제외한 나머지 로직**
- `mutations`와 비슷하지만 **비동기** 작업을 포함할 수 있다는 차이가 있음
- `state`를 직접 변경하지 않고 `commit()`메서드로 `mutations`를 호출해서 `state`를 변경함
- `context` 객체를 인자로 받으며, 이 객체를 통해 `store.js`의 모든 요소와 메서드에 접근할 수 있음
(즉, `state`를 직접 변경이 가능하지만 그렇게 해서는 안됨)
- component에서 `dispatch()`메서드에 의해 호출됨

### 4. getters

- **state를 활용하여 계산된 값을 얻고자 할 때 사용**
    - `state`의 원본 데이터를 건들이지 않고 계산된 값을 얻을 수 있음
- `vue instance`의 `computed`에 해당
- `computed`와 마찬가지로 `getters`의 결과는 캐치(cache) 되며, 종속된 값이 변경된 경우에만 재계산
- `getters`에서 계산된 값은 state에 영향을 미치지 않음
- 첫번째 인자로 `state`, 두 번째 인자로 `getter`를 받음

## Vuex 작성

### state

- 중앙에서 관리하는 모든 상태 정보
- `$stroe.state`로 접근 가능
- `store`의 `state`에 `message` 데이터 정의
    - `index.js`
        
        ```jsx
        // index.js
        
        import Vue from 'vue'
        import Vuex from 'vuex'
        
        Vue.use(Vuex)
        
        export default new Vuex.Store({
          state: {
            message: 'message in store'
          },
        ```
        
- `component`에서 `state` 사용
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>{{ $store.state.message }}</h1>
          </div>
        </template>
        
        <script>
        
        export default {
          name: 'App',
          components: {
          }
        }
        </script>
        ```
        
- `$store.state`로 바로 접근하기 보다 `computed`에 정의 후접근하는 것을 권장
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>{{ message }}</h1>
          </div>
        </template>
        
        <script>
        
        export default {
          name: 'App',
          components: {
          },
          computed: {
            message() {
              return this.$store.state.message
            }
          }
        }
        </script>
        ```
        

### actions

- `state`를 변경할 수 있는 `mutations` 호출
- `component`에서 `dispatch()`에 의해 호출됨
- `dispatch(A, B)`
    - A : 호출하고자 하는 actions 함수
    - B : 넘겨주는 데이터(payload)
- `actions`에 정의된 `chageMessage` 함수에 데이터 전달하기
- `component`에서 `actions`는 `dispatch()`에 의해 호출됨
    - `App.vue`
        
        ```jsx
        <template>
          <div id="app">
            <h1>{{ message }}</h1>
            <input 
              type="text"
              @keyup.enter="changeMessage"
              v-model="inputData"
            >
          </div>
        </template>
        
        <script>
        
        export default {
          name: 'App',
          data() {
            return {
              inputData: null,
            }
          },
          components: {
          },
          computed: {
            message() {
              return this.$store.state.message
            }
          },
          methods: {
            changeMessage() {
              const newMessage = this.inputData
              this.$store.dispatch('changeMessage', newMessage)
            }
          }
        }
        </script>
        ```
        
- `actions`의 첫 번째 인자는 `context`
    - `context`
        - `store`의 전반적인 속성을 모두 가지고 있으며 `context.state`와 `context.getters`를 통해 `mutations`를 호출하는 것이 모두 가능
        - `dispatch()`를 사용해 다른 `actions`도 호출할 수 있음
        - **단, `actions`에서 `state`를 직접 조작하는 것은 삼가해야 함**
- `acionts`의 두번째 인자는 `payload`
    - 넘겨준 데이터를 받아서 사용
- `store/index.js`
    
    ```jsx
    import Vue from 'vue'
    import Vuex from 'vuex'
    
    Vue.use(Vuex)
    
    export default new Vuex.Store({
      state: {
        message: 'message in store'
      },
      getters: {
      },
      mutations: {
      },
      actions: {
        changeMessage(context, newMessage) {
          console.log(context)
          console.log(newMessage)
        }
      },
      modules: {
      }
    })
    ```
    

### mutations

- `mutations`는 `state`를 변경하는 유일한 방법
- `component` 또는 `actions`에서 `commit()`에 의해 호출됨
- `commit(A, B)`
    - A : 호출하고자 하는 `mutations`함수
    - B : `payload`
- `actions`에서 `commit()`으로 `mutations` 호출
    - `index.js`
        
        ```jsx
        export default new Vuex.Store({
          ...
          actions: {
            changeMessage(context, newMessage) {
              // console.log(context)
              // console.log(newMessage)
              context.commit('CHANGE_MESSAGE', newMessage) // mutation 호출
            }
          ...
        })
        ```
        
- `mutations` 함수 작성하기
- `mutations`의 첫 번째 인자는 `state`
- `mutations`의 두 번째 인자는 `payload`
- `mutations`는 `state`를 변경하는 유일한 방법
    - `index.js`
        
        ```
        export default new Vuex.Store({
          ...
          mutations: {
            CHANGE_MESSAGE(state, newMessage) {
              console.log(state)
              console.log(newMessage)
              state.message = newMessage
            }
          },
          ...
        })
        ```
        

### getters

- `getters`는 `state`를 활용한 새로운 변수
- `getters`함수의 첫 번째 인자는 `state`
- `getters`함수의 첫 번째 인자는 `getters`
- `index.js`
    
    ```jsx
    export default new Vuex.Store({
      ...
      },
      getters: {
        messageLength(state) {
          return state.message.length
        }
      },
      ...
    })
    ```
    
- `App.vue`
    
    ```jsx
    <template>
      <div id="app">
        <h1>{{ message }}</h1>
        <h2>문자 길이 : {{ messageLength }}</h2>
        <input 
          type="text"
          @keyup.enter="changeMessage"
          v-model="inputData"
        >
      </div>
    </template>
    
    <script>
    
    export default {
      ...
      computed: {
        message() {
          return this.$store.state.message
        },
        messageLength() {
          return this.$store.getters.messageLength
        }
      },
      ...
    }
    </script>
    ```
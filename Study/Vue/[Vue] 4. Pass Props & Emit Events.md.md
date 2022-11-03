# Pass Props & Emit Events

## Data in components

- 현재 목표는 정적 웹페이지가 아닌 동적 웹페이지
- 한 페이지 내에서 같은 데이터를 공유해야 함
    - 하지만 페이지들은 `component`로 구분 되어있음
- `MyComponent`에 정의된 data를 `MyChild`에서 사용하기 위해선?
- 컴포넌트는 부모 -자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고 받도록 구성
    - 데이터의 흐름을 파악하기 용이
    - 유지 보수하기 쉬움
- `부모 ⇒ 자식` 데이터 흐름
    - `pass props`(데이터)의 방식
- `자식 ⇒ 부모` 데이터 흐름
    - `emit event`(이벤트)의 방식

## Pass Props

- 요소의 속성(property)을 사용하여 데이터 전달
- `props`는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 `props` 옵션을 사용하여 수신하는 `props`를 명시적으로 선언해야 함
- 정적인 데이터를 전달하는 경우 `static props`라고 명시하기도 함
- 요소에 속성을 작성하듯이 사용 가능하여, `prop-data-name="value"`의 형태로 데이터를 전달
    - 이때 속성의 키 값은 `kebab-case`를 사용
        - html의 속성에 해당하는 형태이기에 `kebab-case`를 사용
        - 이때 `prop`을 받는 `vue`는 `JS`기반이기에  `camel-case`를 사용
- **props 전송(부모에서 넘겨주는 props)**
    - `kebab-case`
    
    ```jsx
    <!-- App.vue -->
    <template>
      <div id="app">
        <img alt="Vue logo" src="./assets/logo.png">
        <!-- 3. 보여주기 -->
        <MyComponent/>
        <HelloWorld msg-title="Welcome to Your Vue.js App!!!"/>
      </div>
    </template>
    ```
    
- **props 수신(자식에서 받는 props)**
    - `camelCase`
    
    ```jsx
    // HelloWorld.vue
    <script>
    export default {
      name: 'HelloWorld',
      props: {
        msgTitle: String
      }
    }
    </script>
    ```
    
- 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 `props`에 대해 명시적으로 작성 해주어야 함
- 전달받은 `props`를 type과 함께 명시
- 컴포넌트를 문서화할 뿐만 아니라, 잘못된 타입을 전달하는 경우 브라우저의 자바스크립트 콘솔에서 사용자에게 경고

### Dynamic props

- 변수를 `props`로 전달할 수 있음
- `v-bind directive(:)`를 사용해 데이터를 동적으로 바인딩
- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨
- **props 전송(부모에게 넘겨주는 props)**

```jsx
<template>
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem :dynamic-props="dynamicProps"/>
  </div>
</template>
<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터!',
    }
  },
</script>
```

- **props 수신(자식에게 넘겨주는 props)**

```
<template>
  <div>
    <p>{{ dynamicProps }}</p>
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    dynamicProps: String,
  },
```

### 컴포넌트의 data 함수

- 각 `vue instance`는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함

```jsx
data: function() {
  return {
    word: '예시' 
  }
}
```

### 퀴즈

- 1, 2번 중 숫자를 `props`로 전달하기 위한 방법은?

```jsx
// 1
<SomeComponent num-props="1"/>

// 2
<SomeComponent :num-props="1"/>
```

> 첫 번째 방식은 `static props`로 string “1”을 전달
두 번째 방식은 `dynamic props`로 숫자 1을 전달
> 

### 단방향 데이터 흐름

- 모든 `props`는 부모에서 자식으로 즉, 아래로 단방향 바인딩을 형성
- `부모 → 자식` 가능
`자식 → 부모` 불가능
    - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 `prop`들이 최신 값으로 새로고침 됨
- 이와 같이 설계한 이유
    - 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지

## Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생 시킴
- 이벤트를 발생시키는 게 어떻게 데이터를 전달하는 것이냐?
    1. 데이터를 이벤트 리스너의 **콜백함수의 인자로 전달**
    2. 상위 컴포넌트는 해당 **이벤트를 통해 데이터를 받음**

### $emit

- `$emit` 메서드를 통해 부모 컴포넌트에 이벤트를 발생
    - `$emit('event-name')` 형식으로 사용하며 부모 컴포넌트에 `event-name`이라는 이벤트가 발생했다는 것을 알림
    - 마치 사용자가 마우스 클릭을 하면 click 이벤트가 발생하는 것처럼 `$emit('event-name')`가 실행되면 `event-name`이벤트가 발생하는 것
- `$`
    - javascript는 변수에 `$`, `_` 두개의 특수문자를 사용 가능
    - 내장된 함수와 변수, 메서드와 이름이 겹치지 않게 하기 위해서 `$`가 붙어 있음

### 1. 자식에서 이벤트 발생

```jsx
<template>
  <div>
    <button @click="childToParent">클릭!</button>
  </div>
</template>
<script>
export default {
  ...
  methods: {
    childToParent: function() {
      this.$emit('child-to-parent', '자식이 보낸 데이터') // 'give-me' : 이름, '자식이 보낸 데이터' : 전송할 데이터
    }
  },
  ...
}
</script>
```

### 2. 부모에서 이벤트를 통해 데이터 수신

```jsx
<template>
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!</h1>
    <MyComponentItem @child-to-parent="parentGetEvent"/> // 자식에서 이벤트 give-me 이벤트가 발생 시 parentGetEvent 실행
    <h3>{{ childData }}</h3>
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    // 2. 등록하기
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '이건 동적인 데이터!',
      childData: null, // 자식에서 이벤트가 발생하면 데이터가 저장될 변수
    }
  },
  methods: {
    parentGetEvent: function(childData) {
      this.childData = childData // 이벤트가 발생 시 자식에서 온 데이터를 childData 변수에 할당
      console.log(childData)
    }
  }
}
</script>
```

### Emit Event 흐름 정리

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(`childToParent`) 호출
2. 호출된 함수에서 `$emit`을 통해 상위 컴포넌트에 이벤트(`child-to-parent`)발생
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(`child-to-parent`)를 청취하여 연결된 핸들러 함수(`parentGetEvent`) 호출

### Emit with data 흐름

1. 자식 컴포넌트에 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(`ChildToParent`) 호출
2. 호출된 함수에서 `$emit`을 통해 부모 컴포넌트에 이벤트(`child-to-parent`)를 발생
    - 이벤트에 데이터(`child data`)를 함께 전달
3. 부모 컴포넌트는 자식 컴포넌트의 이벤트 (`child-to-parent`)를 청취하여 연결된 핸들러 함수(`parentGetEvent`)호출, 
함수의 인자로 전달된 데이터(`child data`)가 포함되어 있음
4. 호출된 함수에서 `console.log(`~child data~`)`실행

### pass props / emit event 컨벤션

- **props `상위 ⇒ 하위`**
    - 상위 component 에서 HTML 요소로 전송 : `kebab-case`
    - 하위 component 에서 JavaScript 에서 수신 : `camel-case`
- **emit `하위 => 상위`**
    - 하위 component 에서 HTML 요소가 이벤트를 청취 : `kebab-case`
    - 메서드, 변수명 JavaScript에서 사용 시 : `camel-case`
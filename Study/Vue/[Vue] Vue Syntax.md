## Template Syntax

- `Vue2 guide` > `Template Syntax` 참고
- 렌더링 된 `DOM`을 기본 `Vue instance`의 `data`에 선언적으로 바인딩 할 수 있는 HTML 기반 `template syntax`를 사용
    - 렌더링 된 `DOM` : 브라우저에 의해 보기 좋게 그려질 HTML 코드
    - HTML 기반 `template syntax` : HTML 코드에 직접 작성할 수 있는 문법 제공
    - 선언적으로 바인딩 : `Vue instance`와 `DOM`을 연결

### Text Interpolation

- 가장 기본적인 바인딩(연결) 방법
- 중괄호 2개로 표기
- `DTL`과 동일한 형태로 작성
- `Text interpolation` 방법은 모두 일반 텍스트로 표현

```html
<body>
  <!-- 1. Text interpolation -->
  <div id="app">
    <p>메시지: {{ msg }}</p>   
    <p>HTML 메시지 : {{ rawHTML }}</p>
    <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>
	<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
	  <script>
	    // 1. Text interpolation
	    const app = new Vue({
	      el: '#app',
	      data: {
	        msg: 'Text interpolation',
	        rawHTML: '<span style="color:red"> 빨간 글씨</span>'
	      }
	    })
  </script>
</body>
```

## Directives

> `v-on:submit.prevent=”onSubmit”`
> 
- `v-접두사`가 있는 특수 속성에는 값을 할당 할 수 있음
    - 값에는 `JS` 표현식을 작성 할 수 있음
- `directive`의 역할은 **표현식의 값이 변경될 때** 반응적으로 `DOM`에 적용하는 것
- `v-on` : Name
- `submit` : argument
- `prevent` : Modifiers
- `"onSubmit"` : Value
- `:` 을 통해 전달인자를 받을 수 있음
- `.`으로 표시되는 특수 접미사 - directive를 특별한 방법으로 바인딩

### v-text

- `Template Interpolation`과 함께 가장 기본적인 바인딩 방법
- `{{ }}` 와 동일한 역할

```html
<div id="app">
  <p>메시지: {{ msg }}</p>   
  <p>HTML 메시지 : {{ rawHTML }}</p>
  <p>HTML 메시지 : <span v-html="rawHTML"></span></p>
  <p>{{ msg.split('').reverse().join('') }}</p>
</div>
<script>
const app = new Vue({
  el: '#app',
  data: {
    msg: 'Text interpolation',
    rawHTML: '<span style="color:red"> 빨간 글씨</span>'
  }
})
</script>
```

### v-html

- `RAW HTML`을 표현할 수 있는 방법
- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 **절대 사용 금지**

```html
<div id="app2">
  <p v-html="html"></p>
</div>
<script>
const app2 = new Vue({
  el: '#app2',
  data: {
    message: 'Hello!',
    html: '<a href="https://www.google.com">GOOGLE</a>'
  }
})
</script>
```

### v-show

- 표현식에 작성된 값에 따라 `element`를 보여 줄 것인지 결정
    - `boolean` 값이 변경 될 때 마다 반응
- 대상 `element`의 `display` 속성을 기본 속성과 none으로 `toggle`
- 요소자체는 항상 `DOM`에 렌더링 됨

```html
<div id="app3">
  <p v-show="isActive">보이니? 안보이니?</p>
</div>
<script>
const app3 = new Vue({
  el: '#app3',
  data: {
    isActive: false
  }
})
</script>
```

### v-if

- `v-show`와 사용 방법은 동일
- `isActive`의 값이 변경 될 때 반응
- 단, 값이 false인 경우 `DOM`에서 사라짐
- `v-if`, `v-else-if`, `v-else` 형태로 사용

```html
<div id="app3">
  <p v-if="isActive">안보이니? 보이니?</p>
</div>
<script>
const app3 = new Vue({
  el: '#app3',
  data: {
    isActive: false
  }
})
</script>
```

### `v-show` VS `v-if`

- `v-show`(Expensive initial load, cheap toggle)
    - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 `v-if` 보다 높을 수 있음
    - `display` 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음
- `v-if`(Cheap initial load, expensive toggle)
    - 표현식 결과가 false인 경우 렌더링 조차 되지 않으므로 초기 렌더링 비용은 `v-show`보다 낮을 수 있음
    - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가

### v-for

- `for .. in ..` 형식으로 작성
- 반복한 데이터 타입에 모두 사용 가능
- `:key=""`
    - `v-for` 사용 시 반드시 `key`속성을 각 요소에 작성
    - 주로 `v-for directive` 작성 시 사용
    - `vue` 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용
        - key가 중복되어서는 안됨
    - 각 요소가 고유한 값을 가지고 있다면 생략 가능

```html
<div id="app">
  <div v-for="(char, index) in myStr" :key="index">
    <p>{{ index }}번째 문자열 {{ char }}</p>
  </div>

  <h2>Array</h2>
  <div v-for="(item, index) in myArr" :key="`ssafy-${index}`">
    <p>{{ index }}번째 아이템 {{ item }}</p>
  </div>

  <div v-for="(item, index) in myArr2" :key="`arry-${index}`">
    <p>{{ index }}번째 아이템</p>
	  <p>{{ item.name }}</p>
  </div>

  <h2>Object</h2>
  <div v-for="value in myObj">
    <p>{{ value }}</p>
  </div>

  <div v-for="(value, key) in myObj" :key="key">
    <p>{{ key }} : {{ value }}</p>
  </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      // 1. String
      myStr: 'Hello, World!',

      // 2-1. Array
      myArr: ['python', 'django', 'vue.js'],

      // 2-2. Array with Object
      myArr2: [
        { id: 1, name: 'python', completed: true},
        { id: 2, name: 'django', completed: true},
        { id: 3, name: 'vue.js', completed: false},
		  ],
      
      // 3. Object
      myObj: {
        name: 'harry',
        age: 27
      },
    }
  })
</script>
```

### v-on

- `method`를 통한 `data` 조작도 가능
- `method`에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
- `:`을 통해 전달된 인자에 따라 특별한 modifiers(수식어)가 있을 수 있음
    - ex) `v-on:keyup.enter` 등
    - `vue2` 가이드 → `api` → `v-on` 파트 참고
- `@` shortcut 제공
    - ex) `@keyup.click`

```html
<div id="app">
  <button v-on:click="number++">increase Number</button>
  <p>{{ number }}</p>

  <button v-on:click="toggleActive">toggle isActive</button>
  <p>{{ isActive }}</p>

  <button @click="checkActive(isActive)">check isActive</button>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      number: 0,
      isActive: false,
    },
    methods: {
      toggleActive: function () {
        this.isActive = !this.isActive
      },

      checkActive: function (check) {
        console.log(check)
      }
    }
  })
</script>
```

### v-bind

- HTML 기본 속성에 `Vue data`를 연결
- class의 경우 다양한 형태로 연결 가능
    - 조건부 바인딩
        - { ‘class Name’:’조건 표현식’}
        - 삼항 연산자도 가능
    - 다중 바인딩
        - [’JS표현식’, ‘JS표현식’, …]
- `Vue data`의 변환에 대응하여 `DOM`에 반영하므로 상황에 따라 유동적 할당 가능
- `:` shortcut 제공
    - ex) `:class` 등
    - `v-for` 에서사용하였던 `:key`에서의 `:`는 `v-bind` shortcut을 활용한 것

```html
<div id="app2">
  <a v-bind:href="url">Go To GOOGLE</a>

  <p v-bind:class="redTextClass">빨간 글씨</p>
  <p v-bind:class="{ 'red-text': true }">빨간 글씨</p>
  <p v-bind:class="[redTextClass, borderBlack]">빨간 글씨, 검은 테두리</p>

  <p :class="theme">상황에 따른 활성화</p>
  <button @click="darkModeToggle">dark Mode {{ isActive }}</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
const app2 = new Vue({
  el: '#app2',
  data: {
    url: 'https://www.google.com/',
    redTextClass: 'red-text',
    borderBlack: 'border-black',
    isActive: true,
    theme: 'dark-mode'
  },
  methods: {
    darkModeToggle() {
      this.isActive = !this.isActive
      if (this.isActive) {
        this.theme = 'dark-mode'
      } else {
        this.theme = 'white-mode'
      }
    }
  }
})
</script>
```

### v-model

- `Vue instance`와 `DOM`의 양방향 바인딩
- `Vue data` 변경 시 `v-model`로 연결된 사용자 입력 `element`에도 적용

```html
<div id="app">
  <h2>1. Input -> Data</h2>
  <h3>{{ myMessage }}</h3>
  <input @input="onInputChange" type="text">
  <hr>

  <h2>2. Input <-> Data</h2>
  <h3>{{ myMessage2 }}</h3>
  <input v-model="myMessage2" type="text">
  <hr>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      myMessage: '',
      myMessage2: '',
    },
    methods: {
      onInputChange: function (event) {
        this.myMessage = event.target.value
      },
    }
  })
</script>
```

## Vue advanced

### computed

- `Vue instance`가 가진 `options`중 하나
- `computed` 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
    - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환

```html
<div id="app">
  <h1>data_01 : {{ number1 }}</h1>
  <h1>data_02 : {{ number2 }}</h1>
  <hr>
  <h1>add_method : {{ add_method() }}</h1>
  <h1>add_method : {{ add_method() }}</h1>
  <h1>add_method : {{ add_method() }}</h1>
  <hr>
  <h1>add_computed : {{ add_computed }}</h1>
  <h1>add_computed : {{ add_computed }}</h1>
  <h1>add_computed : {{ add_computed }}</h1>
  <hr>
  <button v-on:click="dataChange">Change Data</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      number1: 100,
      number2: 100
    },
    computed: {
      add_computed: function () {
        console.log('computed 실행됨!')
        return this.number1 + this.number2
      }
    },
    methods: {
      add_method: function () {
        console.log('method 실행됨!')
        return this.number1 + this.number2
      },
      dataChange: function () {
        this.number1 = 200
        this.number2 = 300
      }
    }
  })
</script>
```

> console을 통해 확인을 해보면 method는 호출될 때마다 실행이 되고 computed는 처음으로 호출했을 때만 연산작업을 실행한다.
> 

### methods VS computed

- methods
    - 호출 될 때마다 함수를 실행
    - 같은 결과여도 매번 새롭게 계산

- computed
    - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
    - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환
    

### watch

- 통상적으로 디버깅 시에 사용
- 특정 데이터의 변화를 감지하는 기능
    1. `watch` 객체를 정의
    2. 감시할 대상 `data`를 지정
    3. `data`가 변할 시 실행 할 함수를 정의
- 첫 번째 인자는 변동 전 `data`
- 두 번째 인자는 변동 후 `data`
- `parameter`와 `argument`의 이름이 같아야 함
- 실행 함수를 `Vue method`로 대체 가능
    1. 감시 대상 `data`의 이름으로 객체 생성
    2. 실행하고자 하는 `method`를 `handler`에 문자열 형태로 할당
- `Array, Object`의 내부 요소 변경 감지를 위해서는 `deep`속성 추가 필요

```html
<button @click="number++"></button>

<script>
const app = new Vue({
  data: {
    number : 0,
  }, 
  watch: {
    number function(val, oldVal) {
      console.log(val, oldVal)
      },
    }
  })
</script>
```

### filters

- 텍스트 형식화를 적용할 수 있는 필터
- `interpolation` 혹은 `v-bind`를 이용할 때 사용 가능
- 필터는 자바스크립트 표현식 마지막에 `|(파이프)`와 함께 추가되어야 함
- 이어서(chaining) 사용 가능

```html
<div id="app">
  <p>{{ numbers | getOddNums | getUnderTenNums }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    },
    filters: {
      getOddNums: function (nums) {
        const oddNums = nums.filter((num) => {
          return num % 2
        })
        return oddNums
      },
      
      getUnderTenNums: function (nums) {
        const underTen = nums.filter((num) => {
          return num < 10
        })
        return underTen
      }
    }
  })
</script>
```
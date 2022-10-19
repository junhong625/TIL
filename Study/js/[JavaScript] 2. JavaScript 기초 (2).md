# JavaScript 기초 (2)

## 함수

> 참조 타입 중 하나로써 function 타입에 속함
> 

### 함수 선언식(Function declaration)

- 일반적인 프로그래밍 언어의 함수 정의 방식

```jsx
function 함수명() {
  // do someting
}
```

- 예시

```jsx
function add(num1, num2) {
  return num1 + num2
}

console.log(add(2, 7)) // 9
```

### 함수 표현식(Function expression)

> 표현식 내에서 함수를 정의하는 방식
> 
- 함수 표현식은 함수의 이름을 생략한 **익명 함수**로 정의 가능
    - 표현식에서 함수 이름을 명시하는 것도 가능
    - 다만 이 경우 함수 이름은 호출에 사용 되지 못하고 디버깅 용도로 사용

```jsx
변수키워드 함수명 = function () {
  // do something
}
```

- 예시

```jsx
const sub = function (num1, num2) {
  return num1 - num2
}

console.log(sub(7, 2)) // 5
```

### 기본 인자(Default arguments)

- 인자 작성 시 ‘=’ 문자 뒤 기본 인자 선언 가능

```jsx
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting() // Hi Anonymous
```

### 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```jsx
const noArgs = function () {
  return 0
}

noArgs(1, 2, 3) // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

twoArgs(1, 2, 3) // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우

```jsx
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3]
}

threeArgs()     // [undifined, undifined, undifined]
threeArgs(1)    // [1, undifined, undifined]
threeArgs(1, 2) // [1, 2, undifined]
```

### Spread syntax(…)

> 전개 구문
> 
- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음
1. 배열과의 사용
    
    ```jsx
    let parts = ['shoulders', 'knees']
    let lyrics = ['head', ...parts, 'and', 'toes']
    
    console.log(lyrics) // ['head', 'shoulders', 'knees', 'and', 'toes']
    ```
    
2. 함수와의 사용(Rest parameters)
    - The rest parameter syntax 를 사용하여 정해지지 않은 수의 매개변수를 배열로 받을 수 있음
    
    ```jsx
    function func(a, b, ...theArgs) {
      // do something
    }
    ```
    
    ```jsx
    const restOpr = function (arg1, arg2, ...restArgs) {
      return [arg1, arg2, restArgs]
    }
    
    console.log(restOpr(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
    console.log(restOpr(1, 2)) // [1, 2, []]
    ```
    

## 선언식과 표현식

### 함수의 타입

> 선언식 함수와 표현식 함수 모두 타입은 function으로 동일
> 

### 호이스팅 - 선언식

> 함수 선언식으로 정의한 함수는 var로 정의한 변수처럼 호이스팅이 발생
> 
- 즉, 함수 호출 이후에 선언해도 동작

### 호이스팅 - 표현식

> 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
> 
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름
- **따라서, Airbnb Style Guide에서는 표현식 사용을 권장**

# Arrow Function

> 함수를 비교적 간결하게 정의할 수 있는 문법
> 
- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생
    1. function 키워드 생략 가능
    2. 함수의 매개변수가 하나 뿐이라면 ‘()’ 도 생략 가능
    3. 함수의 내용이 한 줄이라면 ‘{}’와 ‘return’도 생략 가능
- 화살표 함수는 항상 익명 함수 == 함수 표현식에서만 사용 가능

```jsx
const arrow1 = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 삭제
const arrow1 = (name) => { return `hello, ${name}` }

// 2. 인자가 1개일 경우 ( ) 생략 가능
const arrow1 = name => { return `hello, ${name}` }

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우 return, { } 생략 가능
const arrow1 = name => `hello, ${name}`
```

> 명확성과 일관성을 위해 항상 인자 주위에는 괄호 ( ) 를 포함하는 것을 권장
> 

### 화살표 함수 응용

```jsx
// 1. 인자가 없다면? () or _ 로 표시
let noArgs = () => 'No args'
noArgs = _ => 'No args'

// 2-1. object 를 return 한다면
let returnObject = () => { return { key: 'value'} } // return 을 명시적으로 적어준다.

// 2-2. return 을 적지 않으려면 괄호를 붙여야 한다.
returnObject = () => ({key: 'value'})
```

### 즉시 실행 함수(IIFE, Immediately Invoked Function Expression)

- 선언과 동시에 실행되는 함수
- 함수의 선언 끝에 ‘( )’를 추가하여 선언되자 마자 실행하는 형태
- ‘( )’ 에 값을 넣어 인자로 넘겨줄 수 있음
- 즉시 실행 함수는 선언과 동시에 실행되기 때문에 같은 함수를 다시 호출할 수 없음
- 이러한 특징을 살려 초기화 부분에 많이 사용
- 일회성 함수이므로 익명 함수로 사용하는 것이 일반적

```jsx
(function(num) { return num ** 3 }(2) // 8
(num => num ** 3)(2) // 8
```

# Array와 Object

> JavaScript의 데이터 타입 중 참조 타입(reference)에 해당 하는 타입은 Array와 Object이며, 객체라고도 말함
> 
- 객체는 속성들의 모음(collection)
    - 객체 안쪽의 속성들은 메모리에 할당 되어 있고 해당 객체는 메모리의 시작 주소 값을 가리키고 있는 형태로 이루어져 있음

# 배열(Array)

> 키와 속성들을 담고 있는 참조 타입의 객체
> 
- 순서를 보장하는 특징이 있음
- 주로 대괄호 `[ ]`를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 array.length 형태로 접근 가능
    - 배열의 마지막 원소는 array.length - 1로 접근

## 배열 메서드 기초

| 메서드 | 설명 | 비고 |
| --- | --- | --- |
| reverse | 원본 배열의 요소들의 순서를 반대로 정렬 |  |
| push & pop | 배열의 가장 뒤에 요소를 추가 또는 제거 |  |
| unshift & shift | 배열의 가장 앞에 요소를 추가 또는 제거 |  |
| includes | 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환 |  |
| indexOf | 배열에 특정 값이 존재하는지 판별 후 인덱스 반환 | 요소가 없을 경우 -1 반환 |
| join | 배열의 모든 요소를 구분자를 이용하여 연결 | 구분자 생략 시 쉼표가 기본값 |

## 배열 메서드 심화

- 배열을 **순회**하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 `callback 함수`를 받는 것이 특징
    - `callback 함수`: 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨 받는 함수
    - ex) django의 urls.py에서 path함수의 인자로 들어가는 `views.index`가 바로 `callback 함수`
    
    ```jsx
    urlpatterns = [
        path('index/', views.index, name='index')
    ]
    ```
    

| 메서드 | 설명 | 비고 |
| --- | --- | --- |
| forEach | 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행 | 반환 값 없음 |
| map | 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환 |  |
| filter | 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환 |  |
| reduce | 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환 |  |
| find | 콜백 함수의 반환 값이 참이면 해당 요소를 반환 |  |
| some | 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환 |  |
| every | 배열의 모든 요소가 판별 함수를 통과하면 참을 반환 |  |

### forEach

> array.forEach(callback(element[, index[,array]]))
> 
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
    - 콜백 함수는 3가지 매개변수로 구성
        1. element: 배열의 요소
        2. index: 배열 요소의 인덱스
        3. array: 배열 자체
- 반환 값(return) 없음

```jsx
const colors = ['red', 'blue', 'green']

// 1. 
const printClr = function (color) {
  console.log(color)
}
color.forEach(printClr)

// 2.
color.forEach(function (color) {
  console.log(color)
})

// 3.
color.forEach((color) => { console.log(color) })

// red
// blue
// green
```

### map

> array.map(callback(element[, index[, array]]))
> 
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용
- `forEach + return` 이라고 생각하기

```jsx
const numbers = [1, 2, 3, 4, 5]

// 1.
const doubleEle = function (number) {
  return number * 2
}

const newArry = numbers.map(doubleEle)

console.log(newArry)

// 2.
const newArry = numbers.map(function (number) {
  return number * 2
})

// 3.
const newArry = numbers.map((number) => {
  return number * 2
})

// 4.
const newArry = numbers.map((number) => number * 2
)
```

### filter

> array.filter(callback(element[, index[, array]]))
> 
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환
    - map + true인 값들
- 기존 배열의 요소들을 필터링 할 때 유용

```jsx
const products = [
  { name: 'cucumber', type: 'vegetable' }, 
  { name: 'banana', type: 'fruit' }, 
  { name: 'carrot', type: 'vegetable' }, 
  { name: 'apple', type: 'fruit' }, 
]

// 1.
const fruitFilter = function (product) {
  return products.type === 'fruit'
}

const newArray = products.filter(fruitFilter)
console.log(newArray)

// 2.
const newArray = products.filter(function (product) {
  return products.type === 'fruit'
}

// 3.
const newArray = products.filter((product) => {
  return products.type === 'fruit'
}
// 4.
const newArray = products.filter((product) => products.type === 'fruit')
```

### reduce

> array.reduce(callback(acc, element, [index[, array]])[, initialValue])
> 
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과 값을 반환
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용(총합, 평균 등)
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음
- reduct 메서드의 주요 매개변수
    - acc
        - 이전 callback 함수의 반환 값이 누적되는 변수
    - initialValue(optional)
        - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
- reduce의 첫번째 매개변수인 콜백 함수의 첫번째 매개변수(acc)는 누적된 값(전 단계까지의 값)
- reduce의 두번째 매개변수인 initialValue는 누적될 값의 초기값, 지정하지 않을 시 첫번째
- 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

```jsx
let numbers = [90, 80, 70, 100]

// 1.
let sumNum = numbers.reduce(function (total, number) {
  return total + number
}, 0)
console.log(sumNum)

// 2.
let sumNum = numbers.reduce((total, number) => {
  return total + number
}, 0)

// 3.
let sumNum = numbers.reduce((total, number) => total + number, 0)

// 4. 평균값 구하기
let avgNum = numbers.reduce((total, number) => total + number, 0) / numbers.length
```

### find

> array.find(callback(element[, indexp, array]]))
> 
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

```jsx
let avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rodgers', age: 32 },
    { name: 'Thor', age: 40 },
]

let ironman = avengers.find((avenger) => avenger.name === 'Tony Stark')
console.log(ironman)
```

### some

> array.some(callback(element[, index[, array]]))
> 
- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환

```jsx
let arr = [1, 2, 3, 4, 5]
let result = arr.some((elem) => elem % 2 === 0) //true

// 되돌리기 1.
let result = arr.some((elem) => {
  return elem % 2 === 0
})

// 되돌리기 2.
let result = arr.some(function (elem) {
  return elem % 2 === 0
})
```

### every

> array.every(callback(element[, index[, array]]))
> 
- 배열의 모든 요소가 주어진 판별 함수를 통과하면 참을 반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- 빈 배열은 항상 true 반환

```jsx
let arr = [1, 2, 3, 4, 5]
let result = arr.every((elem) => elem % 2 === 0) //false

// 되돌리기 1.
let result = arr.every((elem) => {
  return elem % 2 === 0
})

// 되돌리기 2.
let result = arr.every(function (elem) {
  return elem % 2 === 0
})
```

### 배열 순회 비교

| 방식 | 특징 | 비고 |
| --- | --- | --- |
| for loop | - 모든 브라우저 환경에서 지원
- 인덱스를 활용하여 배열의 요소에 접근
- break, continue 사용 가능 |  |
| for…of | - 일부 오래된 브라우저 환경에서 지원
- 인덱스 없이 배열의 요소에 바로 접근 가능
- break, continue 사용 가능 |  |
| forEach | - 대부분의 브라우저 환경에서 지원
- break, continue 사용 불가능 | Airbnb Style Guide 권장 방식 |

# 객체(Object)

> 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현
> 
- 쉽게 생각하면 python의 dictionary
- key는 문자열 타입만 가능
    - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수 포함) 가능
- 객체 요소 접근은 점 `.` 또는 대괄호 `[ ]`로 가능
    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```jsx
let myInfo = {
  name: 'AJH',
  phoneNumber: '01099723173',
  'apple products': {
    airpod: 'airpod pro',
    iphone: 'iphoneX',
  },
}

console.log(myInfo.name) // AJH
console.log(myInfo["phoneNumber"] // 01099723173
console.log(myInfo["apple products"]) // airpod: 'airpod pro', iphone: 'iphoneX'
console.log(myInfo["apple products"].iphone) // iphoneX
```

## 객체 관련 문법

### 1. 속성명 축약

> 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능
> 

```jsx
let books = ['Learning JavaScript', 'Learning Python']
let magazines = ['Vogue', 'Science']

const bookShop = {
    books,
    magazines,
}

console.log(bookShop)
/*
{
  books: ['Learning JavaScript', 'Learning Python'],
  magazines: ['Vogue', 'Science']
}
*/
```

### 2. 메서드명 축약

> 메서드 선언 시 function 키워드 생략 가능
> 

```jsx
let obj = {
    name: 'AJH',
    greeting() {
        console.log('Hi!')
    }
}

console.log(obj.name) // AJH
obj.greeting() // Hi!
```

### 3. 계산된 속성(computed property name)

> 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능
> 

```jsx
let key = 'country'
let value = ['한국', '미국', '일본', '중국']

let myObj = {
    [key]: value,
}

console.log(myObj)
console.log(myObj.country)
```

### 4. 구조 분해 할당(destructing assignment)

> 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
> 

```jsx
let userInformation = {
    name:  'ssafy kim',
    userId: 'ssafyStudent1234',
    phoneNumber: '010-1234-1234',
    email: 'ssafy@ssafy.com'
}

// let { name } = userInformation
// let { userId } = userInformation
// let { phoneNumber } = userInformation
// let { email } = userInformation

let { name, phoneNumber } = userInformation

console.log(name)
// console.log(userId)
console.log(phoneNumber)
// console.log(email)
```

### 5. Spread syntax(…)

> 배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
> 
- 얕은 복사에 활용 가능

```jsx
let obj = {b: 2, c: 3, d: 4}
let newObj = {a: 1, ...obj, e: 5}

console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

### JSON

> JavaScript Object Notation
> 
- Key-Value 형태로 이루어진 자료 표기법
- JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, JSON은 형식이 있는 “문자열”
- 즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요
- JSON 변환

```jsx
let jsonData = {
    coffee: 'Americano',
    iceCream: 'Mint Choco',
}

// Object -> JSON
let objToJson = JSON.stringify(jsonData)
console.log(objToJson) // {"coffee":"Americano","iceCream":"Mint Choco"}
console.log(typeof objToJson) // String

// JSON -> Object
let jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj) // { coffee: 'Americano', iceCream: 'Mint Choco' }
console.log(typeof jsonToObj) // Object
```

### 배열은 객체다

> 배열은 키와 속성들을 담고 있는 참조 타입의 객체
> 
- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체

```jsx
console.log(Object.getOwnPropertyDescriptors([1, 2, 3]))

// {
//     '0': { value: 1, writable: true, enumerable: true, configurable: true },
//     '1': { value: 2, writable: true, enumerable: true, configurable: true },
//     '2': { value: 3, writable: true, enumerable: true, configurable: true },
//     length: { value: 3, writable: true, enumerable: false, configurable: false }
// }
``` 
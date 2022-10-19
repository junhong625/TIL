# JavaScript 기초 (1)

## JavaScript를 배워야 하는 이유

### 1. Web 기술의 기반이 되는 언어

> HTML 문서의 콘텐츠를 **동적으로 변경**할 수 있는 언어
> 
- Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반

### 2. 다양한 분야로 확장이 가능한 언어

> 서버 프로그래밍, 모바일 서비스, 컴퓨터 응용 프로그래밍, 블록체인, 게임 개발 등 다양한 분야에서 활용이 가능한 언어
> 

### 3. 꾸준히 가장 인기있는 언어

> Stackoverflow, Github 등에서 꾸준히 1위를 유지하고 있는 언어
> 

## JavaScript의 역사

### 웹 브라우저와 스크립트 언어

### 1993, Mosaic Web Browser

- Netscape에서 유저가 웹을 쉽게 탐색할 수 있게 버튼 등을 탑재한 GUI 기반의 웹 브라우저 출시

### 1994, Netscape Navigator

- Mosaic Web Browser를 개선한 후속작, 시장 점유율 80% 차지
- 당시 브라우저들은 정적 웹페이지를 단순히 보여주는 용도에 그침
- 따라서 웹 페이지를 동적으로 바꿔줄 Script 언어의 필요성을 느낌
    - Script언어
        - 소스 코드를 기계어로 바꿔주는 컴파일러 없이 바로 실행 가능한 언어
        - 속도가 느리다는 단점이 존재
- Netscape에서 약 10일의 개발 기간을 통해 Script언어인 `Mocha` 개발
- 이후 `LiveScript`로 이름 변경 후 브라우저에 LiveScript를 해석해주는 Engine을 내장
- 하지만 사용자들의 관심이 저조하자 당시 인기 있던 JAVA의 명성에 기대보고자 JavaScript로 이름 변경

### 1995, Microsoft의 Internet Explorer

- Microsoft에서 Netscape의 인기를 보고 Web Browser시장에 뛰어들기 시작
- JavaScript를 그대로 복사한 JScript라는 언어 제작 후 이를 탑재한 Web Browser인 Internet Explorer 출시
- 이후 JavaScript와 JScript는 각자의 기능을 추가하기 시작
- 개발자들은 Netscape Navigator와 Internet Explorer 각각에 대한 코드를 작성 해야 하는 상황을 맞이하게 됨

### 1996-2000, ECMA 표준 발의

- Netscape가 정보 통신에 관한 규약을 만드는 비영리 단체 ECMA에게 JavaScript 기반의 표준안 발의 제안, `ECMAScript 1` 출시
- 이후 여러가지 문법이 추가되며 ECMAScript의 버전이 올라감
- 이 상황을 지켜보던 Microsoft에서 Windows에 Internet Explorer를 기본 탑재하여 출시
- 결국 Microsoft가 시장 점유율 95% 이상으로 증가, ECMAScript 표준안 지키지 않기로 선언

### 2001-2004, 다양한 웹 브라우저의 등장

- `ActionScript3`라는 스크립트 언어를 기반으로 한 Firefox 웹 브라우저 출시
- 개발자들은 Netscape Navigator & Internet Explorer & Firefox 지원을 위해 많은 고통을 받음
- 이후 Opera 등의 다양한 웹 브라우저가 계속 시장에 출시
- 다양성으로 인해 더더욱 많은 개발자가 필요해졌고, 이는 집단 지성을 형성

### jQuery 등의 라이브러리 등장

- 각 브라우저의 엔진에 맞는 스크립트를 여러 번 작성하는 것이 고통스러움
- 중간에 하나의 레이어를 두고 코딩하는 것 = jQuery
    - jQuery 문법에 맞춰 작성하면 브라우저별 엔진에 맞는 스크립트 변환은 jQuery가 알아서 변환해줌
- 이후 많은 코드가 jQuery로 작성됨

### 2008, Google의 Chrome 등장과 대통합의 시대

- V8이라는 강력한 엔진을 탑재한 Chrome 등장
    - JavaScript 해석이 다른 웹 브라우저에 비해 월등히 빠름
    - 이로 인해 웹 브라우저가 버벅임이 없고 매우 빠르게 동작
- Chrom의 성능이 너무 압도적이자 다른 웹 브라우저들이 함께 표준안을 만들자고 제안

### 2009, ECMAScript5(ES5) 표준안 제정

### 2015, ECMAScript6(ES6) 표준안 제정

- 이후에도 계속해서 버전이 업데이트 되고 있으나, ES6에서 큰 변화는 없음

## 요약

- 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음
- 현재의 JavaScript는 이제 시장에서 자리를 잡은 언어이며, 개발에서 큰 축을 담당하는 언어
- 더 이상 jQuery 등의 라이브러리를 사용할 필요가 없음(모든 웹 브라우저가 표준안을 따름)
- 특히, Chrome의 V8의 경우 JavaScript를 번역하는 속도가 매우 빠름
    - Web Browser 뿐만이 아니라 다른 개발에서도 활용해보자는 의견이 나옴
    - nods.js, react.js, electron 등의 내부 엔진으로 사용
    - 그 결과, back-end, mobile, desktop app 등을 모두 JavaScript로 개발이 가능해짐

# JavaScript 실행

## 1. Web Browser로 실행하기

> Web Browser에는 JavaScript를 해석할 수 있는 엔진이 있어 실행할 수 있음
> 
- 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 `Vanilla JavaScript`라고 부름

### 1-1. HTML 파일에 직접 javaScript를 작성 후 웹 브라우저로 파일 열기

- 화면이 아닌 개발자 관리 도구(F12)에서 console탭에서 결과 확인 가능

```html
<!-- hello.html -->

...
<body>
    <script>
        console.log('hello, javascript')
    </script>
</body>
...
```

### 1-2. `.js` 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 포함 가능

```jsx
// hello.js

console.log('hello, javascript')
```

```html
<!-- hello.html -->

...
</body>
<script src="hello.js"></script>
</html>
```

### 1-3. 웹 브라우저의 console에서 바로 JavaScript를 입력

```jsx
let hello = 'hello'
console.log(hello)
```

## 2. Node.js로 실행하기

> 웹 브라우저를 이용하지 않고 JavaScript를 실행할 수 있음
> 
- node.js 설치 후
- JavaScript 파일 실행해 보기

```bash
node hello.js
```

# JavaScript 기초 문법

### 세미콜론(semicolon)

> 자바스크립트는 세미콜론을 **선택적**으로 사용 가능
> 
- 세미콜론이 없으면 `ASI`에 의해 자동으로 세미콜론이 삽입됨
    - `ASI` (Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙

### 들여쓰기와 코드 블럭

- python은 4칸 들여쓰기를 사용했으나, JavaScript는 2칸 들여쓰기를 사용
- 블럭(block)은 if, for, 함수에서 중괄호 `{}` 내부를 말함
    - python은 들여쓰기를 이용해서 코드 블럭을 구분
    - JavaScript는 중괄호 `{}`를 사용해 코드 블럭을 구분

### 코딩 스타일 가이드

> 코드 스타일의 핵심은 합의된 원칙과 일관성
> 
- 코드의 품질에 직결되는 중요한 요소
    - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침
- Python에도 PEP8이라는 코드 스타일 가이드가 있었듯, JavaScript에도 코드 스타일 가이드 존재
- 다만 JavaScript는 여러 코드 스타일 가이드가 회사마다 존재하는데, 본 내용에서는 Airbnb Style Guide를 기반으로 사용

### 주석

> 한 줄 주석(`//`) 여러 줄 주석(`/* */`) 사용
> 

# 변수와 식별자

## 식별자 정의와 특징

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
    - 예약어 예시: for, if, function

### **카멜 케이스(camelCase, lower-camel-case)**

- 변수, 객체, 함수에 사용

### **파스칼 케이스(PascalCase, upper-camel-case)**

- 클래스, 생성자에 사용

### **대문자 스네이크 케이스(SNAKE_CASE)**

- 상수(constants)에 사용
- 상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

## 변수 선언 키워드

> Python과 다르게 JavaScript는 변수를 선언하는 키워드가 정해져 있음
> 

### 1. let

- 블록 스코프 지역 변수를 선언(추가로 동시에 값을 초기화)
- 재할당 가능 & 재선언 불가능

```jsx
let number = 10  // 선언 및 초기값 할당
number = 20      // 재할당
let number = 20  // 재선언 불가
```

- 블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음

### 2. const

- 블록 스코프 읽기 전용 상수를 선언(추가로 동시에 값을 초기화)
- 재할당 & 재선언 모두 불가능

```jsx
const number = 10 // 선언 및 초기값 할당
number = 20       // 재할당 불가능
const number = 20 // 재선언 불가능
```

- 선언 시 반드시 초기값을 설정 해야 하며, 이후 값 변경이 불가능
- let과 동일하게 블록 스코프를 가짐

### 3. var

- 변수를 선언(추가로 동시에 값을 초기화)
- 재할당 가능 & 재선언 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- `호이스팅` 되는 특성으로 인해 예기치 못한 문제 발생 가능
    - `호이스팅` : 변수를 선언 이전에 참조할 수 있는 현상
    - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프(function scope)를 가짐
- 변수 선언시 변수 선언 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

## 선언, 할당, 초기화, 블록 스코프

### 선언(Declaration)

- 변수를 생성하는 행위 또는 시점

```jsx
let foo          // 선언
console.log(foo) // undefined
```

### 할당(Assignment)

- 선언된 변수에 값을 저장하는 행위 또는 시점

```jsx
foo = 11         // 할당
console.log(foo) // 11
```

### 초기화(Initialization)

- 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

### 블록 스코프(block scope)

- if, for, 함수 등의 중괄호(`{}`)내부를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

```jsx
let x = 1

if (x === 1) {
  let x = 2
  console.log(x) // 2
}

console.log(x)   // 1
```

# 데이터 타입

> JavaScript의 모든 값은 크게 `원시 타입(Primitive type)`과 `참조 타입(Reference type)`으로 분류됨
> 

## 원시 타입(Primitive type)

### Number

- 정수 또는 실수형 숫자를 표현하는 자료형

```jsx
const a = 13
const b = -5
const c = 3.14
const d = 2.998e8
const e = Infinity  // 양수 무한값
const f = -Infinity // 음수 무한값
const g = NaN       // Not a Number
```

- NaN(Not a Number)
    - `Number.isNaN()`
        - 주어진 값의 유형이 Number이고 값이 NaN이면 true, 아니면 false를 반환
    - 숫자로서 읽을 수 없는 경우 반환(parseInt(”문자”), Number(undefined))
    - 결과가 허수인 수학 계산식인 경우 반환(Math.sqrt(-1))
    - 피연산자가 NaN인 경우(7 ** NaN)
    - 정의할 수 없는 계산식인 경우(0 * Infinity)
    - 문자열을 포함하면서 덧셈이 아닌 계산식(”가” / 3)

### String

- 문자열을 표현하는 자료형
- 작은 따옴표 또는 큰 따옴표 모두 가능

```jsx
const sentence1 = "hello"
const sentence2 = 'hello'

console.log(sentence1) // "hello"
console.log(sentence2) // "hello"
```

- 곱셈, 나눗셈, 뺄셈은 안되지만 덧셈을 통해 문자열 붙일 수 있음

```jsx
const firstName = 'Tony'
const lastName = 'Stark'
const fullName = firstName + lastName

console.log(fullName) // "Tony Stark"
```

- Quote를 사용하면 선언 시 줄 바꿈이 안됨
- 대신 escape sequence를 사용할 수 있기 때문에 `\n`을 사용해야 함

```jsx
const word1 = "안녕 \n하세요"
console.log(word1) // "안녕
                   // 하세요"
```

- Template Literal(`)을 사용하면 줄 바꿈이 되며, 문자열 사이에 변수(`${expression}`도) 삽입 가능

```jsx
const word2 = `안녕
들 하세요`
console.log(word2) // "안녕
                   // 들 하세요"

const age = 10
const message = `홍길동은 ${age}세 입니다.`
console.log(message) // "홍길동은 10세 입니다."
```

### Empty Value

- 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 `null` 과 `undefined` 가 존재
- 동일한 역할을 하는 이 두 개의 키워드가 존재하는 이유는 단순한 설계 실수
- 큰 차이를 두지 말고 interchangeable 하게 사용할 수 있도록 권장함

### null

> null 값을 나타내는 특별한 키워드
> 
- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

### undefined

> 값이 정의되어 있지 않음을 표현하는 값
> 
- 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

### null과 undefined

- 둘의 대표적인 차이점은 `typeof` 연산자를 통해 타입을 확인 했을 때 나타남

```jsx
typeof null      // "object"
typeof undefined // "undefined"
```

- null이 원시 타입임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시 버그를 해결하지 못했기 때문
- null 타입에 의존성을 띄고 있는 많은 프로그램들로 인해 해결이 어려움

### Boolean

- true와 false
- 참과 거짓을 표현하는 값
- 조건문 또는 반복문에서 유용하게 사용
    - 조건문 또는 반복문에서 boolean이 아닌 데이터 타입은 **자동 형변환 규칙**에 따라 true 또는 false로 변환됨

### ToBoolean Conversions(자동 형변환)

| 데이터 타입 | false | true |
| --- | --- | --- |
| undefined | 항상 false | X |
| null | 항상 false | X |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | 빈 문자열 | 나머지 모든 경우 |
| Object | X | 항상 true |

# 연산자

### 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- 다양한 연산에 대한 단축 연산자 지원
- Increment 및 Decrement 연산자
    - Increment(++) : 피연산자의 값을 1 증가시키는 연산자
    - Decrement(—) : 피연산자의 값을 1 감소시키는 연산자
    - `+=` 또는 `-=` 와 같이 더 분명한 표현으로 적을 것을 권장

### 비교 연산자

- 피연산자들을 비교하고 결과값을 boolean으로 반환하는 연산자

### 동등 연산자(==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
- 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

```jsx
const a = 1
const b = '1'

console.log(a == b) //true
console.log(a == true) // true

//자동 형변환 예시
console.log(8 * null) // 0, null은 0
console.log('5' - 1)  // 4
console.log('5' + 1)  // '51'
console.log('five' * 2) // NaN
```

### 일치 연산자(===)

- 두 피연산자의 값과 타임이 모두 같은 경우 true를 반환
- 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
- 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
    - 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교하는 방식

### 논리 연산자

- 세 가지 논리 연산자로 구성
    - and 연산 : `&&` 연산자
    - or 연산 : `||`연산자
    - not 연산 : `!` 연산자
- 단축 평가 지원
    - false && true ⇒ false
    - true || false ⇒ true

### 삼항 연산자(Ternary Operator)

- 3개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 앞의 조건식이 참이면 :(콜론) 앞의 값이 반환되며, 거짓일 경우에는 뒤의 값이 반환되는 연산자
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

```jsx
true ? 1 : 2 // 1
false ? 1 : 2 // 2

const result = Math.PI > 4 ? 'Yep' : 'Nope'
console.log(result) // Nope
```

# 조건문

### if statement

- if, else if, else
    - 조건은 소괄호 `()` 안에 작성
    - 실행할 코드는 중괄호 `{}` 안에 작성
    - 블록 스코프 생성

```jsx
const name = 'manager'

if (name === 'admin') {
  console.log('관리자님 환영합니다.')
} else if (name === 'manager') {
  console.log('매니저님 환영합니다.')
} else {
  console.log(`${name}님 환영합니다.`)
}
```

### switch statement

- 표현식(expression)의 결과값을 이용한 조건문
- 표현식의 결과값과 case문의 오른쪽 값을 비교
- break 및 default문은 선택적으로 사용 가능
- break문이 없는 경우 break문을 만나거나 default문을 실행할 때까지 다음 조건문 실행
- 블록 스코프 생성
- 아래와 같은 예시에서 만약 break문이 없을 경우 같은 조건에 해당하는 case부터 시작하여 순차적으로 default를 만나기 전까지 모든 case들을 출력

```jsx
const name = '홍길동'
switch(name) {
  case '홍길동': {
    console.log('관리자님 환영합니다.')
    break
  }
  case 'manager': {
    console.log('매니저님 환영합니다.')
    break
  }
  default: {
    console.log(`${name}님 환영합니다.`)
  }
}
```

# 반복문

### while

> while (조건문) {}
> 
- 조건문이 참이기만 하면 문장을 계속해서 수행

```jsx
let i = 0
while (i < 6) {
  console.log(i)
  i += 1
}

// 0, 1, 2, 3, 4, 5
```

### for

> for ([초기문]; [조건문]; [증감문]) {}
> 
- 특정한 조건이 거짓으로 판별될 때까지 반복

```jsx
for (let i = 0; i < 6; i++) {
  console.log(i)
}

// 0, 1, 2, 3, 4, 5
```

### for…in

> for (variable in object) {}
> 
- 객체(object)의 속성을 순회할 때 사용
- key값들을 출력
- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

```jsx
const fruits = {a: 'apple', b:'banana'}

for (const key in fruits) {
  console.log(key) // a, b
  console.log(fruits[key]) // apple, banana
}
```

### for…of

> for (variable of object) {}
> 
- 반복 가능한 객체를 순회할 때 사용(Array, Set, String 등)

```jsx
const numbers = [0, 1, 2, 3]

for (const number of numbers) {
  console.log(number) // 0, 1, 2, 3
}
```
# JavaScript 동기와 비동기

## 동기(Synchronous)

> 모든 일을 순서대로 하나씩 처리하는 것
> 
- 순서대로 처리한다 == 이전 작업이 끝나면 다음 작업을 시작한다.
- 우리가 작성했던 Python 코드가 모두 동기식

```jsx
print('첫번째 작업')
for i in range(10):
	print('두번째 작업')
	print(i)
print('세번째 작업')
```

- 요청과 응답을 동기식으로 처리한다면?
    - 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리
- 예시
    
    ```jsx
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
    </head>
    <body>
      <button>버튼</button> 
      <script>
        const btn = document.querySelector('button')
        btn.addEventListener('click', () => {
          alert('you clicked me!')
          const pElem = document.createElement('p')
          pElem.innerText = 'p Element'
          document.body.appendChild(pElem)
        })
      </script>
    </body>
    </html>
    ```
    
    - 해당 코드를 실행 시 `alert`에 의해 알림 창이 뜨고
    - 확인 버튼을 클릭해야 p Element라는 문자가 나타난다.
    - 이것이 바로 **동기식 처리**

## 비동기(Asynchronous)

> 작업을 시작한 후 결과를 기다리지 않고 다음 작업을 처리하는 것(병렬적 수행)
> 
- 시간이 필요한 작업들은 요청을 보낸 뒤 응답이 빨리 오는 작업부터 처리
- 예시) Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨
- 예시
    
    ```jsx
    function slowRequest(callBack) {
      console.log('1. 오래 걸리는 작업 시작 ...')
      setTimeout(function () {  
        callBack()
      }, 3000)
    }
    
    function myCallBack() {
      console.log('2. 콜백함수 실행됨')
    }
    
    slowRequest(myCallBack)
    console.log('3. 다른 작업 실행')
    ```
    
    - 동기식이라면 1 → 2→ 3 순으로 출력이 됐겠지만
    - 앞선 작업이 끝날때 까지 기다리지 않는 비동기식의 경우 1 → 3 → 2 순으로 출력이됨

### 비동기(Asynchronous)를 사용하는 이유

- 사용자 경험
    - 예를 들어 아주 큰 데이터를 불러온 뒤 실행되는 앱이 있을 때, 동기로 처리한다면 데이터를 모두 불러온 뒤에야 앱의 실행 로직이 수행되므로 사용자들은 마치 앱이 멈춘 것과 같은 경험을 겪게 됨
    - 즉, 동기식 처리는 특정 로직이 실행되는 동안 다른 로직 실행을 차단하기 때문에 마치 프로그램이 응답하지 않는 듯한 사용자 경험을 만들게 됨
    - 비동기로 처리한다면 먼저 처리되는 부분부터 보여줄 수 있으므로, 사용자 경험에 긍정적인 효과를 볼 수 있음
    - 이와 같은 이유로 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음

# JavaScript 비동기 처리

## Single Thread 언어, JavaScript

- 사용자 경험을 위해 비동기식을 추구한다면 응답이 오는 순서대로가 아닌 아예 여러 작업을 동시에 처리하면 되지 않을까?라는 생각을 할 수도 있음
- 하지만 JavaScript는 한 번에 하나의 일만 수행할 수 있는 Single Thread 언어로 동시에 여러 작업을 처리할 수 없음
- 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없다. 그렇다면 Single Thread로 어떻게 비동기 처리를 할 수 있을까?

## JavaScript Runtime

- JavaScript 자체는 Single Thread이므로 비동기 처리를 할 수 있도록 도와주는 환경이 필요함
- 특정 언어가 동작할 수 있는 환경을 “런타임(Runtime)”이라 함
- JavaScript에서 비동기와 관련한 작업은 브라우저 또는 Node환경에서 처리
- 이중에서 브라우저 환경에서의 비동기 동작은 크게 아래의 요소들로 구성됨
    1. JavaScript Engine의 `Call Stack`
    2. `Web API`
    3. `Tast Queue`
    4. `Event Loop`

## 비동기 처리 동작 방식

- 브라우저 환경에서의 JavaScript의 비동기는 아래와 같이 처리된다.
1. 모든 작업은 Call Stack(LIFO)으로 들어간 후 처리된다.
2. 오래 걸리는 작업이 Call Stack으로 들어오면 Web API로 보내 별도로 처리하도록 한다.
3. Web  API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 Task Queue(FIFO)에 순서대로 들어간다.
4. Event Loop가 Call Stack이 비어 있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된 (가장 앞에 있는) 작업을 Call Stack으로 보낸다.

### 실습 코드

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <script>
    console.log('Hi')

    setTimeout(function () {
      console.log('SSAFY')
    }, 3000)

    console.log('Bye')
  </script>
</body>
</html>
```

- 위 코드에서 setTimeout으로 3000ms의 지연 시간을 가진 뒤 출력을 한다면 `Hi` → `Bye` → `SSAFY`  순으로 출력된다.
- 그렇다면 0ms으로 지연시간을 변경한다면 어떤 결과를 가져올까?
    - 결국 setTimeout 즉, 지연시간을 설정해줌으로써 Call Stack이 아닌 Web API의 도움을 받아 Task Queue를 거쳐 Event Loop에 의해 Call Stack이 비어있을 때 들어오기 때문에 위와 똑같이 `Hi` → `Bye` → `SSAFY` 순으로 출력된다.

### JavaScript의 비동기 처리

- JavaScript는 한 번에 하나의 작업을 수행하는 Single Thread 언어로 동기적 처리를 하지만, 브라우저 환경에서는 Web API에서 처리된 작업이 지속적으로 Task Queue를 거쳐 Event Loop에 의해 Call Stack에 들어와 순차적으로 실행됨으로써 비동기 작업이 가능한 환경이 됨
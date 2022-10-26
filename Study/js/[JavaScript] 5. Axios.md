# JavaScript Axios

# Axios

> JavaScript의 비동기 HTTP 웹 통신을 위한 라이브러리
> 
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
- node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 있음

## Axios 기본 구조

### Axios 사용해보기

```jsx
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios.get('요청할 URL')
  .then(성공하면 수행할 콜백함수)
  .catch(실패하면 수행할 콜백함수)
</script>
```

- get, post 등 여러 method 사용 가능
- `then` ⇒ 성공하면 수행할 로직
- `catch` ⇒ 실패하면 수행할 로직
- then과 catch같이 바로 붙여쓸 수 있는 method들을 다음 라인에 작성한 이유 
⇒ 함수에 대한 가독성을 높이기 위해서

### 고양이 사진 가져오기

1. python으로 간단하게 가져오는 방법

```python
import requests 

print('고양이는 야옹')

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
    print(response.json())
else: 
    print('실패했다옹')
    
print('야옹야옹')
```

- 동기식 코드는 위에서부터 순서대로 처리가 되기 때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력된다.

1. Axios 사용하여 비동기식으로 가져오기

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <button>야옹아 이리온</button>
  <button id="dog-btn">멍멍아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    const btn = document.querySelector('button')

    const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
    const dogBtn = document.querySelector('#dog-btn')

    dogBtn.addEventListener('click', function (event) {
      axios({
        method: 'get',
        url: dogImageSearchURL
      })
        .then((response) => {
          console.log(response.data.message)
          const imgSrc = response.data.message
          return imgSrc
        })
        .then((imgSrc) => {
          const imgTag = document.createElement('img')
          imgTag.setAttribute('src', imgSrc)
          document.body.appendChild(imgTag)
        })
        .catch((error) => {
          console.log(error)
        })
        const pTag = document.createElement('p')
        pTag.innerText = '멍멍멍멍'
        document.body.appendChild(pTag)
    })

    // Promise 객체를 리턴하는 axios 라이브러리
    // console.log(axios.get(catImageSearchURL))

    btn.addEventListener('click', function () {
    //   // 권장 표기 방식
      axios({
        method: 'get',
        url: catImageSearchURL,
      })
        .then((response) => {
          // console.log(response.data[0].url)
          imgElem = document.createElement('img')
          imgElem.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgElem)
        })
        .catch((error) => { 
          console.log('실패했다옹')
        })
        const pElem = document.createElement('p')
        pElem.innerText = '야오야옹'
        document.body.appendChild(pElem)

      // 일반 표기 방식
      // axios.get(catImageSearchURL)
      //   .then((response) => {
      //     console.log(response.data[0].url)
      //     const imgElem = document.createElement('img')
      //     imgElem.setAttribute('src', response.data[0].url)
      //     document.body.appendChild(imgElem)
      //   })
      //   .catch((error) => { 
      //     console.log('실패했다옹')
      //   })
      //   console.log('야옹야옹') 
    })
  </script>
</body>
</html>
```

- 비동기식 코드는 바로 처리가 가능한 작업은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내 놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨
- 즉, 바로 처리가 가능한 console.log 는 바로 화면에 출력되지만, 시간이 걸리는 이미지는 처리가 완료된 후 화면에 나타나는 것을 볼 수 있다.
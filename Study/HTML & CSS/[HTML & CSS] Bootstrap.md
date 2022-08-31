# Bootstrap

- 사용 방법
    - [**bootstrap**](https://getbootstrap.com/) 홈페이지 이동
    - Docs → download 이동
    - 해당 페이지에서 ****CDN via jsDelivr****의 `link`, `script` 복사, 붙여넣기
        - `link` : head부분에 붙여넣기
        - `script` : body태그 닫는 코드 바로 위에 붙여넣기
            - 내부 코드를 모두 불러온 후에 script를 적용시키기 위해
            

## 기본 원리

### spacing

> {property}{sides}-{size}
> 
- property : **m**-`margin` or **p**-`padding`
- sides :
    - **t** - `top`
    - **b** - `bottom`
    - **s** - `left`
    - **e** - `right`
    - **x** - `*-left` and `*-right`
    - **y** - `*-top` and `*-bottom`
- size :
    - **0** - 0 `0px`
    - **1** - `0.25rem` `4px`
    - **2** - `0.5rem` `8px`
    - **3** - `1rem` `16px`
    - **4** - `1.5rem` `24px`
    - **5** - `3rem` `48px`
    

### Color

> {type}-{color}
> 
- type : bg - `background` or text - `text`
- color :
    - [Colors](https://getbootstrap.com/docs/5.2/utilities/colors/), [Background](https://getbootstrap.com/docs/5.2/utilities/background/)에서 확인 가능
    - **primary** : blue
    - **secondary** : gray
    - **danger** : red
    
     등
    

### Text

> text-{property}
> 
- property :
    - **start**
    - **center**
    - **end**

> 다양한 사용법 Bootstrap 참조
> 

### Carousel

- 슬라이드 쇼 구성 요소

### Mordal

- 사용 시 `body` 태그와 같은 탑 레벨로 배치!

### BreakPoints

- 반응형 레이아웃 작동 방식을 결정

### Grid system

- 요소들의 디자인과 배치에 도움을 주는 시스템
- BreakPoints를 이용하여 구간마다 레이아웃을 설정 가능
- 반드시 기억해야 할 2가지!
    1. 12개의 column
    2. 6개의 gird breakpoins
# HTML & CSS 🖥️

# CSS

> **Cascading Style Sheets**
> 
- 뼈대(HTML)의 스타일을 지정하기 위한 언어
- 예시

```css
h1 { /*선택자(Selector)*/
	color: blue; /*선언(Declaration)*/
	font-size: 15px; /*속성(Property): 값(value)*/
}
```

- CSS 구문은 **선택자**를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서는 **속성과 값**, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(Property) : 어떤 스타일 기능을 변경할지 결정
    - 값(Value) : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

- 인라인(inline)
    - 인라인을 쓰게 되면 실수가 잦아짐
    - 코드가 너무 길어짐
    - **재사용성 Down**
- 내부 참조(embedding) - <style>
    - 내부 참조를 쓰게 되면 코드가 너무 길어짐
- 외부 참조(link file) - HTML파일에 <link> 태그를 통해  CSS 파일 style
    - 가장 많이 사용
    - **재사용성 Up**

## CSS Selectors 유형

- 기본 선택자
    - 전체 선택자, 요소 선택자
    - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
    - 자손 결합자, 자식 결합자
    - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
    - 링크, 동적 의사 클래스
    - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
- 예시 :

```css
<style>
/*전체 선택자*/
* {
	color : red;
}

/*요소 선택자*/
h2 {
	color : orange;
}

/*요소 다중 선택자*/
h3, h4 {
	font-size: 10px;
}
/*클래스 선택자*/
.green {
	color: green;
}

/*id 선택자*/
#purple {
	color: purple;
}

/*자식 결합자*/
.box > p {
	font-size: 30px;
}

/*자손 결합*/
.box p {
	color: blue;
}
</style>
```

- 요소 선택자
    - HTML 태그를 직접 선택
- 클래스(class) 선택자
    - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
- 아이디(id) 선택자
    - `#` 문자로 시작하며, 해당 아이디가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용
    - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장
    

## CSS 적용 우선 순위(cascading order)

> 범위가 좁을수록 우선 순위가 높다!!
> 
- CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.
    1. 중요도(Importance) - 사용 시 주의
        - !Important
    2. 우선 순위 (Specificity)
        - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
    3. CSS 파일 로딩 순서
    

## CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
    - 속성(property) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
    - 상속 되는 것 예시
        - 예) Text 관련 요소(font, color, text-align), opacity, visibility 등
    - 상속 되지 않는 것 예시
        - 예) Box model 관련 요소(width, height, margin, padding, border, box-sizing, display), position 관련 요소(position, top/right/bottom/left, z-index) 등
        

## CSS 기본 스타일 - 크기 단위

- px (픽셀)
    - 모니터 해상도의 한 화소인 ‘픽셀’ 기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
- em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
    

### viewport

- **디바이스 화면 :** 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- `vw`, `vh`, `vmin`, `vmax`
- `px`는 브라우저의 크기를 변경해도 그대로
- `vw`는 브라우저의 크기에 따라 가변

## CSS 기본 스타일 - 색상 단위

- 색상 키워드(background-color: red;)
    - 대소문자를 구분하지 않음
    - red, blue, black과 같은 특정 색을 직접 글자로 나타냄
- RGB 색상(background-color: rgb(0, 255, 0);)
    - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
    - `#` + 16진수 표기법
    - rgb() 함수형 표기법
- HSL 색상((background-color: hsl(0, 100%, 50%);)
    - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
- a는 alpha(투명도)

## CSS 문서 표현 - 추후에 하나씩

- 텍스트
    - 서체(font-family), 서체 스타일(font-style, font-weight 등)
    - 자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
- 컬러(color), 배경(background-image, background-color)
- 기타 HTML 태그별 스타일링
    - 목록(li), 표(table)
    

## 결합자(Combinators)

- 자손 결합자(공백)
    - selectorA 하위의 모든 selectorB 요소
- 자식 결합자(>)
    - selectorA 바로 아래의 selectorB 요소
- 일반 형제 결합자(~)
    - selectorA의 형제 요소 중에 뒤에 위치하는 selectorB요소 모두 선택
- 인접 형제 경합자(+)
    - selectorA의 형제 요소 바로 뒤에 위치하는 selectorB 요소
    

## CSS 원칙

1. **모든 요소는 네모(박스 모델)이고, 위에서 아래로, 왼쪽에서 오른쪽으로 쌓인다.**
2. **모든 요소는 네모(박스 모델)이고, display에 따라 크기와 배치가 달라진다.**
3. **position으로 위치의 기준을 변경**
    - **relative** : 본인의 원래 위치
    - **absolute** : 특정 부모의 위치
    - **fixed** : 화면의 위치
    - **sticky**: 기본적으로 **static**이나 스크롤 이동에 따라 **fixed**로 변경

## CSS Box Model

- 모든 HTML 요소는 `box` 형태로 되어있음
- 하나의 박스는 네 부분(영역)으로 이루어짐
    - **margin** → 테두리 바깥의 외부 여백
        - `margin` :  4면 동시에 설정 가능
            - 1개 : 전체
            - 2개 : 상하, 좌우
            - 3개 : 상, 좌우, 하
            - 4개 : 상, 우, 하, 좌
        - `margin-top`, `margin-bottom`, `margin-right`, `margin-left` : 분할 설정 가능
    - **border** → 테두리 영역
        - `border-width`, `border-style`, `border-color` : 두께, 스타일, 색상
    - **padding** → 테두리 안쪽의 내부 여백
    - **content** → 요소의 실제 내용(글, 이미지)
    

## box-sizing

- 기본적으로 모든 요소의 **box-sizing**은 **content-box**
    - **Padding**을 제외한 순수 **contents** 영역만을 box로 지정
- 일반적으로 영역을 볼 때 border의 너비를 100px로 보는 것이기에
    - **box-sizing**을 **border-box**로 설정해야 함
    

## 대표적으로 활용되는 display

- display: block
    - 줄 바꿈이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- display: inline
    - 줄 바꿈이 일어나지 않는 행의 일부 요소
    - **content** 너비만큼 가로 폭을 차지한다.
    - `width`, `height`, `margin-top`, `margin-bottom`을 지정할 수 없다.
    - 상하 여백은 `line-height`로 지정한다.

## 블록 레벨 요소와 인라인 레벨 요소

- 블록 레벨 요소와 인라인 레벨 요소 구분
- 대표적인 블록 레벨 요소
    - `div` / `ul`, `ol`, `li` / `p` / `hr` / `form`등
- 대표적인 인라인 레벨 요소
    - `span` / `a` / `img` / `input`, `label` / `b`, `em`, `i`, `strong`등
    
- display: inline-block
    - **block**과 **inline** 레벨 요소의 특징을 모두 가짐
    - **inline**처럼 한 줄에 표시할 수 있고, **block**처럼 `width`, `height`, `margin` 속성을 모두 지정할 수 있음
- display: none
    - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    - 이와 비슷한 `visibility: hidden`은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않음

## CSS position

- 문서 상에서 요소의 위치를 지정
- **static** : 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨
- **relative** : 상대 위치
    - 자기 자신의 **static** 위치를 기준으로 이동 (normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 **static**일 때와 같음 (normal position 대비 offset)
- **absolute** : 절대 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - **static**이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)
- **fixed** : 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
    - 부모 요소와 관계 없이 **viewport**를 기준으로 이동
        - 스크롤 시에도 항상 같은 곳에 위치
- **sticky** : 스크롤에 따라 **static** → **fixed**로 변경
    - 속성을 적용한 박스는 평소에 문서 안에서 `position: static` 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 `position: fixed`와 같이 박스를 화면에 고정할 수 있는 속성

# CSS layout techniques

- Display
- Position
- Float(CSS1, 1996)
- Flexbox(2012)
- Grid
- 기타
    - Responsive Web Design(2010), media Queries(2012)

## Float

- 박스를 왼쪽 혹은 오른쪽으로 이동 시켜 텍스트를 포함 인라인 요소들이 주변을 감싸도록 함
- 요소가 Normal flow를 벗어나도록 함

### 속성

- `none`: 기본값
- `left` : 요소를 왼쪽으로 띄움
- `right` : 요소를 오른쪽으로 띄움

## Flexbox

> [felxboxfroggy](http://flexboxfroggy.com/#ko)에서 자유롭게 테스트 가능
> 

### CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
    - main axis (메인 축)
    - cross axis (교차 축)
- 구성 요소
    - Flex Container(부모 요소) → 부모 요소에 Flex를 적용 시켜야 함
    - Flex Item(자식 요소)
    

### Flex 속성

- 배치 설정
    - flex-direction
        - **메인 축** 기준 방향 설정
        - 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)
    - flex-wrap
        - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
        - 기본적으로 컨테이너 영역을 벗어나지 않도록 함
            - `wrap` : 여백이 생기더라도 아이템의 크기에 맞지 않다면 다음 줄로 배치
            - `nowrap` : 여백 없이 크기를 끼워 맞춤(한 줄에 배치)
            - (`wrap`, `nowrap`) `reverse`로 역순 배치
    - flex-flow
        - `flex-direction`과 `flex-wrap`의 shorthand
        - `flex-direction`과 `flex-wrap`의  값을 차례로 설정
- 공간 나누기
    - `justify-content` (메인 축)
    - `align-content` (교차 축)
- 정렬
    - `align-items`(모든 아이템을 교차 축 기준으로)
    - `align-self`(개별 아이템)
- justify-content
    
    > **메인 축**을 기준으로 공간 배분
    > 
    - `flex-start` : 축의 시작점에 배치
    - `flex-end` : 축의 끝에 배치(요소의 순서는 바뀌지 않음)
    - `center` : 축 중앙에 위치
    - `space-between` : 양 끝까지 균일하게 공간 배분
    - `space-around` : 각 요소의 사이의 여백 똑같이(끝과 요소 사이의 공간 배분도 똑같이)
    - `space-evenly` : 각 요소의 좌우 여백이 똑같이(각 요소 좌우에 1씩 배분 되기에 요소 사이는 2가 됨)
- align-content
    
    > **교차 축**을 기준으로 공간 배분(아이템이 한 줄로 배치되는 경우 확인할 수 없음
    > 
    - 축이 달라질 뿐, **justify**의 모든 설정과 같음
- align-items
    
    > 모든 아이템을 **교차 축**을 기준으로 정렬
    > 
    - `stretch` : 교차 축 세로로 모두 채움
    - `flex-start` : 교차 축 시작점에 정렬
    - `flex-end` : 교차 축 끝에 정렬
    - `center` : 교차 축 중앙에 정렬
    - `baseline` : text baseline에 맞춰 정렬
- align-self
    
    > 개별 아이템을 **교차 축**을 기준으로 정렬
    > 
    - 포함되는 아이템이 다를 뿐, **align-items**의 모든 설정과 같음
- 기타 속성
    - **flex-grow** : 남은 영역을 아이템에 분배
    - **order** : 배치 순서
# MVC와 템플릿 엔진

# MVC

- M : Model
    - 정보와 데이터
    - 내부 비즈니스 로직을 처리하기 위한 역할
- V : View
    - 사용자 인터페이스(UI)
    - 화면에 무엇을 보여주기 위한 역할
- C : Controller
    - 데이터와 사용자 인터페이스들을 잇는 다리
    - Model이 데이터를 어떻게 처리할지 알려주는 역할

## MVC를 활용한 렌더링

### Controller

```java
@Controller
public class HelloController {

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }
}
```

- **@RequestParam(html파일에서 사용할 변수명) 데이터타입 변수**
- **model.addAttribute(key, value)** : return 값에 설정된 String을 이름으로 가진 `resources/templates/`내에 존재한 html로 전달 →  html에서 key로 호출

### View

`resources/templates/{name}.html`

```html
<html xmlns:th="http://www.thymeleaf.org">
<body>
<p th:text="'hello ' + ${name}">hello! empty</p>
</body>
</html>
```

- **${name}** : url에서 요청하면 컨트롤러에서 받아들여 view로 전달해줄 데이터

### 웹에서 요청

- **http://localhost:8080/{Controller의 GetMapping에 적용된 이름}?{RequestParam에 세팅된 변수명}={사용자 입력}**
- **{RequestParam에 세팅된 변수명}={사용자 입력}** 미입력시 오류 발생
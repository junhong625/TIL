# View 환경설정

### 정적 파일 활용 - Welcome Page 만들기

`resources/static/index.html`

```html
<!DOCTYPE HTML>
<html>
<head>
<title>Hello</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
Hello
<a href="/hello">hello</a>
</body>
</html>
```

- 스프링 부트가 제공하는 Welcome Page 기능
    - `static/index.html`을 올려두면 Welcome page 기능을 제공

### 동적 파일 활용

`{package}/controller/HelloController`

```java
package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HelloController {

    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "spring!!");
        return "hello";
    }
}
```

- **@Controller** : Controller의 기능을 데코레이터로 부여
- **@GetMapping(”??”)** : `localhost:8080/` 뒤에 ??가 붙어 url 세팅(API)
- **model.addAttribute(key, value)** : return 값에 설정된 String을 이름으로 가진 `resources/templates/`내에 존재한 html로 전달 →  html에서 key로 호출

`resources/templates/hello.html`

```html
<!DOCTYPE HTML>
<html xmlns:th="http://www.thymeleaf.org">
<head>
  <title>Hello</title>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>
<body>
<p th:text="'안녕하세요. ' + ${data}" >안녕하세요. 손님</p>
</body>
</html>
```

- `<html xmlns:th="http://www.thymeleaf.org">` : thymeleaf 템플릿 엔진 사용
- **data** : controller에서 전달한 인자의 key
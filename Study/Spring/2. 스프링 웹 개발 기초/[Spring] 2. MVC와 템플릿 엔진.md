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

    @GetMapping("hello")
    public String hello(Model model) {
        model.addAttribute("data", "spring!!");
        return "hello";
    }

    @GetMapping("hello-mvc")
    public String helloMvc(@RequestParam("name") String name, Model model) {
        model.addAttribute("name", name);
        return "hello-template";
    }
}
```
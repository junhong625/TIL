# API

### @ResponseBody 문자 반환

```java
@Controller
public class HelloController {
	
	@GetMapping("hello-string")
	@ResponseBody
	public String helloString(@RequestParam("name") String name) {
		return "hello " + name;
	}
}
```

- `@ResponseBody`를  사용하면 뷰 리졸버(`viewResolver`)를 사용하지 않음
- 대신에 HTTP의 BODY에 문자 내용을 직접 반환(HTML BODY TAG를 말하는 것이 아님)

> http://localhost:8080/hello-string?name=spring 으로 실행
> 

### @ResponseBody 객체 반환

```java
@Controller
public class HelloController {
	@GetMapping("hello-api")
	@ResponseBody
	public Hello helloApi(@RequestParam("name") String name) {
		Hello hello = new Hello();
		hello.setName(name);
		return hello;
	}
		
	static class Hello {
		private String name;
		public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}
	}	
}
```

- `ResponseBody`를 사용하고, 객체를 반환하면 JSON으로 변환

> [http://localhost:8080/hello-api?name=spring](http://localhost:8080/hello-api?name=spring)으로 실행
> 

## @ResponseBody 사용 원리

- HTTP의 BODY에 문자 내용을 직접 반환
- `viewResolver` 대신 `HttpMessageConverter`가 동작
- 기본 문자처리 : `StringHttpMessageConverter`
- 기본 객체처리 : `MappingJackson2HttpMessageConverter`
- byte 처리 등등 기타 여러 `HttpMessageCoverter`가 기본으로 등록되어 있음
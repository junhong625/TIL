# 개발환경 세팅

### Version

| JAVA | 1.8.0_192(JDK 8) |
| --- | --- |
| Intellij | 2022.3.1(Community Edition) |

## 프로젝트 생성

### [스프링 부트 스타터](https://start.spring.io)에서 프로젝트 생성

- 프로젝트 선택
    - Project : Gradle - Groovy Project
    - Language : Java
    - Spring Boot : 2.7.7
    - Packaging : Jar
    - Java : 8
    - Dependencies : Spring Web, Thymeleaf

## 동작 확인

- 기본 메인 클래스 실행
    - `{artifact}Application` ex) : HelloSpringApplication
- 스프링 부트 메인 실행 후 에러페이지로 간단하게 동작 확인
    - http://localhost:8080
- IntelliJ Gradle → JAVA 실행으로 **변경**
    - Java로 바로 실행하는 것이 더 빠름
    - Preferences → Build, Execution, Deployment → Build Toos → Gradle
        - Build and run using : Gradle → IntelliJ IDEA
        - Run tests using : Gradle → IntelliJ IDEA
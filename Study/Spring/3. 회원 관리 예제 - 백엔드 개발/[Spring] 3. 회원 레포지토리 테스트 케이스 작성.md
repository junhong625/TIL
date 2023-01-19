# 회원 레포지토리 테스트 케이스 작성

## 테스트 방법

1. main 메서드를 통해서 실행 or 웹 애플리케이션의 컨트롤러를 통해 기능을 실행
    - 준비하고 실행하는데 오래 걸림
    - 반복하기 어려움
    - 테스트를 한 번에 실행하기 어려움
2. JUnit 프레임워크를 이용하여 테스트를 실행
    - 반복하기 쉬움
    - 테스트를 한 번에 실행이 가능

### 회원 레포지토리 메모리 구현체 테스트

> `src/test/java` 하위 폴더에 생성
> 

```java
package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

public class MemoryMemberRepositoryTest {

    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach
    public void afterEach() {
        repository.clearStore();
    }

    @Test
    public void save() {
        Member member = new Member();
        member.setName("spring");

        repository.save(member);

        Member result = repository.findById(member.getId()).get();
        assertThat(member).isEqualTo(result);
    }

    @Test
    public void findByName() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get();

        assertThat(result).isEqualTo(member1);
    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2);

    }
}
```

- `@AfterEach` : 각 테스트(=함수)가 종료될 때 마다 기능을 실행
    - 이를 활용하여 메모리 DB에 저장된 데이터를 삭제
    - 사용 이유 :
        - 테스트를 독립적으로 실행하기 위해 활용
        - 순서 의존 관계를 피하기 위해 활용
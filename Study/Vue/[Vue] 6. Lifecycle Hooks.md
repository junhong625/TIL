# Lifecycle Hooks

- 각 `Vue 인스턴스`는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
    - `Vue 인스턴스`가 생성된 경우, 인스턴스를 `DOM`에 마운트하는 경우, 데이터가 변경되어 `DOM`를 업데이트하는 경우 등
- 각 단계가 트리거가 되어 특정 로직을 실행할 수 있음
- 이를 `Lifecycle Hooks`이라고 함

### Lifecycle Hooks 특징

- `instance`마다 각각의 `Lifecycle`을 가지고 있음
- `Lifecycle Hooks`는 컴포넌트별로 정의할 수 있음
- `ParentComponent` 생성 ⇒ `ChildComponent` 생성 ⇒ `ChildeComponent` 부착 ⇒ `ParentComponent` 부착 ⇒ `ChildComponent` 업데이트
- 부모 컴포넌트의 `mounted hook`이 실행 되었다고 해서 자식이 `mount`된 것이 아니고, 부모 컴포넌트가 `updated hook`이 실행 되었다고 해서 자식이 `updated`된 것이 아님
    - 부모-자식 관계에 따라 순서를 가지고 있지 않다.
- **즉, instance마다 각각의 Lifecycle을 가지고 있다.**

## Lifecycle Hooks 흐름

### created

- `Vue instance`가 생성된 후 호출됨
- `data`, `computed` 등의 설정이 완료된 상태
- 서버에서 받은 데이터를 `Vue instance`의 `data`에 할당하는 로직을 구현하기 적합
- 단, `mount`되지 않아 요소에 접근할 수 없음
    - `dogComponent.vue`
        
        ```
        <template>
          <div>
            <button @click="getDogImage">멍멍아 이리온</button><br><br>
            <img v-if="imgSrc" :src="imgSrc" alt="#"><br>
          </div>
        </template>
        
        <script>
        import axios from 'axios'
        
        export default {
          name:'DogComponent',
          data() {
            return {
              imgSrc: null,
            }
          },
          methods:{
            getDogImage() {
              const dogImageSearchURL = 'https://dog.ceo/api/breeds/image/random'
              
              axios({
                method: 'get',
                url: dogImageSearchURL
              })
                .then((response) => {
                  const imgSrc = response.data.message
                  this.imgSrc = imgSrc
                })
                .catch((error) => {
                  console.log(error)
                })
            }
          },
          created() {
            this.getDogImage()
          }
        }
        </script>
        ```
        

### mounted

- `Vue instance`가 요소에 `mount`된 후 호출됨
- `mount`된 요소를 조작할 수 있음
- `dogComponent.vue`
    
    ```jsx
      ...	
      mounted() {
        const button = document.querySelector('button')
        btn.innerText = '멍멍'
      }
    }
    ```
    

### updated

- 데이터가 변경되어 `DOM`에 변화를 줄 때 호출됨
- `dogComponent.vue`
    
    ```
    ...
    updated() {
        console.log('새로운 멍멍!')
      }
    ```
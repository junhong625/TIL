package hello.hellospring.controller;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

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

    @GetMapping("hello-string")
    @ResponseBody
    public String helloString(@RequestParam("name") String name) {
        return "hello " + name;
    }

    @GetMapping("test-api")
    @ResponseBody
    public String testAPI(@RequestParam("region") int region, @RequestParam("date") String date) {
        Hello hello = new Hello();
        hello.setDate(date);
        hello.setRegion(region);
        return hello.getYear()+"년 "+hello.getMonth()+"월 "+hello.getDay()+"일 점심<br><br>메인 메뉴 : 일본식 함박스테이크<br><br>서브 메뉴 : 야채, 야채, 야채";
    }

    static class Hello {
        private int region;
        private String year, month, day;

        public int getRegion() {
            return region;
        }

        public void setRegion(int region) {
            this.region = region;
        }

        public String getYear() {
            return year;
        }
        public String getMonth() {
            return month;
        }
        public String getDay() {
            return day;
        }

        public void setDate(String date) {
            this.year = date.substring(0,4);
            this.month = date.substring(4,6);
            this.day = date.substring(6,8);
        }
    }
}

package com.sparta.week01.prac;

import java.util.ArrayList;
import java.util.List;

public class PracBasic01 {

    public static void main(String[] args) {
        System.out.println("안녕, 스파르타!");

        // 숫자
        int a = 7;
        int b = 3;
        float c = 3.7f;
        long d = 10000000000L;
        System.out.println(d);

        // 문자열
        String myName = "강미진";
        String myName2 = "홍길동";
        String myName3 = myName + myName2;
        System.out.println(myName3);

        // boolean
        int myAge = 20;
        boolean isAdult = myAge > 20;
        boolean isKid = myAge <= 20;
        System.out.println(isAdult);
        System.out.println(isKid);
        System.out.println(myAge == 20);    // true
        System.out.println(myAge != 20);    // false

        // 배열 - List
        List<String> myList = new ArrayList<>();
        String course_1 = "웹개발의 봄 Spring";
        String course_2 = "프론트엔드의 꽃, React";
        myList.add(course_1);
        myList.add(course_2);
        System.out.println(myList);
        System.out.println(myList.get(1));
        myList.remove(1);
        System.out.println(myList);

        // 연습퀴즈
        // course1 이라는 이름의 변수에 값을 "웹개발 종합반", course2 라는 이름의 변수에 값을 "앱개발 종합반",
        // 넣고, course1과 course2를 courseList라는 배열에 순서대로 넣으려면 어떻게 해야 할까요?
        String course1 = "웹개발 종합반";
        String course2 = "앱개발 종합반";

        List<String> courseList = new ArrayList<>();
        courseList.add(course1);
        courseList.add(course2);
        System.out.println(courseList);
    }
}

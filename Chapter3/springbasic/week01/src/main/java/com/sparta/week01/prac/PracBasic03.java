package com.sparta.week01.prac;

import java.util.ArrayList;
import java.util.List;

public class PracBasic03 {
    public static void main(String[] args) {
        List<String> fruits = new ArrayList<>();
        fruits.add("감");
        fruits.add("배");
        fruits.add("감");
        fruits.add("딸기");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("딸기");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("메론");
        fruits.add("수박");
        fruits.add("감");
        System.out.println(fruits);

        for (int i=0; i<fruits.size(); i++){
            String fruit = fruits.get(i);
            System.out.println(fruit);
        }

        System.out.println();

        // 연습퀴즈
        // 주어진 연예인 목록을 차례대로 하나씩 인쇄하는 반복문을 작성해보세요.
        List<String> celebs = new ArrayList<>();
        celebs.add("아이유");
        celebs.add("린다G");
        celebs.add("은비");
        celebs.add("금비");
        celebs.add("비");
        celebs.add("차은우");
        celebs.add("남주혁");
        celebs.add("수지");
        celebs.add("정우성");
        celebs.add("제니");
        celebs.add("정국");

        for(int i=0; i<celebs.size(); i++){
            String celeb = celebs.get(i);
            System.out.println(celeb);
        }
    }
}

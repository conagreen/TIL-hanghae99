package com.sparta.week01.prac;

import java.util.ArrayList;
import java.util.List;

public class PracBasic05 {
    public static int countFruit(String fruit) {
        List<String> fruitList = new ArrayList<>();
        fruitList.add("감");
        fruitList.add("배");
        fruitList.add("감");
        fruitList.add("딸기");
        fruitList.add("수박");
        fruitList.add("메론");
        fruitList.add("수박");
        fruitList.add("딸기");
        fruitList.add("메론");
        fruitList.add("수박");
        fruitList.add("메론");
        fruitList.add("수박");
        fruitList.add("감");

        int count = 0;

        for (int i = 0; i < fruitList.size(); i++) {
            if (fruitList.get(i) == fruit){
                count++;
            }
        }
        return count;
    }
    public static void main(String[] args) {
        // 연습퀴즈 - 조건문 + 반복문
        // 주어진 과일의 개수를 세고 그 수를 반환하는 메소드를 만들어보세요
        int gam = countFruit(("감"));
        int subak = countFruit(("수박"));
        System.out.println(gam);
        System.out.println(subak);

    }
}

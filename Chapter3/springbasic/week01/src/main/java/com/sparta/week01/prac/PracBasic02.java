package com.sparta.week01.prac;

public class PracBasic02 {
    // 파라미터 X, 반환값 X
    public static void simplePrint() {
        System.out.println("파라미터도 없고, 반환값도 없어요!");
    }

    // 파라미터 O, 반환값 X
    public static void simpleSum(int num1, int num2) {
        System.out.println("num1 :" + num1 + ", num2: " + num2);
    }

    // 파라미터 X, 반환값 O
    public static int simpleReturn() {
        return 3;
    }

    // 파라미터 O, 반환값 O
    public static int sum(int num1, int num2) {
        return num1 + num2;
    }

    // 연습퀴즈 - 메소드
    public static int sub(int num1, int num2){
        return num1 - num2;
    }

    public static void main(String[] args) {
        simplePrint();
        simpleSum(1, 2);
        int ret = simpleReturn();
        System.out.println(ret);
        int ret2 = sum(10, 7);
        System.out.println(ret2);

        // 연습퀴즈
        // 두 정수를 받아서, 뺀 값을 반환하는 메소드를 만들고, 그 값을 인쇄해보세요!
        // (메소드명은 자유롭게 지으세요)
        int ret3 =  sub(10, 5);
        System.out.println(ret3);
    }
}

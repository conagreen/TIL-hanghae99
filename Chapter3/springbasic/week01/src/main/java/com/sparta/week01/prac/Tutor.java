package com.sparta.week01.prac;

public class Tutor {
    // 연습퀴즈
    // 1) Tutor 클래스를 만들고, 이름(name)과, 경력(bio) 멤버 변수를 추가하세요.
    // 2) 그리고 각 변수를 private으로 선언하고, Getter와 Setter를 만들어보세요.
    // 3) 마지막으로, 기본 생성자와, name/bio 입력받는 생성자 두 개를 만들어보세요.

    // 기본 생성자
    public Tutor(){

    }

    // 생성자
    private Tutor(String name, int bio){
        this.name = name;
        this.bio = bio;
    }

    private String name;
    private int bio;

    // Getter
    public String getName() {
        return name;
    }

    public int getBio() {
        return bio;
    }

    // Setter
    public void setName(String name) {
        this.name = name;
    }

    public void setBio(int bio) {
        this.bio = bio;
    }
}

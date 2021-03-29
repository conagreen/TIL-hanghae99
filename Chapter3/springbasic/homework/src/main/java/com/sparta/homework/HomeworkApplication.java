package com.sparta.homework;

import com.sparta.homework.domain.Person;
import com.sparta.homework.domain.PersonRepository;
import com.sparta.homework.domain.PersonRequestDto;
import com.sparta.homework.service.PersonService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.data.jpa.repository.config.EnableJpaAuditing;

import java.util.List;

@EnableJpaAuditing
@SpringBootApplication
public class HomeworkApplication {

    public static void main(String[] args) {
        SpringApplication.run(HomeworkApplication.class, args);
    }

    @Bean
    public CommandLineRunner demo(PersonRepository personRepository, PersonService personService){
      return (args) -> {
          personRepository.save(new Person("강미진", "행복한개발자"));

          System.out.println("데이터 인쇄");
          List<Person> personList = personRepository.findAll();
          for (int i=0; i<personList.size(); i++){
              Person person = personList.get(i);
              System.out.println(person.getId());
              System.out.println(person.getName());
              System.out.println(person.getJob());

          }

          PersonRequestDto requestDto = new PersonRequestDto("강미진", "유능한개발자");
          personService.update(1L, requestDto);
          personList = personRepository.findAll();
          for(int i=0; i<personList.size(); i++){
              Person person = personList.get(i);
              System.out.println(person.getId());
              System.out.println(person.getName());
              System.out.println(person.getJob());

          }
      };
    }
}

# TDD란?
테스트 주도 개발(Test-driven development TDD)은 매우 짧은 개발 사이클을 반복하는 소프트웨어 개발 프로세스 중 하나이다.

## Test
- 기능 테스트(Functional Test, FT) : 애플리케이션이 어떻게 **동작(functions)**하는지 사용자 관점에서 애플리케이션 외부를 테스트
- 단위 테스트(Unit Test) : 프로그래머 관점에서 내부를 테스트

## TDD 프로세스
- 기능 테스트(Functional tests)
- 단위 테스트(Unit tests)
- 단위 테스트-코드 주기(Unit test-code cycle)
    - 단위테스트를 실행해 어떻게 실패하는지 확인
    - 현재 실패 테스트를 수정하기 위한 **최소한**의 코드 변경
- 리팩토링(Refactoring) : **기능(결과물)은 바꾸지 않고** 코드 자체를 개선하는 작업

## TDD 작업 흐름
- 이중 루프 TDD
- 레드, 그린, 리팩터
- 삼각
- 작업 메모장
- 스트라이크 세 개면 리팩터 : 같은 코드가 세 번 등장하게 되면 중복을 제거
- YAGNI : You ain't gonna need it. 창의적이지만 과도한 열정을 억제해주는 경전

# 프로젝트 생성, 관리
```shell
# 크롬에서 테스트하기 위한 웹 드라이버 설치
$ brew install chromedriver

$ mkdir tdd_hw
$ cd tdd_hw

# 가상환경 생성
$ pyenv virtualenv 3.4.3 tdd_hw

# 가상환경 적용
$ pyenv local tdd_hw

# Django 1.7 설치
$ pip install django==1.7

# selenium 설치
$ pip install --upgrade selenium

# Django Project 생성
$ django-admin startproject superlists

# Django Project 이름 변경
$ mv superlists django_app

# 프로젝트 구성확인
.
├── functional_tests.py
├── django_app
│   ├── manage.py
│   ├── superlists
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
└── requirements.txt
```

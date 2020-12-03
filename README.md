# 영화 추천 웹 페이지 제작

---

## **팀원 정보 및 업무 분담 내역**

### 1) Front-end(Vue) : 김진웅

- Vuex를 활용한 로그인 상태 관리 (login, logout, signup)
- DB에 저장된 영화 정보를 불러와 카드 형태로 정보 제공
- 영화 상세정보를 모달 형태로 제공 (youtube API 활용)
- 영화 리뷰 작성 및 댓글 작성 기능 구현 (CRUD)
- 관리자 페이지 제작 및 staff 권한 부여 기능 구현
- 추천된 영화를 카드 형식으로 제공
- DB에 저장된 배우 이미지를 활용한 이상형 월드컵 기능 구현

### 2) Back-end(Django) : 이연재

- Selenium을 활용한 영화 진흥 위원회 데이터 크롤링 및 모델 구축
- Selenium을 활용한 위키 백과 및 네이버 프로필 배우 사진 크롤링 및 모델 구축
- Django rest-framework(Serializer)을 이용한 데이터 JSON화 및 서버 구축 및 실행
- 기본적인 Django ORM을 이용한 쿼리문 작성 및 데이터 필터링 실행
- 날씨 기반 영화 추천을 위한 공공 데이터 API 서버 구축 및 코드 작성 및 실행
- 사용자의 영화 평점을 기반으로 하는 추천을 위한 알고리즘 작성 및 실행

---

## 목표 서비스 구현 및 실제 구현 정도

- [ ]  크롤링을 활용한 영화 데이터 수집
    - Selenium을 활용하여 영화진흥위원회에서 영화관련정보 크롤링
    - Selenium을 이용하여 위키백과, 네이버 배우 프로필 크롤링

- [ ]  반응형 웹 구현
    - 화면의 비율에 맞게 변환되는 반응형 웹 구현

- [ ]  CSS 및 라이브러리를 활용한 웹 사이트 디자인
    - Vuetify를 활용한 전체적인 웹 사이트 디자인
    - 모달을 이용하여 영화 상세 정보 제공
    - Youtube iframe을 활용한 영화 예고편 제공

- [ ]  평점을 활용한 추천 알고리즘
    - 유저가 영화에 대한 평점을 남긴다.
    - 해당 유저가 선호하는 영화 장르를 선별하기 위한 기준으로 평점 4점 이상의 영화를 정재한다.
    - 평점 4점 이상의 영화 중에 가장 많이 나온 장르를 유저에게 추천한다.

- [ ]  날씨API를 활용한 추천 알고리즘
    - 유저가 현재 위치하고 있는 지역을 select를 이용하여 선택한다.
    - 공공데이터포털의 API URL로 해당 지역을 매개변수로 요청을 보내고 받아온 JSON형식의 날씨 데이터를 정재하여 유저가 있는 지역의 날씨 정보를 알아낸다.
    - 날씨가 '비 / 눈'이 오면 로맨스, 드라마, 가족 장르 영화를 추천한다.
    - 날씨가 '맑음' 이면 애니메이션, 코미디, 뮤지컬 장르 영화를 추천한다.
    - 날씨가 '구름많음'이면 액션, 사극, 판타지, SF, 어드벤처 장르 영화를 추천한다.
    - 날씨가 '흐림'이면 미스터리, 스릴러, 공포(호러), 범죄 영화를 추천한다.

- [ ]  이상형 월드컵 추천 알고리즘
    - Selenium을 활용한 위키백과, 네이버 배우 프로필 사진을 크롤링한다.
    - 1대1 형식으로 32강부터 결승까지 진행한다.
    - 우승한 배우가 출연한 영화에 대해서 추천한다.

---

## 데이터 베이스 모델링 (ERD)

![](README.assets/movie_db (1).png)

---

## 필수기능

- 관리자 뷰
- [x]  관리자 권한의 유저만 영화 등록 / 수정 / 삭제 권한을 가집니다.
- [x]  권리자 권한의 유저만 유저 관리 권한을 가집니다.

- 영화 정보
- [x]  영화 정보는 Database Seeding을 활용해 최소 50개 이상의 데이터가 존재하도록 구성해야 합니다.
- [x]  모든 로그인 된 유저는 영화에 대한 평점 등록 / 수정 / 삭제 등을 할 수 있어야 합니다.

- 추천 알고리즘
- [x]  평점을 등록한 유저는 해당 정보를 기반으로 영화를 추천 받을 수 있어야 합니다.
- [x]  추천 알고리즘의 지정된 형식은 없으나, 사용자는 반드시 최소 1개 이상의 방식으로 영화를 추천 받을 수 있어야 합니다.
- [x]  추천 방식은 각 팀별로 자유롭게 선택할 수 있으며 어떠한 방식으로 추천 시스템을 구성 했는지 설명할 수 있어야 합니다.

- 커뮤니티
- [x]  영화 정보와 관련된 대화를 할 수 있는 커뮤니티 기능을 구현해야 합니다.
- [x]  로그인한 사용자만 글을 조회 / 생성 할 수 있으며 작성자 본인만 글을 수정 / 삭제 할 수 있습니다.
- [x]  사용자는 작성된 게시글에 댓글을 작성할 수 있어야 하며 작성자 본인만 댓글을 삭제 할 수 있습니다.
- [x]  각 게시글 및 댓글은 생성 및 수정 시각 정보가 포함되어야 합니다.

- 심화
- [x]  게시글 pagination 활용
- [x]  복수의 기능 게시판 구성
- [x]  권한을 나누어 유저 관리 (예 - 관리자, 스태프 등)

---

## 배포 서버 URL

https://nervous-swartz-5a0624.netlify.app/

---

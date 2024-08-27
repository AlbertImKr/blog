# 블로그 프로젝트

이 프로젝트는 모두연 오름캠프 백엔드 2기 미니프로젝트이며 실제로 사용할 수 있는 블로그 시스템으로 개발하고자 하는 목표를 가지고 있습니다.

## WBS

[![WBS](https://github.com/user-attachments/assets/b02561f9-53d1-428c-bfed-e7c48cbd26bc)](https://github.com/users/AlbertImKr/projects/5/views/2)

## ERD

[![ERD](https://github.com/user-attachments/assets/17c8389e-2df6-4da5-a6e9-b76e726f8b1a)](https://www.erdcloud.com/d/48L5ncfrCxRGcuixX)

## URL 구조

### 게시글 App

| URL                                         | HTTP METHOD | Views Function | HTML File Name | Note       |
|---------------------------------------------|-------------|----------------|----------------|------------|
| `/`                                         | `GET`       |                |                | 홈화면        |
| `/posts/new`                                | `GET`       |                |                | 게시글 작성 페이지 |
| `/posts/`                                   | `POST`      |                |                | 게시글 생성     |
| `/posts/?tag=:tag&title=:title&sort=:sort/` | `GET`       |                |                | 게시글 검색     |
| `/posts/:pk/detail/`                        | `GET`       |                |                | 게시글 수정 페이지 |
| `/posts/:pk/`                               | `PUT`       |                |                | 게시글 수정     |
| `/posts/:pk/`                               | `DELETE`    |                |                | 게시글 삭제     |

### 유저 App

| URL                    | HTTP METHOD | Views Function | HTML File Name | Note           |
|------------------------|-------------|----------------|----------------|----------------|
| `/users/:pk/`          | `GET`       |                |                | 유저 개인 페이지      |
| `/users/:pk/profile/`  | `GET`       |                |                | 유저 프로필 수정 페이지  |
| `/users/:pk/profile/`  | `PUT`       |                |                | 유저 프로필 수정      |
| `/users/:pk/password/` | `GET`       |                |                | 유저 비밀번호 수정 페이지 |
| `/users/:pk/password/` | `PUT`       |                |                | 유저 비밀번호 수정     |
| `/signin/`             | `GET`       |                |                | 로그인 페이지        |
| `/signin/`             | `POST`      |                |                | 로그인            |
| `/signout/`            | `POST`      |                |                | 로그아웃           |
| `/signup/`             | `GET`       |                |                | 회원가입 페이지       |
| `/signup/`             | `POST`      |                |                | 회원가입           |






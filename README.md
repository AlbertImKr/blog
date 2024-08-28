# 블로그 프로젝트

이 프로젝트는 모두연 오름캠프 백엔드 2기 미니프로젝트이며 실제로 사용할 수 있는 블로그 시스템으로 개발하고자 하는 목표를 가지고 있습니다.

## WBS

[![WBS1](https://github.com/user-attachments/assets/c62ad0c2-2271-45e3-8faa-bf9f70d8b58a)](https://github.com/users/AlbertImKr/projects/5/views/2)
[![WBS2](https://github.com/user-attachments/assets/4041ec85-08dd-4279-a96e-aa1a86638f41)](https://github.com/users/AlbertImKr/projects/5/views/2)

## ERD

[![ERD](https://github.com/user-attachments/assets/4d5d90a2-7577-42cf-8775-de00d869f4e6)](https://www.erdcloud.com/d/48L5ncfrCxRGcuixX)

## URL 구조

### 게시글 App

| URL                                         | HTTP METHOD | Views Function   | HTML File Name               | Note       |
|---------------------------------------------|-------------|------------------|------------------------------|------------|
| `/`                                         | `GET`       | `HomeView`       | `post/index.html`            | 홈화면        |
| `/posts/new`                                | `GET`       | `PostCreateView` | `post/post_form.html`        | 게시글 작성 페이지 |
| `/posts/new`                                | `POST`      | `PostCreateView` | `post/post_form.html`        | 게시글 생성     |
| `/posts/?tag=:tag&title=:title&sort=:sort/` | `GET`       |                  |                              | 게시글 검색     |
| `/posts/:pk/`                               | `GET`       | `PostDetailView` | `post/post_detail.html`      | 게시글 개별 조회  |
| `/posts/:pk/edit/`                          | `GET`       | `PostUpdateView` | `post/post_update_form.html` | 게시글 수정 페이지 |
| `/posts/:pk/edit/`                          | `POST`      | `PostUpdateView` | `post/post_update_form.html` | 게시글 수정     |
| `/posts/:pk/`                               | `DELETE`    |                  |                              | 게시글 삭제     |

### 유저 App

| URL                    | HTTP METHOD | Views Function | HTML File Name     | Note           |
|------------------------|-------------|----------------|--------------------|----------------|
| `/users/:pk/`          | `GET`       |                |                    | 유저 개인 페이지      |
| `/users/:pk/profile/`  | `GET`       |                |                    | 유저 프로필 수정 페이지  |
| `/users/:pk/profile/`  | `PUT`       |                |                    | 유저 프로필 수정      |
| `/users/:pk/password/` | `GET`       |                |                    | 유저 비밀번호 수정 페이지 |
| `/users/:pk/password/` | `PUT`       |                |                    | 유저 비밀번호 수정     |
| `/signin/`             | `GET`       | `SignInView`   | `user/signin.html` | 로그인 페이지        |
| `/signin/`             | `POST`      | `SignInView`   | `user/signin.html` | 로그인            |
| `/signout/`            | `POST`      | `SignOutView`  |                    | 로그아웃           |
| `/signup/`             | `GET`       | `SignupView`   | `user/signup.html` | 회원가입 페이지       |
| `/signup/`             | `POST`      | `SignupView`   | `user/signup.html` | 회원가입           |






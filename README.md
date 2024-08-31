# 블로그 프로젝트

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

이 프로젝트는 모두연 오름캠프 백엔드 2기 미니프로젝트이며 실제로 사용할 수 있는 블로그 시스템으로 개발하고자 하는 목표를 가지고 있습니다.

## WBS

[![WBS1](https://github.com/user-attachments/assets/c62ad0c2-2271-45e3-8faa-bf9f70d8b58a)](https://github.com/users/AlbertImKr/projects/5/views/2)
[![WBS2](https://github.com/user-attachments/assets/4041ec85-08dd-4279-a96e-aa1a86638f41)](https://github.com/users/AlbertImKr/projects/5/views/2)

## ERD

[![ERD](https://github.com/user-attachments/assets/151e6fce-1a4e-4eed-8073-bc6a55c186bf)](https://www.erdcloud.com/d/48L5ncfrCxRGcuixX)

## URL 구조

### 게시글 App

| URL                     | HTTP METHOD  | Views Function             | HTML File Name                      | Note               |
|-------------------------|--------------|----------------------------|-------------------------------------|--------------------|
| `/`                     | `GET`        | `HomeView`                 | `post/index.html`                   | 홈화면                |
| `/posts/new/`           | `GET`,`POST` | `PostCreateView`           | `post/post_form.html`               | 게시글 생성             |
| `/posts/?keyword=:q`    | `GET`        | `PostListView`             | `post/post_list.html`               | 게시글 조회             |
| `/posts/:pk/`           | `GET`        | `PostDetailView`           | `post/post_detail.html`             | 게시글 개별 조회          |
| `/posts/:pk/edit/`      | `GET`,`POST` | `PostUpdateView`           | `post/post_update_form.html`        | 게시글 수정             |
| `/posts/:pk/`           | `POST`       | `DeletePostView`           | `NONE`                              | 게시글 삭제             |
| `/posts/fragment/`      | `GET`        | `PostListFragmentView`     | `post/post_list_fragment.html`      | 게시글 조회 조각 조회       |
| `/posts/fragment/grid/` | `GET`        | `PostListFragmentGridView` | `post/post_list_fragment_grid.html` | 게시글 조회 조각 조회(Grid) |
| `/categories/`          | `GET`        | `CategoryListView`         | `post/category_list.html`           | 카테고리 조회            |

### 유저 App

| URL                                 | HTTP METHOD   | Views Function             | HTML File Name                 | Note         |
|-------------------------------------|---------------|----------------------------|--------------------------------|--------------|
| `/users/:pk/`                       | `GET`         |                            |                                | 유저 개인 페이지    |
| `/users/:pk/profile/`               | `GET`,`POST`  |                            |                                | 유저 프로필 수정    |
| `/users/:pk/password/`              | `GET`,`POST`  |                            |                                | 유저 비밀번호      |
| `/signin/`                          | `GET` ,`POST` | `SignInView`               | `user/signin.html`             | 로그인          |
| `/signout/`                         | `POST`        | `SignOutView`              | `NONE`                         | 로그아웃         |
| `/signup/`                          | `GET`,`POST`  | `SignupView`               | `user/signup.html`             | 회원가입 페이지     |
| `/users/manage/`                    | `GET`         | `UserManageView`           | `user/manage.html`             | 유저 관리페이지     |
| `/users/posts/?keyword=:q`          | `GET`         | `UserPostListView`         | `user/posts.html`              | 유저 개시글 조회    |
| `/users/posts/fragment/?keyword=:q` | `GET`         | `UserPostListFragmentView` | `user/post_list_fragment.html` | 유저 개시글 조각 조회 |







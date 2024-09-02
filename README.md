# 블로그 프로젝트

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

이 프로젝트는 모두연 오름캠프 백엔드 2기 미니 프로젝트로 시작되었지만 실제로 사용할 수 있는 블로그 시스템을 개발하고자 하는 욕심을 가지고 진행했습니다. UI는 Bootstrap 블로그 템플릿을 구매하여
적용하였고 백엔드는 Django를 사용했습니다. 추가로 필요한 프론트엔드 기능은 Vanilla JS로 구현했습니다. 배포는 완료하지 않았으나 S3와 연동하여 이미지 업로드 기능은 구현했습니다.

## WBS

[![WBS1](https://github.com/user-attachments/assets/f108f6a4-079c-434b-937b-877a360f74a9)](https://github.com/users/AlbertImKr/projects/5/views/2)
[![WBS2](https://github.com/user-attachments/assets/6c476877-b688-47c3-a689-47a35112a933)](https://github.com/users/AlbertImKr/projects/5/views/2)

## ERD

[![ERD](https://github.com/user-attachments/assets/1534f88d-f390-450b-a110-96637a5afb28)](https://www.erdcloud.com/d/48L5ncfrCxRGcuixX)

## URL 구조

### 게시글 App

| URL                     | HTTP METHOD  | Views Function             | HTML File Name                      | Note           |
|-------------------------|--------------|----------------------------|-------------------------------------|----------------|
| `/`                     | `GET`        | `HomeView`                 | `post/index.html`                   | 홈화면            |
| `/posts/new/`           | `GET`,`POST` | `PostCreateView`           | `post/post_form.html`               | 게시글 생성         |
| `/posts/?keyword=:q`    | `GET`        | `PostListView`             | `post/post_list.html`               | 게시글 조회         |
| `/posts/:pk/`           | `GET`        | `PostDetailView`           | `post/post_detail.html`             | 게시글 개별 조회      |
| `/posts/:pk/edit/`      | `GET`,`POST` | `PostUpdateView`           | `post/post_update_form.html`        | 게시글 수정         |
| `/posts/:pk/delete/`    | `POST`       | `DeletePostView`           | `NONE`                              | 게시글 삭제         |
| `/posts/fragment/`      | `GET`        | `PostListFragmentView`     | `post/post_list_fragment.html`      | 게시글 조회 조각      |
| `/posts/fragment/grid/` | `GET`        | `PostListFragmentGridView` | `post/post_list_fragment_grid.html` | 게시글 조회 조각(Grid) |
| `/categories/`          | `GET`        | `CategoryListView`         | `post/category_list.html`           | 카테고리 조회        |

### 유저 App

| URL                                 | HTTP METHOD   | Views Function             | HTML File Name                 | Note         |
|-------------------------------------|---------------|----------------------------|--------------------------------|--------------|
| `/users/:pk/profile/`               | `GET`,`POST`  | `UserProfileUpdateView`    | `user/profile-edit.html`       | 유저 프로필 수정    |
| `/users/:pk/password/`              | `POST`        | `UserPasswordChangeView`   | `NONE`                         | 유저 비밀번호 변경   |
| `/signin/`                          | `GET` ,`POST` | `SignInView`               | `user/signin.html`             | 로그인          |
| `/signout/`                         | `POST`        | `SignOutView`              | `NONE`                         | 로그아웃         |
| `/signup/`                          | `GET`,`POST`  | `SignupView`               | `user/signup.html`             | 회원가입         |
| `/users/manage/`                    | `GET`         | `UserManageView`           | `user/manage.html`             | 유저 관리페이지     |
| `/users/posts/?keyword=:q`          | `GET`         | `UserPostListView`         | `user/posts.html`              | 유저 개시글 조회    |
| `/users/posts/fragment/?keyword=:q` | `GET`         | `UserPostListFragmentView` | `user/post_list_fragment.html` | 유저 개시글 조회 조각 |

### 이미지 App

| URL                           | HTTP METHOD | Views Function             | HTML File Name      | Note                |
|-------------------------------|-------------|----------------------------|---------------------|---------------------|
| `api/generate-presigned-url/` | `GET`       | `GeneratePresignedUrlView` | `{ url: ... }`      | S3 presigned URL 요청 |
| `api/upload-image/`           | `POST`      | `UploadImageView`          | `{ image_id: ... }` | image 저장            |              

## 구현 상세

1. 홈화면
    - 게시물 목록이 기본적으로 표시됩니다.
    - 인기 게시물, 카테고리, 태그 목록도 추가로 표시됩니다.
    - 사용자가 "더보기" 버튼을 클릭하면 추가 게시물이 로드됩니다.
    - 카테고리, 유저네임, 태그, 포스터를 클릭하면 해당 페이지로 이동합니다.

   ![홈화면1](https://github.com/user-attachments/assets/534bc023-c6b4-447e-bd04-dc9a2d3d805d)

2. 게시글 생성, 수정
    - 이미지 첨부 기능은 S3 Presigned URL을 제공하여 업로드하도록 구현했습니다.
    - Quill WYSIWYG 에디터를 사용하며 Quill에서 제공하는 Delta형식의 JSON 데이터를 데이터베이스에 저장하도록 구현했습니다.

   ![게시글 생성 ,수정 페이지](https://github.com/user-attachments/assets/cef5706f-43a6-4d38-aee7-45c2d59a706b)

3. 게시글 조회
    - Ajax를 사용하여 다음 페이지의 목록을 동적으로 가져오도록 구현했습니다.
    - 인기 게시물과 카테고리 목록도 추가로 표시됩니다.
    - 주어진 검색어를 바탕으로 게시글을 필터링할 수 있는 기능을 구현했습니다.
        - 타이틀 검색: 기본 검색어로 게시글을 검색합니다.
        - 유저네임 검색: @ 기호로 시작하는 검색어로 유저이름을 검색합니다.
        - 카테고리 검색: ! 기호로 시작하는 검색어로 카테고리를 검색합니다
        - 태그 검색: # 기호로 시작하는 검색어로 태그를 검색합니다.

   ![게시글 조회](https://github.com/user-attachments/assets/09f95186-ae27-46eb-807a-bee413c2745b)

4. 게시글 삭제
    - 게시글 삭제 기능은 모달을 사용하여 구현했습니다.
    - Ajax를 사용하여 게시글을 삭제하더라도 현재 페이지에 머물며 데이터는 업데이트됩니다.

   ![게시글 삭제](https://github.com/user-attachments/assets/e60efadc-1f14-4d9b-bc0c-0dcea3dfc0f4)

5. 카테고리 조회

   ![카테고리 조회](https://github.com/user-attachments/assets/899e9d6a-9b19-4ad6-ba3b-9502f6f28925)

6. 유저 프로필 수정 및 비번 수정
    - 비밀번호 수정 시 성공 및 실패 메시지를 표시하도록 구현했습니다.

   ![프로필 및 비번 수정](https://github.com/user-attachments/assets/4dbb857f-a7be-4f36-8163-f948740e17ca)
   ![성공](https://github.com/user-attachments/assets/ef281845-a848-4bac-b150-b9b29dc2ad97)
   ![실패](https://github.com/user-attachments/assets/0cb5ff78-0c92-4c35-b3e6-f1bd5e9da74a)

7. 로그인
    - 로그인 실패 시 에러 메시지를 표시하도록 구현했습니다.
    - 로그인 성공 시 홈 페이지로 이동하며 네비게이션 바에 개인 설정 링크를 추가했습니다.

   ![회원 로그인](https://github.com/user-attachments/assets/a0149a94-990d-4fed-8a28-f2afa9857f00)

8. 로그아웃

   ![로그아웃](https://github.com/user-attachments/assets/c8b9be78-4520-4ece-8392-f79811c6ebe4)

9. 회원 가입

   ![회원가입](https://github.com/user-attachments/assets/2ad6249d-370b-4b26-8d50-c9af2bd05fcd)

10. 유저 관리페이지

- 해당 유저의 게시글을 페이지네이션으로 가져오고 총 게시글 개수를 표시하도록 구현했습니다.

![유저 관리페이지](https://github.com/user-attachments/assets/d253b781-1291-4958-89e5-bca706e0686e)

11. 유저 게시글 조회

- 선택한 유저의 게시글을 페이지네이션으로 가져와 표시하도록 구현했습니다.
- 게시글 검색 및 정렬 기능도 지원합니다.

![유저 게시글 조회](https://github.com/user-attachments/assets/af545d6a-2fd6-4fcb-9a0b-69a72462ed66)

## 느낀점

1. 작업 범위 조정의 중요성
    - 프로젝트를 기간 내에 완성하기 위해서는 적절한 작업 범위를 설정하는 것이 중요하다는 것을 깨달았습니다. Django에 집중하기보다는 보이는 화면에 지나치게 신경을 쓴 결과 계획한 기능의 90% 이상은
      구현했지만 나머지 10%가 완성되지 않아 아쉬움이 있습니다.
2. Django의 강력함
    - 프로젝트 초기에 view를 사용하여 기능을 구현한 후 피드백을 받고 리팩토링하면서 generic view와 auth view 등을 활용하게 되었습니다. 이 과정에서 Django의 강력함과 코드의 간소화를
      직접 경험할 수 있었습니다. Django의 다양한 기능을 효과적으로 활용하면 코드가 훨씬 깔끔해지고 유지보수가 용이해진다는 것을 느꼈습니다.
3. 프론트엔드와 백엔드 작업의 병행
    - 혼자서 백엔드와 프론트엔드를 모두 작업하다 보니 불편함을 느꼈습니다. 백엔드와 프론트엔드를 나누고 백엔드에서 JSON을 보내고 프론트엔드에서 데이터를 처리하면 훨씬 빠르고 쉬울 것 같은데 템플릿 작업에 신경을 쓰다 보니 많은 불필요한 시간과 노력을 투자하게 되었습니다. 프론트엔드와 백엔드를 분리하여 작업하거나 각 분야의 전문가와 협력하는 것이 더 효율적일 것이라는 것을 느꼈습니다.

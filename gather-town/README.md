> '지금 게더에 몇 명 있어요?'   
> 진짜 게더에 서식하는 유령을 만들어보자


### idea building
1. `모.각.코.(모여서 각자 코딩)` 성격이 강한 우리 외대 멋사의 gather는 접속 중인 사람이 많을수록 재미있다.
2. [Gather Home](https://app.gather.town/app) 에 갈 때 접속자 수가 0이면 슬프다.
    | 주말에도 활발한 멋사 | 초반에만 반짝 사용한 동창 게더 |
    | :-: | :-: |
    | ![gather-ghost](https://user-images.githubusercontent.com/60145951/160228700-def9ad6a-3d4c-4b47-ac25-ff650a8c5f9a.png) | ![no-one](https://user-images.githubusercontent.com/60145951/160228706-6e2f804a-0d83-4258-a686-1b8ba8314b56.png) |
3. 방학에 쫌쫌따리 만들어 본 맛집 추천 봇이 웹 크롤링 결과를 응답으로 뱉는 봇이었다. `==` API를 제공하는지 어떤진 모르겠지만 정 안되면 접속자 수만 긁어와도 상관 없다는 판단이 섰다. 물론 더 나은 방법이 있다면 그걸 사용해야지...

### Goal `==` 하고 싶은 것
> Gather를 잘 사용하기
1. [welcome-kit](https://github.com/hufslion10th/welcome_kit) 배부가 지연되었던 원인인 <font color=grey>반응형 웹 구현,</font> 배포를 자동화 할 방법을 찾고 도입하자.
    - 웹 페이지 구현이 아니니 반응형까지 신경 쓸 필요는 없다
2. heroku와의 악연을 청산하자
    - 뭐 때문에 그렇게 안됐나...
3. 이 참에 [gather의 api](https://support.gather.town/help/gather-api)를 확인해보자.


### TODO
- [ ] [Gather API](https://support.gather.town/help/gather-api) 탐색 후 logic 설계
- [ ] 배포 자동화
- [ ] 기본 틀이 되는 slack bot 생성
- [ ] 때가 되면 생길 것이다.
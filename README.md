## Django channels (chat app)

### 참조
* https://channels.readthedocs.io/en/latest/tutorial/part_1.html
* https://a-littlecoding.tistory.com/27

### TODOS
1. Django Channels를 사용하여 웹소켓(WebSocket) 프로토콜을 이용해 양방향 통신을 구현할 수 있다.
2. Figma와 같은 그림 작업 시스템을 만들어보기 위해서는 클라이언트와 서버 간의 양방향 통신이 필요하다.
3. 이를 위해 Django Channels를 이용하여 채팅방(chat room)을 만들어, 클라이언트 간 실시간 채팅 기능을 구현해보았다.
4. 이제는 이를 발전시켜, 클라이언트가 그림을 그릴 때마다 서버에 전송하여 실시간으로 작업이 저장되도록 구현해야 한다.
5. 이를 위해 클라이언트에서 발생한 그림 정보를 WebSocket을 통해 서버로 전송하고, 서버에서는 이 정보를 데이터베이스에 저장한다.
6. 이후에는 저장된 그림 정보를 불러와서 다른 클라이언트에게 전송하고, 이를 이용하여 모든 클라이언트가 실시간으로 그림 작업을 공유할 수 있도록 구현해야 한다.

### 전체 프로세스
1.Django Channels 설치
  * asgi.py 생성 및 설정
  * settings.py 설정 변경
  * routing.py 생성 및 설정

2.모델 생성
  * 방(Room) 모델 생성
  * 메시지(Message) 모델 생성

3.뷰(View) 생성
  * 뷰(View) 생성
  * 방 입장 뷰
  * 방 나가기 뷰

4.템플릿(Template) 생성
  * 방 목록 템플릿
  * 방 입장 템플릿 

5.프론트엔드(Front-end) 구현
  * 채팅 및 그림 그리기 UI 구현
  * WebSocket으로 데이터 전송

6.컨슈머(Consumer) 생성
  * WebSocket에서 데이터 수신
  * 받은 데이터 처리 및 전송
  * Redis와 PostgreSQL을 이용한 데이터 저장 및 불러오기

7.ASGI 서버 띄우기
  * Daphne 이용


지금 models, testconsumers, views 는 임시
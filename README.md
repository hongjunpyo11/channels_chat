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
# Algorithm_Trading_Bot
Upbit 거래소의 [openAPI](https://docs.upbit.com/)를 활용한 암호화폐 트레이딩 봇


## 첫번째 계획
1. Upbit 거래소의 프로젝트 공시 게시판 크롤링 -> 1분 간격으로 신규 공시 내역을 확인
2. 신규 공시 내역의 키워드(코인명, 기공개 여부 등)을 확인하여 사용자에게 알림
3. 사용자가 투자 금액 등을 입력하여 승인 한 경우 해당 코인 감시를 시작
4. 적정가격으로 매수한 후, 매수한 갯수의 20% 씩 구매가의 +10% 간격으로 매도 주문
5. 마지막 매도 체결을 기준으로 15분간 체결되지 않으면 매도 금액을 변경
6. 공시 시점으로부터 3시간이 지나면 전량 매도
- 위 수치들은 임시로 결정된 값이며, 추후 데이터 분석을 바탕으로 변경될 예정


## 참고
- Upbit openAPI의 경우 jwt가 아닌 pyjwt를 사용함
- pyjwt 2.0.0 이상 버전의 경우 jwt.encode() 메소드의 반환값이 byteString -> String으로 [변경](https://github.com/vimalloc/flask-jwt-extended/issues/386)되었음
  이에 encode 된 값을 decode 할 필요없음

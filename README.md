# Algorithm_Trading_Bot
Upbit 거래소의 [openAPI](https://docs.upbit.com/)를 활용한 암호화폐 트레이딩 봇


## 참고
- Upbit openAPI의 경우 jwt가 아닌 pyjwt를 사용함
- pyjwt 2.0.0 이상 버전의 경우 jwt.encode() 메소드의 반환값이 byteString -> String으로 [변경](https://github.com/vimalloc/flask-jwt-extended/issues/386)되었음 이에 encode 된 값을 decode 할 필요없음 (레퍼런스 페이지 수정 요청 -> 반영됨)

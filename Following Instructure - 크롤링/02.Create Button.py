# 버튼 생성
btn =  Button(win)

# 버튼 크기
btn.config(width = 20, height = 20)

# 버튼 내용
btn.config(text = "버튼")

# 버튼 기능
btn.config(command = alert)
def alert():
    print("버튼이 눌림")

# 버튼 배치
btn.pack()

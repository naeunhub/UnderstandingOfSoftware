mymemo = []
myfile = input('저장할 파일 이름을 입력해주세요 : ')
f = open(myfile, 'w')

while True :
    print("국어와 영어 점수를 입력해주세요","\n","예) 90 85")
    score = input()
    if len(score) == 0 :
        break
    mymemo.append(score)

for item in mymemo :
    msg = score + '\n'
    f.write(msg)
f.close()
print("score.txt 저장 완료")

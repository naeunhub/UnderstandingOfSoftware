#항목을 입력받아 리스트에 저장하고 파일에 출력하는 프로그램

mymemo = []
myfile = input('파일명을 입력하세요 : ')
f = open(myfile, 'w')

while True :
    print("점수를 입력해 주세요. 끝내시려면 엔터키를 두 번 눌러주세요.")
    item = input()
    if len(item) == 0 :
        break
    mymemo.append(item)

for item in mymemo :
    msg = item + '\n'
    f.write(msg)
f.close()
print("score.txt 저장 완료")

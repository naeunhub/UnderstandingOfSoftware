#텍스트 파일을 읽어서 각 문장을 출력하는 프로그램

mymemo = []
myfile = input('불러올 파일 이름을 입력하세요 : ')
ave = 0
maxscore = 0
f = open(myfile)
while True :
    line = f.readline()
    if len(line) == 0 :
        break
    line = line.strip()
    mymemo.append(line)
f.close()

for item in mymemo :
    ave = ave + int(item)

    if maxscore < int(item) :
        maxscore = int(item)
        
    print(item)
    
ave = ave / len(mymemo)

print("-------------------------")
print("평균 : "+ str(ave))
print("최고점 : "+ str(maxscore))

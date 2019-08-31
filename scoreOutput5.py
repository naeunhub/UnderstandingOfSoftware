mymemo = []
myfile = input('불러올 파일 이름을 입력하세요. : ')

aline = 0
bline = 0
cnt = 0
with open(myfile) as data :
    lines = data.readlines()

    for line in lines :
        nline = line.split()
        aline = aline + float(nline[0])
        bline = bline + float(nline[1])
        cnt = cnt + 1

kave = aline/cnt
eave = bline/cnt
tave = aline + bline
taves = cnt*2
tave = tave/taves
print("국어 평균 : {0:.2f}".format(kave))
print("영어 평균 : {0:.2f}".format(eave))
print("총 평균 : {0:.2f}".format(tave))



#페이징에 필요한 정보를 만들어서 가져가야 한다 

import math #수학 라이브러리  

def getPaging(pageNum, totalCnt):
    #pageNum - 현재페이지정보 
    #totalCnt - 전체 데이터 개수(페이징 개수를 찾아내자)
    
    pageGroupSize=10 #한번에 10페이지씩 출력 

    #전체 데이터 개수 - 353 개 
    #353/10  = 35.3 
    #ceil - 올림, floor - 내림 
    pnTotal = math.ceil(totalCnt/pageGroupSize)

    #그룹 1~10, 11~20, 21~30 ....
    #pageNum = 5    1~10
    #pageNum = 17   11~20
    #pageNum = 22   21~30

    groupStart = int((pageNum-1)/pageGroupSize) * pageGroupSize + 1
    groupEnd = groupStart+pageGroupSize
    if groupEnd>pnTotal:
        groupEnd=pnTotal+1 
    
    return {"pageNum":pageNum, 
             "pnStart":int(groupStart), 
             "pnEnd":int(groupEnd), 
             "pnTotal":pnTotal}

import datetime
 

def getFilename(filename):
    #확장자가져오기
    pos = filename.rfind(".")
    ext = filename[pos+1:]
    #print(ext)
    now =  datetime.datetime.now()
    filename = now.strftime('%Y%m%d%H%M%S%f')+"."+ext 
    return filename 

if __name__ =="__main__":
    print( getFilename("test.txt") )


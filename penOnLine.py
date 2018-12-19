mport cv2
import numpy as np 
import matplotlib.pyplot as plt
import pygame
import time
from aip import AipOcr
from aip import AipSpeech
from PIL import Image
#需要的库

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) == 32:
        cv2.imwrite("kk.png",frame)
#摄像头截取图片

        kkk=Image.open("kk.png")
        kkk=kkk.convert("L")
#转换为灰度图片

        threshold = 160
        table = []
        for i in range(256):
            if i <threshold:
                table.append(0)
            else:
                table.append(1)
        kkkk=kkk.point(table,"1")
        kkkk.save("kkkk.png")
#转换为黑白图片

        APP_ID = '15155701'
        API_KEY = 'tpiAH59yHC2SF736GMdhB19D'
        SECRET_KEY = 'txZOB0dmY5GePp8oFNtoRKATaeaLdHCE'
       
        Aipocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
     
        filePath = "kkkk.png"
 
        def get_file_content(filePath):
           with open(filePath, 'rb') as fp:
              return fp.read()
 
       
        options = {
          'detect_direction': 'true',
             'language_type': 'CHN_ENG',
        }
 

        result = Aipocr.basicGeneral(get_file_content(filePath), options)
        words_result=result['words_result']
        for i in range(len(words_result)):
           penWords=words_result[i]['words']
           print(penWords)           
#转换为文字信息
    
           client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
           result  = client.synthesis( penWords, 'zh', 1, {
             'vol': 5,'per':4
                 })
 
 
           if not isinstance(result, dict):
              with open('auido.mp3', 'wb') as f:
                f.write(result)
#合成语音文件

           file=r'auido.mp3'
           pygame.mixer.init()
           track = pygame.mixer.music.load(file)
           pygame.mixer.music.play()
           time.sleep(10)
           pygame.mixer.music.stop()
#播放语音文件 
        
    if cv2.waitKey(1) == 27:break
        
cap.release() 
cv2.destroyAllWindows()

#关闭程序释放窗口

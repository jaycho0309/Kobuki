# Kobuki - Human Following Robot


YOLOv3를 사용하여 객체 인식  
장애물을 피해 사람을 따라다니는 알고리즘 개발


----------------------
# 프로젝트 구조
- camera.py : camera 정보를 cv_bridge로 ros에 전달
- detect.py : YOLO-332로 객체 인식
- rgb_sub.py : camera 정보 중 rgb 값을 subscribe
- depth_sub.py : camera 정보 중 depth 값을 subscribe
- think.py : 받은 정보를 바탕으로 주행하는 알고리즘
- sense.py : 현재 로봇의 위치 및 이동 정보 저장
- act.py : 로봇의 행동 제어

# YOLOv3 
![그림1](https://user-images.githubusercontent.com/80737266/124345892-a163de00-dc16-11eb-9cf2-0494b272d706.png)  
기존 DarkNet53의 빨간색 부분인 Residual Block의 반복횟수를 (1,2,8,8,4) -> (1,2,3,3,2)로 줄임  


![그림2](https://user-images.githubusercontent.com/80737266/124345996-37980400-dc17-11eb-97a5-0c6641f46b04.png)  
주행 환경과 로봇 시야에 맞는 영상을 직접 촬영하여 데이터 학습

----------------------
# Driving Algorithm
## Schematic of Kobuki Zones  
![캡처](https://user-images.githubusercontent.com/80737266/124346735-7039dc80-dc1b-11eb-968a-284d0c7ff25c.PNG)
## Flow Chart of Kobuki
![캡처1](https://user-images.githubusercontent.com/80737266/124346736-7039dc80-dc1b-11eb-8530-8b2a1083cf1a.PNG)
# Experiments
## Experiment 0
![캡처4](https://user-images.githubusercontent.com/80737266/124346739-716b0980-dc1b-11eb-8808-9c71c91ad3b2.PNG)

## Experiment 1
![캡처2](https://user-images.githubusercontent.com/80737266/124346737-70d27300-dc1b-11eb-9d40-c606f8f168bc.PNG)  
![캡처5](https://user-images.githubusercontent.com/80737266/124346740-7203a000-dc1b-11eb-8001-56580dd9765c.PNG)   
![캡처6](https://user-images.githubusercontent.com/80737266/124346741-7203a000-dc1b-11eb-9d27-a1d9c2557e3c.PNG)  
## Experiment 2
![캡처3](https://user-images.githubusercontent.com/80737266/124346738-70d27300-dc1b-11eb-9070-582e34dc6e33.PNG)  
![캡처7](https://user-images.githubusercontent.com/80737266/124346742-729c3680-dc1b-11eb-9828-8622aa72218a.PNG)  
![캡처8](https://user-images.githubusercontent.com/80737266/124346743-7334cd00-dc1b-11eb-8f84-725a7136bca0.PNG)

# Future Works
![캡처10](https://user-images.githubusercontent.com/80737266/124346747-792aae00-dc1b-11eb-87a1-93f7f0a2b12a.PNG)


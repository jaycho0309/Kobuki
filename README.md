# Kobuki - Human Following Robot


YOLOv3를 사용하여 객체 인식, 경량화로 속도 향상  
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
------------------------
# YOLOv3 
![그림1](https://user-images.githubusercontent.com/80737266/124345892-a163de00-dc16-11eb-9cf2-0494b272d706.png)  
기존 DarkNet53의 빨간색 부분인 Residual Block의 반복횟수를 (1,2,8,8,4) -> (1,2,3,3,2)로 줄임 [YOLO332]  


![그림2](https://user-images.githubusercontent.com/80737266/124345996-37980400-dc17-11eb-97a5-0c6641f46b04.png)  
주행 환경과 로봇 시야에 맞는 영상을 직접 촬영하여 데이터 학습

----------------------
# Driving Algorithm
## Schematic of Kobuki Zones  
![캡처](https://user-images.githubusercontent.com/80737266/124346735-7039dc80-dc1b-11eb-968a-284d0c7ff25c.PNG)  
Turnzone : 장애물을 인식하여 회피 명령  
Yellowzone : 장애물 충돌 방지  
Redzone : 정지 명령  
- kobuki의 지름이 약 35cm 이므로 50cm를 충돌 범위로 설정
- Redzone 앞에서 최저속도 0.2m/s, 0.04m/s로 감속하므로 충돌하지 않고 멈추기 위해 1m를 안전거리로 설정
- 회전 시 직선방향 0.2m/s, 각속도 0.4rad/s. 최악의 상황인 90도 회전을 위해 4초 필요, Trunzone을 1.5m로 설정
- 1.5m 까지의 거리는 회전 시 충돌 우려가 있어 Yellowzone으로 설정, 장애물이 있다면 직진 강제

## Flow Chart of Kobuki
![캡처1](https://user-images.githubusercontent.com/80737266/124346736-7039dc80-dc1b-11eb-8530-8b2a1083cf1a.PNG)

# Experiments
## Experiment 0
![캡처4](https://user-images.githubusercontent.com/80737266/124346739-716b0980-dc1b-11eb-8808-9c71c91ad3b2.PNG)
- YOLO332는 Darknet에 비해 70%의 parameter를 가짐 -> 33% 속도 향상
- mean AP는 4.6%p 하락, Person에 대한 AP는 3.2%p 하락 (Trade-off)
- 실험환경은 laptop이고 배터리에 영향을 많이 받아 전원이 50% 이하일 때 fps가 절반으로 하락하는 현상 확인

## Experiment 1
### 실험 환경
![캡처2](https://user-images.githubusercontent.com/80737266/124346737-70d27300-dc1b-11eb-9d40-c606f8f168bc.PNG)  
### 주행
![캡처5](https://user-images.githubusercontent.com/80737266/124346740-7203a000-dc1b-11eb-8001-56580dd9765c.PNG)   
- Kobuki의 위치를 1초마다 기록. 사람은 검정색 박스를 따라 이동하며 로봇의 이동경로는 각 색깔로 표시
### 결과
![캡처6](https://user-images.githubusercontent.com/80737266/124346741-7203a000-dc1b-11eb-9d27-a1d9c2557e3c.PNG)  
- 5번의 실험 모두 사람을 따라가는데 성공
- 평군 0.37m/s로 주행, 6%의 비율로 Target 감지 실패
- fps : 1.8 ~ 3.6

## Experiment 2
### 실험 환경
![캡처3](https://user-images.githubusercontent.com/80737266/124346738-70d27300-dc1b-11eb-9070-582e34dc6e33.PNG)  
### 주행
![캡처7](https://user-images.githubusercontent.com/80737266/124346742-729c3680-dc1b-11eb-9828-8622aa72218a.PNG)  
- 로봇은 원점에서 출발, Target은 (6,0)에 고정, 검정 박스는 장애물
- 밝은 청색(Trial 1)과 노란 경로(Trial 4)는 실패 사례
- Trial 1 : 장애물을 사람으로 잘못 인식  Trial 4 : 장애물을 뒤늦게 인식하여 충돌
### 결과
![캡처8](https://user-images.githubusercontent.com/80737266/124346743-7334cd00-dc1b-11eb-8f84-725a7136bca0.PNG)
- 성공한 사례에선 평군 11.75m 이동, 평균속도 0.3722m/s
- Lost track target 비율은 exp1에 비해 높음 -> 장애물 회피를 위해 회전하며 target이 시야에서 벗어나고 흔들리기 때문

# Future Works
![캡처10](https://user-images.githubusercontent.com/80737266/124346747-792aae00-dc1b-11eb-87a1-93f7f0a2b12a.PNG)
- Turn 이후 새로운 Person이 화면에 잡히면 Target이 변경되는 문제 
  - Target의 상의 등 RGB값을 저장하여 해결 시도
    - Object Box에서 정확한 위치 파악 문제, 빛에 따른 RGB 값 변화 문제
    - 우연힌 같은 옷을 입은 사람이 있다면 여전히 Target을 잃음
- 실험 2에서 확인한 객체인식 오류
  - YOLO332의 고도화
    - Data 증가, laptop 성능 향상

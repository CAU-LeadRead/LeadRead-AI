# Catchinichi-AI# A.I

# 개발환경

### Label Recognition & Recommendation

```
# pip install -r requirements.txt

# base ----------------------------------------
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow
PyYAML>=5.3.1
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
pymysql
google-cloud-vision
pandas
argparse

# logging -------------------------------------
tensorboard>=2.4.1
# wandb

# plotting ------------------------------------
seaborn>=0.11.0
pandas

# export --------------------------------------
# coremltools>=4.1
# onnx>=1.8.1
# scikit-learn==0.19.2  # for coreml quantization

# extras --------------------------------------
thop  # FLOPS computatio
pycocotools>=2.0  # COCO mAP
```

### Data

labelImg

Selenium

## 개발 배경

사용자가 향수의 정보를 찾아볼 때에 어려움을 덜어주고자 향수 라벨의 사진을 이용한 검색 기능을 구현하였다. 또한, 사용자들이 단일 제품을 검색하는 경우도 있을테지만 매장에 디스플레이 되어있는 여러 제품을 한번에 검색해볼 경우도 고려하여 여러개의 향수를 동시에 인식하는 기능을 구현하였다.

니치 향수라는 소수를 위한 향수를 주제로 하는 만큼 보편적인 추천 알고리즘이 아닌 사용자 개개인에게 추천하는 알고리즘이 더욱 적합할 것이라고 판단하여 구현하였습니다.

# 개발 사항

- 향수 데이터 크롤러
- 향수 DB로의 입력 및 출력
- 개인별 추천 알고리즘
- 추천 향수 DB 자동 업데이트
- 다중 라벨 인식 모듈

## 구현 사항

### 데이터 수집

- 설문조사
    - 프로그램의 완성도에 있어 독자적인 데이터를 사용하는 것이 중요할 것이라 판단하여 설문조사를 통한 향수에 대한 사용자 평가 수집
- 크롤링
    - 크롤링을 통하여 학습을 위한 데이터와 향수 노트 데이터 수집

### 전처리

- 번역
    - 수집한 데이터의 한글화
    - 수집한 설문조사 데이터의 영문/라틴 번역
- 이미지 라벨링
    - *LabelImg*를 활용하여 이미지 box 생성 및 라벨링
- 이미지 augmentation
    - tilt, shift, resizing을 통해 데이터 증축

### 개별추천 알고리즘

- 데이터 수집
    - 회원가입시 사용자의 취향을 파악할 수 있는 향들에 대한 리뷰를 받는다.
    - 사용자가 향수에 대한 리뷰를 남길시 해당 데이터를 수집한다.
- 모델 학습
    - Matrix Factorization을 활용하여 학습을 진행한다.
    - 과적합을 방지하는 regularization term과 bias 추가
- 결과
    - 예측값 중 니치 향수 추출
    - 예측값 정렬 및 상위 5개 데이터를 다음과 같은 포맷으로 추출:

        ```json
        {"detected": [{"brand":<brand1>, "en_name":<en_name1>}, {"brand":<brand2>, "en_name":<en_name2>}]}
        ```

    - 예측값을 데이터베이스에 저장

### 유사한 향수 추천 알고리즘

- 데이터 수집
    - 사용자의 리뷰를 기반으로 평점 데이터 수집
- 데이터 전처리
    - 각 향수별 데이터의 평준화
- 유사도 확인
    - 각 향수별 Cosine 유사도 검사
    - 각 향수들 사이의 상관관계를 표현하는 매트릭스를 데이터베이스에 저장
    - 니치향수 추출하여 출력

    ```json
    {"detected": [{"brand":<brand1>, "en_name":<en_name1>}, {"brand":<brand2>, "en_name":<en_name2>}]}
    ```

### 향수 라벨 인식 모듈

1. OCR을 통한 향수 브랜드 및 이름 추출
    1. Google Vision API를 활용
        1. 높은 영문인식률
        2. 높은 Latin 알파벳 인식률
        3. 높은 필기체 인식률
    2. 향수 브랜드 추출하여 DB의 데이터와 대조하여 향수정보 추출
        1. 브랜드별 다양한 표기방법에 맞춰 예외 케이스 확인 처리
            1. e.g) Maison Margiella 와 Maison Martin Margiella는 동일한 브랜드이다.
        2. 다양한 브랜드가 존재 가능하기 때문에 여러 브랜드 교차 확인
    3. DB의 향수 이름과 교차 검증하여 결과값 저장후 JSON으로 출력

        ```json
        {"detected": [{"brand":<brand1>, "en_name":<en_name1>}, {"brand":<brand2>, "en_name":<en_name2>}]}
        ```

2. 이미지 Classification 모듈
    1. 라벨을 단순히 이름으로 검색하기 어려운 경우
        1. 예시

        ![A%20I%2066e7afc8c4d94632acceb6f4e66d72eb/Untitled.png](A%20I%2066e7afc8c4d94632acceb6f4e66d72eb/Untitled.png)

        딥디크 오 데 썽

    2. YOLOv5를 활용한 이미지 Classification
        1. 각 라벨별 600개의 이미지를 활용하여 학습

            ![A%20I%2066e7afc8c4d94632acceb6f4e66d72eb/results.png](A%20I%2066e7afc8c4d94632acceb6f4e66d72eb/results.png)

    3. 이미지를 ResNet50를 활용하여 학습
        1. Prediction Accuracy : 85%

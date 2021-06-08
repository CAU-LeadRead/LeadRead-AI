# Catchinichi-AI
# 매뉴얼

## 환경설정

### Clone Repository

```bash
git clone https://github.com/Catchi-Nichi/Catchinichi-AI.git
```

### 필요 라이브러리 및 YOLOv5 다운로드

```bash
cd Catchinichi-AI
pip install -r requirements.txt
git clone https://github.com/ultralytics/yolov5.git
```

### 디렉토리 구조

```
Catchinichi-AI
├─.vscode
├─DB_related
├─etc
├─fragrance_Data
├─imgs
├─label_recognition
├─recommender
│  ├─.vscode
│  ├─DataFrames
│  ├─recommender
│  │  └─DataFrames
│  ├─reviews
│  └─__pycache__
├─ResNet50
├─ResNet_dataset
├─ResNet_data_split
│  ├─test
│  ├─train
│  └─val
├─sample_imgs
└─yolov5
```

## 추천 알고리즘

### **자동 업데이트 설정**

recommender디렉토리의 [updateTable.py](http://updatetable.py)를 통하여 DB 업데이트

```bash
crontab -e
```

```
* * * * * python ~/Catchinichi-AI/recommender/updateTable.py
```

### 개별 추천 알고리즘 실행

```bash
python ~/Catchinihi-AI/recommender/user_based.py <user_id>
```

### 유사 향수 알고리즘 실행

```bash
python  ~/Catchinihi-AI/recommender/user_based.py <brand> <product>
```

## 사진을 통한 향수 검색

GOOGLE_VISION_CRED에 Google Vision 의 Credential 주소 지정

### 사진 검색 실행

```bash
python ~/Catchinihi-AI/label_recognition/label_cls.py <image path>
```

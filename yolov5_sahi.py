#%% Kütüphanelerin Yükle

import numpy as np
from sahi.model import Yolov5DetectionModel
from sahi.utils.cv import read_image
from sahi.predict import get_prediction, get_sliced_prediction, predict

#%% Tüm Resimleri Test Et

Yolov5DetectionModel(
   model_path="models/best.pt",
   confidence_threshold=0.5,
   device="cuda",)

result = predict(
    source = "images/",
    model_type  = "yolov5" ,
    model_path  = "models/best.pt",  
    export_visual = True,
    project = "demo_data/")
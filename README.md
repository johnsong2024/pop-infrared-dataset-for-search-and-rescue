# POP:An infrared dataset for partially occluded person detection in complex environment for search and rescue

---

> This repository contains the necessary python files to help experts and scholars use POP simpler and more efficient.

## Abstract

The combination of unmanned aerial vehicles (UAVs) and deep learning has potential applicability in various complex
search and rescue scenes. However, due to the presence of environmental occlusions such as trees, the performance of
UAVs mounted with different optical payloads in detecting trapped persons is poor. Until now, there are rarely published
datasets specialized for detecting human objects in occluded environments by a UAV. To address this problem, we
collected a UAV-based infrared thermal imaging dataset for outdoor, partially occluded person detection (POP). This
dataset is composed of 7868 labelled thermal images collected from different environmental scenes. After evaluating with
five popular object detection networks, YOLOv8s achieved best detection accuracy and shortest response time. High object
detection accuracy was not attenuated under YOLOv8s until the occlusion rate exceeded 70%. In addition, we used POP to
verify the possibility of performing a preliminary injury classification task in partially occluded environments. We
expected POP would extend present modalities for the search and rescue under complex occluded circumstances.

---

## POP:infrared thermal dataset for partially occluded person detection

The POP dataset includes a total of 7868 images (5548 that can be used for model training and 2320 for model validation)
collected at many different outdoor scenarioesand annotations in the form of 23971 label boxes.It is collected by drones
at different flying heights(30 m, 50 m, and 70 m), weather(cloudy, overcast, foggy and sunny), scenes(Cedar, Pagoda
tree, Sweetgum tree, Privet and so on) and other different experimental sites.

---

## Dataset structure

The purpose of the original dataset structure is to improve the readability of the dataset. All images are stored in JPG
format and divided into a training set and validation set according to the characteristics of the scene. Each image uses
the same naming format: <scene_ID>_<image_ID>_<height>.JPG.

<scene_ID> represents the sequence ID of the shooting site, <image_ID> represents the ID number of the image (starting
from 0000 for each scene to improve readability and facilitate data management), and <height> indicates the height at
which the image was captured relative to the take-off point.

---

## Download and use POP dataset

If you want to explore or use the POP dataset, you can download and use it as follows:

1. Download the <kbd>ZIP</kbd> dataset from current repository:
   [github](https://github.com/johnsong2024/pop-infrared-dataset-for-search-and-rescue)

or run the following command at <kbd>cmd</kbd>:

```
git clone https://github.com/johnsong2024/pop-infrared-dataset-for-search-and-rescue.git
```

then, you can get the POP dataset in the [POP](POP) directory.

2. (optional) Convert the dataset format to the format you need.POP dataset provides experts and scholars with
   annotation information in [COCO](POP) format. If you need VOC format or yolo format, we provide you with [conversion
   tools](src).Please refer to <kbd>Source code</kbd> for specific usage methods.

---

## Source code 


The code is written in Python and includes an algorithm for converting the labelled boxes from the COCO format to the
VOC format or YOLO format, providing support for subsequent object detection network training.

### convert coco to voc

[coco2voc](src/coco2voc.py) tools provides a conversion method from coco to voc.In order to use this tool correctly, you
need to replace the following two parameters with the path of your specified folder:

```
coco_annotation_file = r'/path/to/your/coco/file'  # Replace it with your COCO annotation file path
output_directory = r'/path/to/your/voc/dictory'  # Replace it with the path where you want to store the VOC annotations
```

After that, you can get the converted result in <kbd>output_directory</kbd> by running the following command.

```
python coco2voc.py
```

### convert coco to yolo

[coco2yolo](src/coco2yolo.py) tools provides a conversion method from coco to yolo.In order to use this tool correctly,
you need to replace the following two parameters with the path of your specified folder:

```
json_path = r'/path/to/your/coco/file'  # Replace it with your COCO annotation file path
save_path = r'/path/to/your/yolo/dictory'  # Replace it with the path where you want to store the yolo annotations
```

After that, you can get the converted result in <kbd>save_path</kbd> by running the following command.

```
python coco2yolo.py
```

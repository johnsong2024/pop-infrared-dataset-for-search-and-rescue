import json
import os
from xml.etree.ElementTree import Element, SubElement, tostring


def coco_to_voc(coco_ann_file, output_dir):
    with open(coco_ann_file, 'r') as f:
        coco_data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_info in coco_data['images']:
        image_id = image_info['id']
        file_name = image_info['file_name']
        width = image_info['width']
        height = image_info['height']

        annotations = [ann for ann in coco_data['annotations'] if ann['image_id'] == image_id]
        root = Element('annotation')

        SubElement(root, 'filename').text = file_name
        size_elem = SubElement(root, 'size')
        SubElement(size_elem, 'width').text = str(width)
        SubElement(size_elem, 'height').text = str(height)
        SubElement(size_elem, 'depth').text = '3'

        for ann in annotations:
            obj = SubElement(root, 'object')
            SubElement(obj, 'name').text = coco_data['categories'][ann['category_id'] - 1]['name']
            bbox = ann['bbox']
            bndbox = SubElement(obj, 'bndbox')
            SubElement(bndbox, 'xmin').text = str(int(bbox[0]))
            SubElement(bndbox, 'ymin').text = str(int(bbox[1]))
            SubElement(bndbox, 'xmax').text = str(int(bbox[0] + bbox[2]))
            SubElement(bndbox, 'ymax').text = str(int(bbox[1] + bbox[3]))

        xml_str = tostring(root, encoding='unicode')
        xml_file_path = os.path.join(output_dir, f'{os.path.splitext(file_name)[0]}.xml')
        with open(xml_file_path, 'w', encoding='utf-8') as f:
            f.write(xml_str)

        print(f'Converted {file_name} to {xml_file_path}')


coco_annotation_file = r'path/to/your/coco/file'
output_directory = r'path/to/your/voc/dictory'
coco_to_voc(coco_annotation_file, output_directory)

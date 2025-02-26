"""

NAME : ui_test

USER : admin

DATE : 18/9/2024

PROJECT_NAME : sapic-master

CSDN : friklogff
"""
import os

import oss2

import gradio as gr
import cv2


def save_image(input_image):
    temp_img_path = "temp_img.jpg"
    file_name = os.path.basename(input_image.name)
    # print(file_name)
    image = cv2.imread(input_image.name)
    # 保存到临时文件
    cv2.imwrite(temp_img_path, image)
    print("Save processed img to the path :" + file_name)
    return temp_img_path

    # 此处第一个参数 img/100.png 中的img是阿里云的Bucket中事先创建好的img文件夹，第二个参数100.png是本地的图片100.png


with gr.Blocks() as demo:
    with gr.Tab('dadsad'):
        # gr.Interface(fn=save_image, inputs=input_image, outputs="text")
        image_input = gr.File(label="Image")
        image_output = gr.Text()
        image_button = gr.Button("提交")
        image_button.click(save_image, inputs=image_input, outputs=image_output)

demo.launch()

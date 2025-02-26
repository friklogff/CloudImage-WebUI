import gradio as gr
import cv2

from src.fz import paste_image_to_typora


def save_image(input_image):
    input_image_rgb = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    cv2.imwrite("img.jpg", input_image_rgb)
    return "Image saved successfully!"

input_image = gr.components.Image()
gr.Interface(fn=save_image, inputs=input_image, outputs="text").launch()

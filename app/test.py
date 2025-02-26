"""

NAME : test

USER : admin

DATE : 27/12/2024

PROJECT_NAME : oss

CSDN : friklogff
"""
import gradio as gr
import oss2

import json
import os
import oss2
import gradio as gr
import cv2


class AliyunOss(object):

    def __init__(self):

        with open('config.json', 'r') as f:
            config = json.load(f)

        self.access_key_id = config['access_key_id']
        self.access_key_secret = config['access_key_secret']
        self.auth = oss2.Auth(self.access_key_id, self.access_key_secret)
        self.bucket_name = config['bucket_name']
        self.endpoint = config['endpoint']
        self.bucket = oss2.Bucket(self.auth, self.endpoint, self.bucket_name)
    def put_object_from_file(self, name, file):
        """

        :param name: 在阿里云Bucket中要保存的文件名
        :param file: 本地图片的文件名
        :return:
        """
        self.bucket.put_object_from_file(name, file)
        return "https://{}.{}/{}".format(self.bucket_name, self.endpoint, name)



def save_image(input_image):
    temp_img_path = "temp_img.jpg"

    file_name = os.path.basename(input_image.name).replace(" ", "")
    # print(file_name)
    image = cv2.imread(input_image.name)
    # 保存到临时文件
    cv2.imwrite(temp_img_path, image)
    print("Save processed img to the path :" + file_name)
    img_url = AliyunOss().put_object_from_file(f"uploads/{file_name}", temp_img_path)

    return img_url






# 你的generate_and_save_html函数
def ide():
    # 阿里云配置信息
    access_key_id = AliyunOss().access_key_id
    access_key_secret = AliyunOss().access_key_secret
    bucket_name = "ygcc-gxx"
    endpoint = "oss-cn-beijing.aliyuncs.com"

    # Initialize authentication information and Bucket object
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    # Store image URLs in a list
    image_urls = []

    # List objects in the bucket and get image URLs
    for obj in oss2.ObjectIterator(bucket):
        if obj.key.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            object_url = f"https://{bucket_name}.{endpoint}/{obj.key}"
            image_urls.append(object_url)

    html_start = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CSS 3D Coverflow</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css"> 
  <link rel="stylesheet" href="./style.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prefixfree/1.0.7/prefixfree.min.js"></script>  
</head>
<body>
<div class="main-container">
  <div class="coverflow-container">
    <ol class="coverflow-list">
"""

    # Dynamically add image URLs to HTML content
    html_images = ""
    for i, url in enumerate(image_urls, start=1):
        html_images += f"""
      <input type="radio" name="cover-item" id="cover-{i}">
      <li class="coverflow-item">
        <label for="cover-{i}">
          <figure class="album-cover">
            <img src="{url}">
            <figcaption class="album-name">Album {i}</figcaption>
          </figure>
        </label>
      </li>
"""

    html_controls = """
    </ol>
  </div>
  <div class="controls">
"""

    # Dynamically add control labels to HTML content
    html_control_labels = ""
    for i in range(1, len(image_urls) + 1):
        html_control_labels += f"<label for='cover-{i}'>{i}</label>"

    html_end = """
  </div>
</div>
</body>
</html>
"""

    html_content = html_start + html_images + html_controls + html_control_labels + html_end

    # Save the generated HTML content to index.html file
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(html_content)
    return html_content


# 使用gr.Blocks创建Gradio应用
with gr.Blocks(css='style.css') as demo:
    with gr.Tab('上传'):
        image_input = gr.File(label="Image")
        image_output = gr.Text()
        image_button = gr.Button("提交")
        image_button.click(save_image, inputs=image_input, outputs=image_output)
    with gr.Tab('图床'):
        encode_button = gr.Button("Encode")
        encode_output = gr.HTML()  # 初始化一个空的HTML组件
        # 当按钮被点击时，调用ide函数，并更新encode_output组件
        encode_button.click(ide, outputs=encode_output)

demo.launch(share=True)

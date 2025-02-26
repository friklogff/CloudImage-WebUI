"""

NAME : app

USER : admin

DATE : 18/9/2024

PROJECT_NAME : oss

CSDN : friklogff
"""
"""

NAME : dft

USER : admin

DATE : 18/9/2024

PROJECT_NAME : sapic-master

CSDN : friklogff
"""
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

def ide():
    # 阿里云配置信息
    access_key_id = AliyunOss().access_key_id
    access_key_secret = AliyunOss().access_key_secret
    bucket_name = "ygcc-gxx"
    endpoint = "oss-cn-beijing.aliyuncs.com"

    # 初始化认证信息和Bucket对象
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    # 存储对象链接的Markdown格式列表
    md_object_urls = []

    # 列举存储桶中的对象并获取完整链接
    for obj in oss2.ObjectIterator(bucket):
        object_url = f"https://{bucket_name}.{endpoint}/{obj.key}"
        # 设置图片显示大小为宽度200px，高度自适应
        md_object_urls.append(f"![{obj.key}]({object_url})")

    # 换行合并成一个字符串
    md_string = "\n".join(md_object_urls)

    print(md_string)
    return md_string


with gr.Blocks() as demo:
    with gr.Tab('上传'):
        image_input = gr.File(label="Image")
        image_output = gr.Text()
        image_button = gr.Button("提交")
        image_button.click(save_image, inputs=image_input, outputs=image_output)
    with gr.Tab('图床'):
        encode_button = gr.Button("Encode")
        encode_output = gr.Markdown()
        encode_button.click(ide, outputs=encode_output)

demo.launch(share=True)

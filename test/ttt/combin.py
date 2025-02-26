import gradio as gr
import json


# 读取本地 JSON 文件内容的函数
def get_json_data():
    with open("./data.json", "r") as file:
        return json.load(file)


# 使用 Gradio Blocks 组件创建界面
with gr.Blocks(css='./style.css', js='./script.js') as demo:
    with gr.Tab("Local HTML"):
        gr.HTML(value=open("./index.html", "r").read())
        json_output = gr.JSON()
        load_button = gr.Button("Load JSON")
        load_button.click(get_json_data, outputs=json_output)

# 启动应用
demo.launch()

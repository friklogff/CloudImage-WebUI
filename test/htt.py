import gradio as gr

# 读取本地 HTML 文件内容
with open("index.html", "r") as file:
    html_content = file.read()

# 使用 Gradio HTML 组件展示 HTML 内容
with gr.Blocks(css='style.css',js='script.js') as demo:
    with gr.Tab("Local HTML"):
        gr.HTML(value=html_content)

# 启动应用
demo.launch()

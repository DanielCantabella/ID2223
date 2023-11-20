import gradio as gr
from PIL import Image
import hopsworks

project = hopsworks.login()
fs = project.get_feature_store()

dataset_api = project.get_dataset_api()

dataset_api.download("Resources/images/latest_wine.png", overwrite=True)
dataset_api.download("Resources/images/actual_wine.png", overwrite=True)
dataset_api.download("Resources/images/df_recent.png", overwrite=True)
dataset_api.download("Models/wine_model/1/confusion_matrix.png", overwrite=True)

with gr.Blocks() as demo:
    with gr.Row():
      with gr.Column():
          gr.Label("Today's Predicted Image")
          input_img = gr.Image("latest_wine.png", elem_id="predicted-img").style(width=256, height=256)
      with gr.Column():
          gr.Label("Today's Actual Image")
          input_img = gr.Image("actual_wine.png", elem_id="actual-img").style(width=256, height=256)
    with gr.Row():
      with gr.Column():
          gr.Label("Recent Prediction History")
          input_img = gr.Image("df_recent.png", elem_id="recent-predictions")
      with gr.Column():
          gr.Label("Confusion Matrix with Historical Prediction Performance")
          input_img = gr.Image("confusion_matrix.png", elem_id="confusion-matrix")

demo.launch()
# demo.launch(share=True)

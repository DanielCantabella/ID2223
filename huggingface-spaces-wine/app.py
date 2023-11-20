import gradio as gr
from PIL import Image
import requests
import hopsworks
import joblib
import pandas as pd

project = hopsworks.login()
fs = project.get_feature_store()


mr = project.get_model_registry()
model = mr.get_model("wine_model", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/wine_model.pkl")
print("Model downloaded")

def wine(alcohol, sulphates, volatile_acidity, total_sulfur_dioxide):
    print("Calling function")
#     df = pd.DataFrame([[sepal_length],[sepal_width],[petal_length],[petal_width]], 
    df = pd.DataFrame([[alcohol, sulphates, volatile_acidity, total_sulfur_dioxide]],
                      columns=["alcohol", "sulphates", "volatile_acidity", "total_sulfur_dioxide"])
    print("Predicting")
    print(df)
    # 'res' is a list of predictions returned as the label.
    res = model.predict(df) 
    # We add '[0]' to the result of the transformed 'res', because 'res' is a list, and we only want 
    # the first element.
#     print("Res: {0}").format(res)
    print(res)
    wine_url = "https://github.com/DanielCantabella/ID2223/blob/main/images/" + res[0] + ".png?raw=true"
    img = Image.open(requests.get(wine_url, stream=True).raw)
    return img
        
demo = gr.Interface(
    fn=wine,
    title="Wine quality Predictive Analytics",
    description="Experiment with sepal/petal lengths/widths to predict which flower it is.",
    allow_flagging="never",
    inputs=[
        gr.inputs.Number(default=9.0, label="alcohol"),
        gr.inputs.Number(default=1.0, label="sulphates"),
        gr.inputs.Number(default=1.4, label="volatile_acidity"),
        gr.inputs.Number(default=220, label="total_sulfur_dioxide"),
        ],
    outputs=gr.Image(type="pil").style(width=256, height=256))

demo.launch(debug=True)


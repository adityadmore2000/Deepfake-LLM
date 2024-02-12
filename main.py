from palm import Palm
from deepfake import Deepfake
import gradio as gr

palm = Palm()
deepfake = Deepfake()

def main(prompt):
    print(f"prompt: {prompt}")
    output = palm.generate(prompt)
    output = deepfake.generate_deepfake(output)
    return output

outputs = gr.Video(label="Output")
demo = gr.Interface(fn=main, inputs="text", outputs=outputs,title = "🤖 Deep LLM")
demo.launch(share=True)   

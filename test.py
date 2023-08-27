import requests
import gradio as gr

# Fetch the audio file
response_0 = requests.get("https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav")
example_audio = response_0.content

# Define the Gradio app and specify the source type as "huggingface"
app = gr.Interface.load("https://cliphamper-openai-whisper-medium.hf.space/", source="huggingface")

# Make a prediction using the Gradio app
result = app.predict([example_audio])

# Print the result
print(result[0])

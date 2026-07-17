!pip -q install google-genai gradio

from google import genai
import gradio as gr

#gemini API key
client = genai.Client(api_key="Gemini_API")
def generate_blog(topic,audience,language,tone,words):
  prompt=f"""
  Write a {words}-word blog.
  Topic :{topic}
  Audience: {audience}
  Language: {language}
  Tone: {tone}

  Include:
  -Introduction
  -History
  -related terms
  -Conclusion
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )

  return response.text

demo=gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Audience"),
        gr.Dropdown(["English","Hindi","telugu","French","Spanish","Urdu"],label="Language"),
        gr.Dropdown(
            ["professional","causal","informal","Technical","Inspirational"],
            label="Tone",
        ),
        gr.Slider(200,1000,value=500,label="Word content")
    ],
    outputs="markdown",
    title="AI Blog Generator (Gemini)"
)
demo.launch(share=True)

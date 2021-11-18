from flask import Flask, app
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import T5ForConditionalGeneration, T5Tokenizer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = T5ForConditionalGeneration.from_pretrained("t5-base")

tokenizer = T5Tokenizer.from_pretrained("t5-base")


def video_id(x):
    try:
        s = [i['text'] for i in YouTubeTranscriptApi.get_transcript(x)]
        s = " ".join(s)
        print(s)
        inputs = tokenizer.encode("summarize: " + s, 
        return_tensors="pt", max_length=1024,truncation=True)
        outputs = model.generate(
        inputs, 
        max_length=150, 
        min_length=40, 
        length_penalty=2.0, 
        num_beams=4, 
        early_stopping=True)
        return tokenizer.decode(outputs[0])
    except:
        return "Summary unavailable"

@app.route('/v/<id>')
def youtubetranscript(id):
    return video_id(id)

if __name__ == "__main__":
    app.run(debug=True)

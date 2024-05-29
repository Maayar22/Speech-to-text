import whisper
from flask import Flask, request
import base64

def decode_base64_to_mp3(base64_string, output_file):
 try:
  # Decode Base64 string
  decoded_data = base64.b64decode(base64_string)

  # Write decoded data to a .mp3 file
  with open(output_file, 'wb') as f:
   f.write(decoded_data)
  print("Decoding successful. MP3 file created:", output_file)
 except Exception as e:
  print("Error:", e)
app = Flask(__name__)

@app.route("/result", methods= ["POST", "GET"])
def result():
   # return {"API":"Respose Positive"}
    output = request.get_json()
    base64_string = output['audioString']
    model = whisper.load_model("medium")
    decode_base64_to_mp3(base64_string, 'audio.mp3')

    result = model.transcribe('audio.mp3', fp16=False)

    SpeechToText = {}
    SpeechToText['Text: ']= result["text"]
    return (SpeechToText)

if __name__ == '__main__':
    app.run(debug= True, port= 200)

# model = whisper.load_model("medium")
# result = model.transcribe("C:/Users/DELL/Downloads/audio (8).mp3", beam_size=5, best_of=5, fp16=False)
# print(result["text"])



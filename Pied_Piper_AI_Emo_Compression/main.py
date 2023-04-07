import wave
import json
from vosk import Model, KaldiRecognizer, SetLogLevel
from transformers import pipeline
from pydub import AudioSegment
import os
import shutil
class Word:


    def __init__(self, dict):


        self.conf = dict["conf"]
        self.end = dict["end"]
        self.start = dict["start"]
        self.word = dict["word"]

    def to_string(self):

        return "{:20} from {:.2f} sec to {:.2f} sec, confidence is {:.2f}%".format(
            self.word, self.start, self.end, self.conf*100)
    
    def start_point(self):

        return self.word
    


def word_list (base_audio_path,model_path):

    audio_filename = base_audio_path

    model = Model(model_path)
    wf = wave.open(audio_filename, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # get the list of JSON dictionaries
    results = []
    # recognize speech using vosk model
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            part_result = json.loads(rec.Result())
            results.append(part_result)
    part_result = json.loads(rec.FinalResult())
    results.append(part_result)

    # convert list of JSON dictionaries to list of 'Word' objects
    list_of_Words = []
    for sentence in results:
        if len(sentence) == 1:
            continue
        for obj in sentence['result']:
            w = Word(obj)  # create custom Word object
            list_of_Words.append(w)  # and add it to list

    wf.close()  # close audiofile

    final=[]

    # # output to the screen
    # for word in list_of_Words:
    #     print(word.to_string())
    
    for word in list_of_Words:
        time = word.start_point()
        final.append(time)

    return final

def clear_output_folder(output_dir):
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)

def piper_compress(base_audio_path, segment_length, model_path,high_bitrate,low_bitrate):
    
    # Create output directory
    output_dir = os.path.join(os.path.dirname(base_audio_path), "output")
    clear_output_folder(output_dir)

    os.makedirs(output_dir, exist_ok=True)

    # Open the base audio file
    base_audio_file = wave.open(base_audio_path, "rb")
    base_audio_params = base_audio_file.getparams()

    # Calculate the number of frames per segment
    frames_per_segment = int(segment_length * base_audio_params.framerate)

    # Split audio into segments
    segments = []
    ans=[]

    for i in range(0, base_audio_params.nframes, frames_per_segment):
        # Read segment frames
        segment_frames = base_audio_file.readframes(frames_per_segment)
        
        # Create new wave object for segment
        segment_path = os.path.join(output_dir, f"segment_{i // frames_per_segment}.wav")
        segment = wave.open(segment_path, "wb")
        segment.setparams(base_audio_params)
        segment.writeframes(segment_frames)
        segment.close()
        
        # Append segment to list
        segments.append(segment_frames)

    
    music_lines=[]
    for i in range(0, base_audio_params.nframes, frames_per_segment):
          file_name = os.path.join(output_dir, f"segment_{i // frames_per_segment}.wav")
          music_lines.append(word_list(file_name,model_path))
          
    list_of_sentences=[]
    for a in music_lines:
        sentence = ' '.join(a)
        list_of_sentences.append(sentence)
        print(a)

    
    count=0

    final_audio = AudioSegment.empty()

    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    for b in list_of_sentences:

        print(b)

        sentiment_pipeline = pipeline("sentiment-analysis",model=model_name)

        print(sentiment_pipeline(b))

        sentiment = sentiment_pipeline(b)[0]['label']

        print(sentiment)

        if sentiment == 'POSITIVE':
            
            wave_file = AudioSegment.from_wav(os.path.join(output_dir, f"segment_{count}.wav"))

            # Set the bitrate and export as mp3
            wave_file.export(os.path.join(output_dir, f"segment_{count}_high.mp3"), format="mp3", bitrate=high_bitrate)

            final_audio += AudioSegment.from_mp3(os.path.join(output_dir, f"segment_{count}_high.mp3"))

        else:
         
            wave_file = AudioSegment.from_wav(os.path.join(output_dir, f"segment_{count}.wav"))

            # Set the bitrate and export as mp3
            wave_file.export(os.path.join(output_dir, f"segment_{count}_low.mp3"), format="mp3", bitrate=low_bitrate)

            final_audio += AudioSegment.from_mp3(os.path.join(output_dir, f"segment_{count}_low.mp3"))



        count=count+1

    final_audio.export(os.path.join(os.path.dirname(base_audio_path), "Pied_Pipered_Output.mp3"), format="mp3")
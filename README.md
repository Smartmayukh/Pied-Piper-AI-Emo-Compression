# Pied-Piper-AI-Emo-Compression

## Emotion based Audio Compression 



I recently found a paper titled as "The Effects of MP3 Compression on Perceived Emotional Characteristics in Musical Instruments" 

https://www.aes.org/tmpFiles/elib/20230406/18523.pdf


This paper examines the impact of MP3 compression on the emotional characteristics by conducting listening tests. The experiment compared compressed and uncompressed samples at different bit rates across ten emotional categories. The results revealed that MP3 compression enhanced negative emotions like Mysterious, Shy, Scary, and Sad while diminishing positive emotions like Happy, Heroic, Romantic, Comic, and Calm. MP3 compression reduced positive emotions and amplified negative emotions such as Mysterious and Scary. 

So I decided to come up with a python code that can change the compression of an audio file based on emotions. 

## Basic Idea behind PPEC

My code defines a function Piper_Compress that takes in a base audio file path, segment length, Vosk model path, and high/low bitrate values as inputs. The function splits the audio file into segments of the given length, converts each segment into text using the Vosk model, performs sentiment analysis on the text using the Hugging Face Transformers library, and compresses each segment into either high or low bitrate mp3 files based on the sentiment analysis result. Finally, all the compressed segments are concatenated into a single output audio file named "Pied_Pipered_Output.mp3".



# Pied-Piper-AI-Emo-Compression

## Emotion based Audio Compression 



<a href="#"><img align="right" src="https://user-images.githubusercontent.com/64318469/230570978-cc1a1427-3ff6-45f9-9545-af2635eb10df.png" width="400 " height="250" /></a>



My code defines a function Piper_Compress that takes in a base audio file path, segment length, Vosk model path, and high/low bitrate values as inputs. The function splits the audio file into segments of the given length, converts each segment into text using the Vosk model, performs sentiment analysis on the text using the Hugging Face Transformers library, and compresses each segment into either high or low bitrate mp3 files based on the sentiment analysis result. Finally, all the compressed segments are concatenated into a single output audio file named "Pied_Pipered_Output.mp3".

I got inspiration of this model from the paper titled as "The Effects of MP3 Compression on Perceived Emotional Characteristics in Musical Instruments" 

https://www.aes.org/tmpFiles/elib/20230406/18523.pdf


This paper examines the impact of MP3 compression on the emotional characteristics by conducting listening tests. The experiment compared compressed and uncompressed samples at different bit rates across ten emotional categories. The results revealed that MP3 compression enhanced negative emotions like Mysterious, Shy, Scary, and Sad while diminishing positive emotions like Happy, Heroic, Romantic, Comic, and Calm. MP3 compression reduced positive emotions and amplified negative emotions such as Mysterious and Scary. 

So I decided to come up with a python module that can change the compression of an audio file based on emotions. 

## Song I have chosen is "Castle on the Hill" -Ed Sheeran

## Below you can see the vosk generated subtitles of the song. I split the audio file into segments of 31 seconds. Note as the training dataset for the vosk model is not a large, so the translation is not too accurate.

<pre>
['when', 'i', 'was', 'six', 'years', 'old', 'and', 'broke', 'my', 'leg', 'i', 'was', 'running', 'from', 'my', 'brother', 'and', 'his', 'friends', 'tasty', 'and', 'sweet', 'perfume', 'mathematics', 'mounting', 'wrote', 'down', 'what', 'was', 'younger', 'then']
['take', 'me', 'back', 'to', 'when', 'haha', 'can', 'you', 'make', 'friends', 'and', 'last', 'two', 'years', 'and', "i've", 'not', 'seen', 'in', 'figs', 'and', 'so', 'on', 'way', 'to', 'go', 'the']
['the', 'the', 'hi', 'fifteen', 'years', 'old', 'smoking', 'a', 'cigarette']
['running', 'from', 'the', 'law', 'to', 'the', 'back', 'fields', 'and', 'getting', 'drunk', 'with', 'my', 'friends', 'my', 'first', 'kiss', 'on', 'friday', 'night', 'reckon', 'that', 'day', 'i', 'was', 'younger', 'then', 'take', 'me', 'back', 'to', 'when', 'we', 'fell', 'can', 'joe', 'we', 'got', 'a', 'cheap', 'spirits', 'drink', 'industry', 'friend'] 
['so', 'how', 'we', 'way', 'to', 'go', 'the', 'the']
['hi', 'one', 'so', 'close']
['works', 'down', 'by', 'the', 'coast', 'one', 'or', 'two', 'kids', 'lives', 'alone', "one's", 'brother', 'with', 'dogs', 'already', 'on', 'second', 'line', "he's", 'just', 'barely', 'getting', 'by', 'these', 'people', 'raise', 'me', 'go', 'as', 'to', 'the']
['country', 'names', 'when', 'we', "didn't", 'know', 'hi']
['the']
</pre>


## Sentiment Analysis using Hugging face "distilbert-base-uncased-finetuned-sst-2-english" model



<pre>
when i was six years old and broke my leg i was running from my brother and his friends tasty and sweet perfume mathematics mounting wrote down what was younger then
[{'label': 'NEGATIVE', 'score': 0.9836982488632202}]
NEGATIVE

take me back to when haha can you make friends and last two years and i've not seen in figs and so on way to go the
[{'label': 'POSITIVE', 'score': 0.9919325709342957}]
POSITIVE

the the hi fifteen years old smoking a cigarette
[{'label': 'NEGATIVE', 'score': 0.979468822479248}]
NEGATIVE

running from the law to the back fields and getting drunk with my friends my first kiss on friday night reckon that day i was younger then take me back to when we fell can joe we got a cheap spirits drink industry friend
[{'label': 'NEGATIVE', 'score': 0.9779858589172363}]
NEGATIVE

so how we way to go the the
[{'label': 'POSITIVE', 'score': 0.9858322143554688}]
POSITIVE

hi one so close
[{'label': 'POSITIVE', 'score': 0.9994691014289856}]
POSITIVE

works down by the coast one or two kids lives alone one's brother with dogs already on second line he's just barely getting by these people raise me go as to the
[{'label': 'NEGATIVE', 'score': 0.9983982443809509}]
NEGATIVE

country names when we didn't know hi
[{'label': 'NEGATIVE', 'score': 0.9887117147445679}]
NEGATIVE

the
[{'label': 'POSITIVE', 'score': 0.9635980725288391}]
POSITIVE
</pre>

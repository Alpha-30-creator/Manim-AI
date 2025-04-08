# API Reference [\#](https://voiceover.manim.community/en/stable/api.html\#api-reference "Permalink to this heading")

This reference manual details modules, functions, and variables included in
Manim Voiceover, describing what they are and what they do. For learning how to use
Manim Voiceover, see [Quickstart](https://voiceover.manim.community/en/stable/quickstart.html).

## Voiceover scene [\#](https://voiceover.manim.community/en/stable/api.html\#module-manim_voiceover "Permalink to this heading")

_class_ VoiceoverScene( _renderer=None_, _camera\_class=<class'manim.camera.camera.Camera'>_, _always\_update\_mobjects=False_, _random\_seed=None_, _skip\_animations=False_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene "Permalink to this definition")

Bases: `Scene`

A scene class that can be used to add voiceover to a scene.

add\_voiceover\_text( _text_, _subcaption=None_, _max\_subcaption\_len=70_, _subcaption\_buff=0.1_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.add_voiceover_text) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.add_voiceover_text "Permalink to this definition")

Adds voiceover to the scene.

Parameters:

- **text** ( _str_) – The text to be spoken.

- **subcaption** ( _Optional_ _\[_ _str_ _\]_ _,_ _optional_) – Alternative subcaption text. If not specified, text is chosen as the subcaption. Defaults to None.

- **max\_subcaption\_len** ( _int_ _,_ _optional_) – Maximum number of characters for a subcaption. Subcaptions that are longer are split into chunks that are smaller than max\_subcaption\_len. Defaults to 70.

- **subcaption\_buff** ( _float_ _,_ _optional_) – The duration between split subcaption chunks in seconds. Defaults to 0.1.


Returns:

The tracker object for the voiceover.

Return type:

[VoiceoverTracker](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverTracker "manim_voiceover.VoiceoverTracker")

add\_wrapped\_subcaption( _subcaption_, _duration_, _subcaption\_buff=0.1_, _max\_subcaption\_len=70_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.add_wrapped_subcaption) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.add_wrapped_subcaption "Permalink to this definition")

Adds a subcaption to the scene. If the subcaption is longer than max\_subcaption\_len, it is split into chunks that are smaller than max\_subcaption\_len.

Parameters:

- **subcaption** ( _str_) – The subcaption text.

- **duration** ( _float_) – The duration of the subcaption in seconds.

- **max\_subcaption\_len** ( _int_ _,_ _optional_) – Maximum number of characters for a subcaption. Subcaptions that are longer are split into chunks that are smaller than max\_subcaption\_len. Defaults to 70.

- **subcaption\_buff** ( _float_ _,_ _optional_) – The duration between split subcaption chunks in seconds. Defaults to 0.1.


Return type:

None

safe\_wait( _duration_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.safe_wait) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.safe_wait "Permalink to this definition")

Waits for a given duration. If the duration is less than one frame, it waits for one frame.

Parameters:

**duration** ( _float_) – The duration to wait for in seconds.

Return type:

None

set\_speech\_service( _speech\_service_, _create\_subcaption=True_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.set_speech_service) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.set_speech_service "Permalink to this definition")

Sets the speech service to be used for the voiceover. This method
should be called before adding any voiceover to the scene.

Parameters:

- **speech\_service** ( [_SpeechService_](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")) – The speech service to be used.

- **create\_subcaption** ( _bool_ _,_ _optional_) – Whether to create subcaptions for the scene. Defaults to True. If config.save\_last\_frame is True, the argument is

- **created.** ( _ignored and no subcaptions will be_) –


Return type:

None

voiceover( _text=None_, _ssml=None_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.voiceover) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.voiceover "Permalink to this definition")

The main function to be used for adding voiceover to a scene.

Parameters:

- **text** ( _str_ _,_ _optional_) – The text to be spoken. Defaults to None.

- **ssml** ( _str_ _,_ _optional_) – The SSML to be spoken. Defaults to None.


Yields:

_Generator\[VoiceoverTracker, None, None\]_ – The voiceover tracker object.

Return type:

_Generator_\[ [_VoiceoverTracker_](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverTracker "manim_voiceover.tracker.VoiceoverTracker"), None, None\]

wait\_for\_voiceover() [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.wait_for_voiceover) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.wait_for_voiceover "Permalink to this definition")

Waits for the voiceover to finish.

Return type:

None

wait\_until\_bookmark( _mark_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/voiceover_scene.html#VoiceoverScene.wait_until_bookmark) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene.wait_until_bookmark "Permalink to this definition")

Waits until a bookmark is reached.

Parameters:

**mark** ( _str_) – The mark attribute of the bookmark to wait for.

Return type:

None

_class_ VoiceoverTracker( _scene_, _data_, _cache\_dir_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/tracker.html#VoiceoverTracker) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverTracker "Permalink to this definition")

Bases: `object`

Class to track the progress of a voiceover in a scene.

Initializes a VoiceoverTracker object.

Parameters:

- **scene** ( _Scene_) – The scene to which the voiceover belongs.

- **path** ( _str_) – The path to the JSON file containing the voiceover data.

- **data** ( _dict_) –

- **cache\_dir** ( _str_) –


get\_remaining\_duration( _buff=0.0_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/tracker.html#VoiceoverTracker.get_remaining_duration) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverTracker.get_remaining_duration "Permalink to this definition")

Returns the remaining duration of the voiceover.

Parameters:

**buff** ( _float_ _,_ _optional_) – A buffer to add to the remaining duration. Defaults to 0.

Returns:

The remaining duration of the voiceover in seconds.

Return type:

int

time\_until\_bookmark( _mark_, _buff=0_, _limit=None_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/tracker.html#VoiceoverTracker.time_until_bookmark) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverTracker.time_until_bookmark "Permalink to this definition")

Returns the time until a bookmark.

Parameters:

- **mark** ( _str_) – The mark attribute of the bookmark to count up to.

- **buff** ( _int_ _,_ _optional_) – A buffer to add to the remaining duration, in seconds. Defaults to 0.

- **limit** ( _Optional_ _\[_ _int_ _\]_ _,_ _optional_) – A maximum value to return. Defaults to None.


Return type:

int

## Speech services [\#](https://voiceover.manim.community/en/stable/api.html\#module-manim_voiceover.services.base "Permalink to this heading")

_class_ SpeechService( _global\_speed=1.0_, _cache\_dir=None_, _transcription\_model=None_, _transcription\_kwargs={}_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/base.html#SpeechService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "Permalink to this definition")

Bases: `ABC`

Abstract base class for a speech service.

Parameters:

- **global\_speed** ( _float_ _,_ _optional_) – The speed at which to play the audio.
Defaults to 1.00.

- **cache\_dir** ( _str_ _,_ _optional_) – The directory to save the audio
files to. Defaults to `voiceovers/`.

- **transcription\_model** ( _str_ _,_ _optional_) – The
[OpenAI Whisper model](https://github.com/openai/whisper#available-models-and-languages)
to use for transcription. Defaults to None.

- **transcription\_kwargs** ( _dict_ _,_ _optional_) – Keyword arguments to
pass to the transcribe() function. Defaults to {}.


audio\_callback( _audio\_path_, _data_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/base.html#SpeechService.audio_callback) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService.audio_callback "Permalink to this definition")

Callback function for when the audio file is ready.
Override this method to do something with the audio file, e.g. noise reduction.

Parameters:

- **audio\_path** ( _str_) – The path to the audio file.

- **data** ( _dict_) – The data dictionary.


_abstract_ generate\_from\_text( _text_, _cache\_dir=None_, _path=None_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/base.html#SpeechService.generate_from_text) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService.generate_from_text "Permalink to this definition")

Implement this method for each speech service. Refer to AzureService for an example.

Parameters:

- **text** ( _str_) – The text to synthesize speech from.

- **cache\_dir** ( _str_ _,_ _optional_) – The output directory to save the audio file and data to. Defaults to None.

- **path** ( _str_ _,_ _optional_) – The path to save the audio file to. Defaults to None.


Returns:

Output data dictionary. TODO: Define the format.

Return type:

dict

set\_transcription( _model=None_, _kwargs={}_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/base.html#SpeechService.set_transcription) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService.set_transcription "Permalink to this definition")

Set the transcription model and keyword arguments to be passed
to the transcribe() function.

Parameters:

- **model** ( _str_ _,_ _optional_) – The Whisper model to use for transcription. Defaults to None.

- **kwargs** ( _dict_ _,_ _optional_) – Keyword arguments to pass to the transcribe() function. Defaults to {}.


_class_ RecorderService( _format=None_, _channels=1_, _rate=44100_, _chunk=512_, _device\_index=None_, _transcription\_model='base'_, _trim\_silence\_threshold=-40.0_, _trim\_buffer\_start=200_, _trim\_buffer\_end=200_, _callback\_delay=0.05_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/recorder.html#RecorderService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

Speech service that records from a microphone during rendering.

Initialize the speech service.

Parameters:

- **format** ( _int_ _,_ _optional_) – Format of the audio. Defaults to pyaudio.paInt16.

- **channels** ( _int_ _,_ _optional_) – Number of channels. Defaults to 1.

- **rate** ( _int_ _,_ _optional_) – Sampling rate. Defaults to 44100.

- **chunk** ( _int_ _,_ _optional_) – Chunk size. Defaults to 512.

- **device\_index** ( _int_ _,_ _optional_) – Device index, if you don’t want to choose it every time you render. Defaults to None.

- **transcription\_model** ( _str_ _,_ _optional_) –

The [OpenAI Whisper model](https://github.com/openai/whisper#available-models-and-languages) to use for transcription. Defaults to “base”.

- **trim\_silence\_threshold** ( _float_ _,_ _optional_) – Threshold for trimming silence in decibels. Defaults to -40.0 dB.

- **trim\_buffer\_start** ( _int_ _,_ _optional_) – Buffer duration for trimming silence at the start. Defaults to 200 ms.

- **trim\_buffer\_end** ( _int_ _,_ _optional_) – Buffer duration for trimming silence at the end. Defaults to 200 ms.

- **callback\_delay** ( _float_) –


_class_ AzureService( _voice='en-US-AriaNeural'_, _style=None_, _output\_format='Audio48Khz192KBitRateMonoMp3'_, _prosody=None_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/azure.html#AzureService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.azure.AzureService "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

Speech service for Azure TTS API.

Parameters:

- **voice** ( _str_ _,_ _optional_) – The voice to use. See the [API page](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=stt-tts) for all the available options. Defaults to `en-US-AriaNeural`.

- **style** ( _str_ _,_ _optional_) – The style to use. See the [API page](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech?tabs=streaming#style) to see how you can see available styles for a given voice. Defaults to None.

- **output\_format** ( _str_ _,_ _optional_) – The output format to use. See the [API page](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/rest-text-to-speech?tabs=streaming#audio-outputs) for all the available options. Defaults to `Audio48Khz192KBitRateMonoMp3`.

- **prosody** ( _dict_ _,_ _optional_) – Global prosody settings to use. See the [API page](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-synthesis-markup#adjust-prosody) for all the available options. Defaults to None.


_class_ CoquiService( _model\_name='tts\_models/en/ljspeech/tacotron2-DDC'_, _config\_path=None_, _vocoder\_path=None_, _vocoder\_config\_path=None_, _progress\_bar=True_, _gpu=False_, _speaker\_idx=0_, _language\_idx=0_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/coqui.html#CoquiService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.coqui.CoquiService "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

Speech service for Coqui TTS.
Default model: `tts_models/en/ljspeech/tacotron2-DDC`.

Parameters:

- **global\_speed** ( _float_ _,_ _optional_) – The speed at which to play the audio.
Defaults to 1.00.

- **cache\_dir** ( _str_ _,_ _optional_) – The directory to save the audio
files to. Defaults to `voiceovers/`.

- **transcription\_model** ( _str_ _,_ _optional_) –

The
[OpenAI Whisper model](https://github.com/openai/whisper#available-models-and-languages)
to use for transcription. Defaults to None.

- **transcription\_kwargs** ( _dict_ _,_ _optional_) – Keyword arguments to
pass to the transcribe() function. Defaults to {}.

- **model\_name** ( _str_) –

- **config\_path** ( _str_) –

- **vocoder\_path** ( _str_) –

- **vocoder\_config\_path** ( _str_) –

- **progress\_bar** ( _bool_) –


generate\_from\_text( _text_, _cache\_dir=None_, _path=None_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/coqui.html#CoquiService.generate_from_text) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.coqui.CoquiService.generate_from_text "Permalink to this definition")

Implement this method for each speech service. Refer to AzureService for an example.

Parameters:

- **text** ( _str_) – The text to synthesize speech from.

- **cache\_dir** ( _str_ _,_ _optional_) – The output directory to save the audio file and data to. Defaults to None.

- **path** ( _str_ _,_ _optional_) – The path to save the audio file to. Defaults to None.


Returns:

Output data dictionary. TODO: Define the format.

Return type:

dict

_class_ GTTSService( _lang='en'_, _tld='com'_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/gtts.html#GTTSService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.gtts.GTTSService "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

SpeechService class for Google Translate’s Text-to-Speech API.
This is a wrapper for the gTTS library.
See the [gTTS documentation](https://gtts.readthedocs.io/en/latest/)
for more information.

Parameters:

- **lang** ( _str_ _,_ _optional_) – Language to use for the speech.
See [Google Translate docs](https://cloud.google.com/translate/docs/languages)
for all the available options. Defaults to “en”.

- **tld** ( _str_ _,_ _optional_) – Top level domain of the Google Translate URL. Defaults to “com”.


_class_ OpenAIService( _voice='alloy'_, _model='tts-1-hd'_, _transcription\_model='base'_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/openai.html#OpenAIService) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.openai.OpenAIService "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

Speech service class for OpenAI TTS Service. See the [OpenAI API page](https://platform.openai.com/docs/api-reference/audio/createSpeech)
for more information about voices and models.

Parameters:

- **voice** ( _str_ _,_ _optional_) – The voice to use. See the
[API page](https://platform.openai.com/docs/api-reference/audio/createSpeech)
for all the available options. Defaults to `"alloy"`.

- **model** ( _str_ _,_ _optional_) – The TTS model to use.
See the [API page](https://platform.openai.com/docs/api-reference/audio/createSpeech)
for all the available options. Defaults to `"tts-1-hd"`.


_class_ PyTTSX3Service( _engine=None_, _\*\*kwargs_) [\[source\]](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/pyttsx3.html#PyTTSX3Service) [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.pyttsx3.PyTTSX3Service "Permalink to this definition")

Bases: [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService")

Speech service class for pyttsx3.

## Defaults [\#](https://voiceover.manim.community/en/stable/api.html\#module-manim_voiceover.defaults "Permalink to this heading")

DEEPL\_SOURCE\_LANG _={'bg':'Bulgarian','cs':'Czech','da':'Danish','de':'German','el':'Greek','en':'English','es':'Spanish','et':'Estonian','fi':'Finnish','fr':'French','hu':'Hungarian','id':'Indonesian','it':'Italian','ja':'Japanese','lt':'Lithuanian','lv':'Latvian','nl':'Dutch','pl':'Polish','pt':'Portuguese(allPortuguesevarietiesmixed)','ro':'Romanian','ru':'Russian','sk':'Slovak','sl':'Slovenian','sv':'Swedish','tr':'Turkish','uk':'Ukrainian','zh':'Chinese'}_ [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.defaults.DEEPL_SOURCE_LANG "Permalink to this definition")

Available source languages for DeepL

DEEPL\_TARGET\_LANG _={'bg':'Bulgarian','cs':'Czech','da':'Danish','de':'German','el':'Greek','en':'Aliasforen-us','en-gb':'English(British)','en-us':'English(American)','es':'Spanish','et':'Estonian','fi':'Finnish','fr':'French','hu':'Hungarian','id':'Indonesian','it':'Italian','ja':'Japanese','lt':'Lithuanian','lv':'Latvian','nl':'Dutch','pl':'Polish','pt':'Aliasforpt-pt','pt-br':'Portuguese(Brazilian)','pt-pt':'Portuguese(allPortuguesevarietiesexcludingBrazilianPortuguese)','ro':'Romanian','ru':'Russian','sk':'Slovak','sl':'Slovenian','sv':'Swedish','tr':'Turkish','uk':'Ukrainian','zh':'Chinese(simplified)'}_ [#](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.defaults.DEEPL_TARGET_LANG "Permalink to this definition")

Available target languages for DeepL
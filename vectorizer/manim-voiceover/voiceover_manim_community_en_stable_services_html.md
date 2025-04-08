ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://voiceover.manim.community/en/stable/services.html#)

[Edit this page](https://github.com/ManimCommunity/manim-voiceover/edit/main/docs/source/services.rst "Edit this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Speech Services [\#](https://voiceover.manim.community/en/stable/services.html\#speech-services "Permalink to this heading")

Manim Voiceover can plug into various speech synthesizers to generate voiceover audio.
Below is a comparison of the available services, their pros and cons, and how to set them up.

## Choosing a speech service [\#](https://voiceover.manim.community/en/stable/services.html\#choosing-a-speech-service "Permalink to this heading")

Manim Voiceover defines the [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService") class for adding new speech synthesizers. The classes introduced below are all derived from [`SpeechService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.base.SpeechService "manim_voiceover.services.base.SpeechService").

| Speech service | Quality | Can run offline? | Paid / requires an account? | Notes |
| --- | --- | --- | --- | --- |
| [`RecorderService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService") | N/A | N/A | N/A | This is a utility class to record your own voiceovers with a microphone. |
| [`AzureService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.azure.AzureService "manim_voiceover.services.azure.AzureService") | Very good, human-like | No | Yes | Azure gives 500min/month free TTS quota. However, registration still needs a credit or debit card. See [Azure free account FAQ](https://azure.microsoft.com/en-us/free/free-account-faq/) for more details. |
| `ElevenLabsService` | Very good, human-like | No | Yes | Requires ElevenLabs account. Click [here](https://elevenlabs.io/sign-up) to sign up. |
| [`CoquiService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.coqui.CoquiService "manim_voiceover.services.coqui.CoquiService") | Good, human-like | Yes | No | Requires [PyTorch](https://pytorch.org/) to run. May be difficult to set up on certain platforms. |
| [`GTTSService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.gtts.GTTSService "manim_voiceover.services.gtts.GTTSService") | Good | No | No | It’s a free API subsidized by Google, so there is a likelihood it may stop working in the future. |
| [`OpenAIService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.openai.OpenAIService "manim_voiceover.services.openai.OpenAIService") | Very good, human-like | No | Yes | Requires OpenAI developer account. See [platform](https://platform.openai.com/signup) to sign up, and the [pricing page](https://openai.com/pricing#:~:text=%24-,0.030,-/%201K%20characters) for more details. |
| [`PyTTSX3Service`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.pyttsx3.PyTTSX3Service "manim_voiceover.services.pyttsx3.PyTTSX3Service") | Bad | Yes | No | Requires [espeak](https://espeak.sourceforge.net/). Does not work reliably on Mac. |

Comparison of available speech services [#](https://voiceover.manim.community/en/stable/services.html#id1 "Permalink to this table")

It is on our roadmap to provide a high quality TTS engine that runs locally for free. If you have any suggestions, please let us know in the [Discord server](https://manim.community/discord).

## [`RecorderService`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService") [\#](https://voiceover.manim.community/en/stable/services.html\#recorderservice "Permalink to this heading")

This is not a speech synthesizer but a utility class to record your own voiceovers with a microphone. It provides a command line interface to record voiceovers during rendering.

Install Manim Voiceover with the `recorder` extra in order to use [`RecorderService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService"):

```
pip install "manim-voiceover[recorder]"

```

Copy to clipboard

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/recorder-example.py) to get started.

## [`AzureService`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.azure.AzureService "manim_voiceover.services.azure.AzureService") [\#](https://voiceover.manim.community/en/stable/services.html\#azureservice "Permalink to this heading")

As of now, the highest quality text-to-speech service available in Manim Voiceover is [Microsoft Azure Speech Service](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/overview). To use it, you will need to [create an\\
Azure account](https://azure.microsoft.com/en-us/free/).

Tip

Azure currently offers free TTS of 500 minutes/month. This is more than enough for most projects.

Install Manim Voiceover with the `azure` extra in order to use [`AzureService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.azure.AzureService "manim_voiceover.services.azure.AzureService"):

```
pip install "manim-voiceover[azure]"

```

Copy to clipboard

Then, you need to find out your subscription key and service region:

- Sign in to [Azure portal](https://portal.azure.com/) and create a new Speech Service resource.

- Go to the [Azure Cognitive Services page](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.CognitiveServices%2Faccounts).

- Click on the resource you created and go to the `Keys and Endpoint` tab. Copy the `Key 1` and `Location` values.


Create a file called `.env` that contains your authentication
information in the same directory where you call Manim.

```
AZURE_SUBSCRIPTION_KEY="..." # insert Key 1 here
AZURE_SERVICE_REGION="..."   # insert Location here

```

Copy to clipboard

Check out [Azure\\
docs](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/)
for more details.

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/azure-example.py) to get started.

## [`CoquiService`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.coqui.CoquiService "manim_voiceover.services.coqui.CoquiService") [\#](https://voiceover.manim.community/en/stable/services.html\#coquiservice "Permalink to this heading")

[Coqui TTS](https://tts.readthedocs.io/) is an open source neural text-to-speech engine.
It is a fork of Mozilla TTS, which is an implementation of Tacotron 2.
It is a very good TTS engine that produces human-like speech.
However, it requires [PyTorch](https://pytorch.org/) to run, which may be difficult to set up on certain platforms.

Install Manim Voiceover with the `coqui` extra in order to use [`CoquiService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.coqui.CoquiService "manim_voiceover.services.coqui.CoquiService"):

```
pip install "manim-voiceover[coqui]"

```

Copy to clipboard

If you run into issues with PyTorch or NumPy, try changing your Python version to 3.9.

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/coqui-example.py) to get started.

## [`GTTSService`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.gtts.GTTSService "manim_voiceover.services.gtts.GTTSService") [\#](https://voiceover.manim.community/en/stable/services.html\#gttsservice "Permalink to this heading")

[gTTS](https://gtts.readthedocs.io/) is a text-to-speech
library that wraps Google Translate’s text-to-speech API. It needs an internet connection to work.

Install Manim Voiceover with the `gtts` extra in order to use [`GTTSService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.gtts.GTTSService "manim_voiceover.services.gtts.GTTSService"):

```
pip install "manim-voiceover[gtts]"

```

Copy to clipboard

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/gtts-example.py) to get started.

## [`OpenAIService`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.openai.OpenAIService "manim_voiceover.services.openai.OpenAIService") [\#](https://voiceover.manim.community/en/stable/services.html\#openaiservice "Permalink to this heading")

[OpenAI](https://platform.openai.com/docs/api-reference/audio/createSpeech/) provides a text-to-speech service. It is through an API, so it requires an internet connection to work. It also requires an API key to use. Register for one [here](https://platform.openai.com/).

Install Manim Voiceover with the `openai` extra in order to use [`OpenAIService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.openai.OpenAIService "manim_voiceover.services.openai.OpenAIService"):

```
pip install "manim-voiceover[openai]"

```

Copy to clipboard

Then, you need to find out your api key:

- Sign in to [OpenAI platform](https://platform.openai.com/) and click into Api Keys from the left panel.

- Click create a new secret key and copy it.


Create a file called `.env` that contains your authentication
information in the same directory where you call Manim.

```
OPENAI_API_KEY="..." # insert the secret key here. It should start with "sk-"

```

Copy to clipboard

Check out [OpenAI docs](https://platform.openai.com/docs/guides/text-to-speech/) for more details.

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/openai-example.py) to get started.

## [`PyTTSX3Service`](https://voiceover.manim.community/en/stable/api.html\#manim_voiceover.services.pyttsx3.PyTTSX3Service "manim_voiceover.services.pyttsx3.PyTTSX3Service") [\#](https://voiceover.manim.community/en/stable/services.html\#pyttsx3service "Permalink to this heading")

[pyttsx3](https://pyttsx3.readthedocs.io/) is a text-to-speech
library that wraps [espeak](https://espeak.sourceforge.net/), a formant synthesis speech synthesizer.

Install Manim Voiceover with the `pyttsx3` extra in order to use [`PyTTSX3Service`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.pyttsx3.PyTTSX3Service "manim_voiceover.services.pyttsx3.PyTTSX3Service"):

```
pip install "manim-voiceover[pyttsx3]"

```

Copy to clipboard

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/pyttsx3-example.py) to get started.

## `ElevenLabsService` [\#](https://voiceover.manim.community/en/stable/services.html\#elevenlabsservice "Permalink to this heading")

[ElevenLabs](https://www.elevenlabs.io/) offers one of the most natural sounding speech service APIs. It has a range of realistic and emotive voices, and also allows you to clone your own voice by uploading a few minutes of your speech. To use it, you will need to create an account at [Eleven Labs](https://elevenlabs.io/sign-up).

Tip

ElevenLabs currently offers free TTS of 10,000 characters/month and up to 3 custom voices.

Install Manim Voiceover with the `elevenlabs` extra in order to use `ElevenLabsService`:

```
pip install "manim-voiceover[elevenlabs]"

```

Copy to clipboard

Then, you need to find out your API key.

- Sign in to [ElevenLabs portal](https://www.elevenlabs.io/) and go to your profile to obtain the key

- Set the environment variable `ELEVEN_API_KEY` to your key


Create a file called `.env` that contains your authentication
information in the same directory where you call Manim.

```
ELEVEN_API_KEY="..." # insert Key 1 here

```

Copy to clipboard

Check out [ElevenLabs\\
docs](https://elevenlabs.io/docs/api-reference/python-text-to-speech-guide#getting-started)
for more details.

Refer to the [example usage](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/elevenlabs-example.py) to get started.
ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://voiceover.manim.community/en/stable/#)

[Edit this page](https://github.com/ManimCommunity/manim-voiceover/edit/main/docs/source/index.rst "Edit this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Manim Voiceover [\#](https://voiceover.manim.community/en/stable/\#manim-voiceover "Permalink to this heading")

[Manim Voiceover](https://voiceover.manim.community/) is a [Manim](https://manim.community/) plugin for all things voiceover:

- Add voiceovers to Manim videos _directly in Python_ without having to use a video editor.

- Record voiceovers with your microphone during rendering with a simple command line interface (see [`RecorderService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService")).

- Develop animations with auto-generated AI voices from various free and proprietary services.

- Per-word timing of animations, i.e. trigger animations at specific words in the voiceover, even for the recordings. This works thanks to [OpenAI Whisper](https://github.com/openai/whisper).


A demo:

Video


- [Installation](https://voiceover.manim.community/en/stable/installation.html)
  - [Extras](https://voiceover.manim.community/en/stable/installation.html#extras)
  - [Installing PortAudio](https://voiceover.manim.community/en/stable/installation.html#installing-portaudio)
  - [Installing SoX](https://voiceover.manim.community/en/stable/installation.html#installing-sox)
  - [Installing gettext](https://voiceover.manim.community/en/stable/installation.html#installing-gettext)
- [Quickstart](https://voiceover.manim.community/en/stable/quickstart.html)
  - [Basic Usage](https://voiceover.manim.community/en/stable/quickstart.html#basic-usage)
  - [Bookmarks](https://voiceover.manim.community/en/stable/quickstart.html#bookmarks)
  - [Record your own voiceover](https://voiceover.manim.community/en/stable/quickstart.html#record-your-own-voiceover)
  - [Generate voiceovers in a different language](https://voiceover.manim.community/en/stable/quickstart.html#generate-voiceovers-in-a-different-language)
- [Speech Services](https://voiceover.manim.community/en/stable/services.html)
  - [Choosing a speech service](https://voiceover.manim.community/en/stable/services.html#choosing-a-speech-service)
  - [`RecorderService`](https://voiceover.manim.community/en/stable/services.html#recorderservice)
  - [`AzureService`](https://voiceover.manim.community/en/stable/services.html#azureservice)
  - [`CoquiService`](https://voiceover.manim.community/en/stable/services.html#coquiservice)
  - [`GTTSService`](https://voiceover.manim.community/en/stable/services.html#gttsservice)
  - [`OpenAIService`](https://voiceover.manim.community/en/stable/services.html#openaiservice)
  - [`PyTTSX3Service`](https://voiceover.manim.community/en/stable/services.html#pyttsx3service)
  - [`ElevenLabsService`](https://voiceover.manim.community/en/stable/services.html#elevenlabsservice)
- [Example Gallery](https://voiceover.manim.community/en/stable/examples.html)
  - [Demo video](https://voiceover.manim.community/en/stable/examples.html#demo-video)
  - [Approximating \\(\\tau\\)](https://voiceover.manim.community/en/stable/examples.html#approximating-tau)
  - [Quadratic formula in Arabic](https://voiceover.manim.community/en/stable/examples.html#quadratic-formula-in-arabic)
- [Translating Scenes](https://voiceover.manim.community/en/stable/translate.html)
  - [Translating scenes with machine translation](https://voiceover.manim.community/en/stable/translate.html#translating-scenes-with-machine-translation)
  - [Available languages](https://voiceover.manim.community/en/stable/translate.html#available-languages)
  - [Editing and maintaining translations](https://voiceover.manim.community/en/stable/translate.html#editing-and-maintaining-translations)
- [API Reference](https://voiceover.manim.community/en/stable/api.html)
  - [Voiceover scene](https://voiceover.manim.community/en/stable/api.html#module-manim_voiceover)
  - [Speech services](https://voiceover.manim.community/en/stable/api.html#module-manim_voiceover.services.base)
  - [Defaults](https://voiceover.manim.community/en/stable/api.html#module-manim_voiceover.defaults)
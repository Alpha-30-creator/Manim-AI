ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://voiceover.manim.community/en/stable/quickstart.html#)

[Edit this page](https://github.com/ManimCommunity/manim-voiceover/edit/main/docs/source/quickstart.rst "Edit this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Quickstart [\#](https://voiceover.manim.community/en/stable/quickstart.html\#quickstart "Permalink to this heading")

Before proceeding, install Manim Voiceover and make sure it’s running properly by following the steps in [Installation](https://voiceover.manim.community/en/stable/installation.html).

## Basic Usage [\#](https://voiceover.manim.community/en/stable/quickstart.html\#basic-usage "Permalink to this heading")

To use Manim Voiceover, you simply import the [`VoiceoverScene`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene "manim_voiceover.VoiceoverScene")
class from the plugin

```
from manim_voiceover import VoiceoverScene

```

Copy to clipboard

Make your scene inherit from [`VoiceoverScene`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.VoiceoverScene "manim_voiceover.VoiceoverScene"):

```
class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        ...

```

Copy to clipboard

You can also inherit from multiple scene classes:

```
from manim.scene.moving_camera_scene import MovingCameraScene

class MyAwesomeScene(MovingCameraScene, VoiceoverScene):
    def construct(self):
        ...

```

Copy to clipboard

This should work as long as the variables or methods of parent classes do not collide.

Manim Voiceover can use various text-to-speech engines, some
proprietary and some free. A good one to start with is gTTS, which uses
the Google Translate API. We found out that this is the best
for beginning to use the library owing to its cross-platform compatibility—however it still needs
an internet connection.

```
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

```

Copy to clipboard

The logic for adding a voiceover is pretty simple. Wrap the animation
inside a `with` block that calls `self.voiceover()`:

```
with self.voiceover(text="This circle is drawn as I speak.") as tracker:
    ... # animate whatever needs to be animated here

```

Copy to clipboard

Manim will animate whatever is inside that with block. If the voiceover
hasn’t finished by the end of the animation, Manim will wait
until it finishes. Furthermore, you can use the `tracker` object for getting
the total or remaining duration of the voiceover programmatically, which
gives you finer control over the scene:

```
with self.voiceover(text="This circle is drawn as I speak.") as tracker:
    self.play(Create(circle), run_time=tracker.duration)

```

Copy to clipboard

Tip

Using with-blocks allows you to chain sentences back to back and results in code that is easier to read, since voiceover calls are practically comments.

The `text` argument is automatically reused for video subcaptions. Alternatively, you can supply a custom subcaption:

```
with self.voiceover(
    text="This circle is drawn as I speak.",
    subcaption="What a cute circle! :)"
) as tracker:
    self.play(Create(circle))

```

Copy to clipboard

See [Example Gallery](https://voiceover.manim.community/en/stable/examples.html) and the [examples directory](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples)
for more examples. We recommend starting with the [gTTS\\
example](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/gtts-example.py).

## Bookmarks [\#](https://voiceover.manim.community/en/stable/quickstart.html\#bookmarks "Permalink to this heading")

One of the most important features of Manim Voiceover is bookmarks.
Bookmarks allow you to trigger an animation at a specific word in the voiceover.

Video


With bookmarks, you can time your animations much more precisely. See the [bookmark example](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/bookmark-example.py) and [Approximating Tau](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/approximating-tau.py) for more examples.

## Record your own voiceover [\#](https://voiceover.manim.community/en/stable/quickstart.html\#record-your-own-voiceover "Permalink to this heading")

Manim Voiceover can record your voiceover directly from the command line. We recommend the following workflow:

1. Develop your animation with one of the text-to-speech engines, e.g. [`services.gtts.GTTSService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.gtts.GTTSService "manim_voiceover.services.gtts.GTTSService"):


```
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle))

```

Copy to clipboard

2. When you’re happy with the animation, switch the service with [`services.recorder.RecorderService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService") to record your own voiceover:


```
from manim_voiceover import VoiceoverScene
# from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.recorder import RecorderService

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        # self.set_speech_service(GTTSService())
        self.set_speech_service(RecorderService())

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle))

```

Copy to clipboard

3. Render the scene the same way you would normally do:


```
manim -pql my_awesome_scene.py --disable_caching

```

Copy to clipboard

This will instruct you in the terminal step by step what to do to record your voiceover.

## Generate voiceovers in a different language [\#](https://voiceover.manim.community/en/stable/quickstart.html\#generate-voiceovers-in-a-different-language "Permalink to this heading")

Each speech service supports a different set of options, and some of them
support multiple languages. You can learn about these options in the
[Speech services](https://voiceover.manim.community/en/stable/api.html#api-speech-services) section in the API reference.

For example, [`services.gtts.GTTSService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.gtts.GTTSService "manim_voiceover.services.gtts.GTTSService")
supports all the languages supported by Google Translate, which you
can find [here](https://cloud.google.com/translate/docs/languages).
The [gTTS example](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/gtts-example.py)
implements the same scene in English and Vietnamese as a demonstration.

If you can’t find a good text-to-speech engine for your language, you can directly
record your own voiceover using [`services.recorder.RecorderService`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.services.recorder.RecorderService "manim_voiceover.services.recorder.RecorderService").
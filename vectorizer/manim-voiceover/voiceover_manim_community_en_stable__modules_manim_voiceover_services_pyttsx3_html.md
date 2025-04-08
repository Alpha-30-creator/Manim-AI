ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://voiceover.manim.community/en/stable/_modules/manim_voiceover/services/pyttsx3.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Source code for manim\_voiceover.services.pyttsx3

```
from pathlib import Path
from manim import logger
from manim_voiceover.helper import prompt_ask_missing_extras

try:
    from pyttsx3 import Engine
except ImportError:
    logger.error(
        'Missing packages. Run `pip install "manim-voiceover[pyttsx3]"` to use PyTTSX3Service.'
    )

from manim_voiceover.services.base import SpeechService

[docs]class PyTTSX3Service(SpeechService):
    """Speech service class for pyttsx3."""

    def __init__(self, engine=None, **kwargs):
        """"""
        prompt_ask_missing_extras("pyttsx3", "pyttsx3", "PyTTSX3Service")

        if engine is None:
            engine = Engine()

        self.engine = engine
        SpeechService.__init__(self, **kwargs)

    def generate_from_text(
        self, text: str, cache_dir: str = None, path: str = None
    ) -> dict:
        """"""
        if cache_dir is None:
            cache_dir = self.cache_dir

        input_data = {"input_text": text, "service": "pyttsx3"}

        cached_result = self.get_cached_result(input_data, cache_dir)
        if cached_result is not None:
            return cached_result

        if path is None:
            audio_path = self.get_audio_basename(input_data) + ".mp3"
        else:
            audio_path = path

        self.engine.save_to_file(text, str(Path(cache_dir) / audio_path))
        self.engine.runAndWait()
        self.engine.stop()

        json_dict = {
            "input_text": text,
            "input_data": input_data,
            "original_audio": audio_path,
        }

        return json_dict

```

Copy to clipboard
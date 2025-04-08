# Translating Scenes [\#](https://voiceover.manim.community/en/stable/translate.html\#translating-scenes "Permalink to this heading")

Manim Voiceover supports translating scenes into other languages. It uses the [gettext](https://en.wikipedia.org/wiki/Gettext) convention of wrapping translatable strings in `_()`. gettext is an established internationalization and localization (i18n and l10n) system commonly used for writing multilingual programs. It allows you to keep your Manim scenes and all of the translations organized neatly in the same git repository.

Check out [the translation example](https://github.com/ManimCommunity/manim-voiceover/tree/main/examples/translation-example/):

```
import os
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.translate import get_gettext

# It is good practice to get the LOCALE and DOMAIN from environment variables
LOCALE = os.getenv("LOCALE")
DOMAIN = os.getenv("DOMAIN")

# The following function uses LOCALE and DOMAIN to set the language, and
# returns a gettext function that is used to insert translations.
_ = get_gettext()

class TranslationExample(VoiceoverScene):
    def construct(self):
        # We use the free TTS service from Google Translate
        # The TTS language is set via the LOCALE environment variable
        self.set_speech_service(GTTSService(lang=LOCALE))

        circle = Circle()
        square = Square().shift(2 * RIGHT)

        # The voiceover strings are wrapped in _()
        # This means that their translations will be looked up in the .po files
        # and used to replace the original strings
        with self.voiceover(text=_("This circle is drawn as I speak.")) as tracker:
            self.play(Create(circle), run_time=tracker.duration)

        with self.voiceover(text=_("Let's shift it to the left 2 units.")) as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

        with self.voiceover(
            text=_("Now, let's transform it into a square.")
        ) as tracker:
            self.play(Transform(circle, square), run_time=tracker.duration)

        with self.voiceover(text=_("Thank you for watching.")):
            self.play(Uncreate(circle))

        self.wait()

```

Copy to clipboard

In this example, the German and Vietnamese translations are available in the files [locale/de/LC\_MESSAGES/translation-example.po](https://github.com/ManimCommunity/manim-voiceover/tree/main/examples/translation-example/locale/de/LC_MESSAGES/translation-example.po) and [locale/vi/LC\_MESSAGES/translation-example.po](https://github.com/ManimCommunity/manim-voiceover/tree/main/examples/translation-example/locale/vi/LC_MESSAGES/translation-example.po) respectively.

We have introduced the command line utility `manim_render_translation` to make it easier to render translations. It is similar to calling `manim render`, but it also lets you choose which locale (i.e. language) to render:

```
# Assuming you are in the root directory of manim-voiceover repo
cd examples/translation-example
manim_render_translation translation-example.py \
    -s TranslationExample                       \
    -d translation-example                      \
    -l de,vi                                    \
    -qh

```

Copy to clipboard

Here,

- `-s`: Scene to render.

- `-d`: gettext domain (the name of the translation file wihout the `.po` extension)

- `-l`: Locale to render. If not specified, all locales will be rendered.

- `-q`: Render quality, same as in `manim render`.


For more information, run `manim_render_translation --help`.

## Translating scenes with machine translation [\#](https://voiceover.manim.community/en/stable/translate.html\#translating-scenes-with-machine-translation "Permalink to this heading")

We have also introduced the command line utility `manim_translate` to make it easier to translate scenes. It uses the [DeepL API](https://www.deepl.com/pro-api) to translate the voiceover strings in a scene into other languages. DeepL is a paid service, but it allows you to translate up to 500,000 characters per month for free. You can sign up for a free account [here](https://www.deepl.com/signup).

Once you have signed up for a DeepL account, generate an API key and set it as the environment variable `DEEPL_API_KEY`. If you save it in a file `.env` in the root directory of the project, it will be automatically loaded when you run `manim_translate`. For example,

```
# Assuming you are in the root directory of manim-voiceover repo
cd examples/translation-example
manim_translate translation-example.py \
    -s en                              \
    -t tr                              \
    -d translation-example

```

Copy to clipboard

Here,

- `-s`: Original (source) language of the scene.

- `-t`: Target language to translate to.

- `-d`: gettext domain to save the translation to (the name of the translation file wihout the `.po` extension)


Running this command will generate a file `locale/tr/LC_MESSAGES/translation-example.po` containing the translated strings. You can then render the scene in Turkish by running

```
manim_render_translation translation-example.py -s TranslationExample -d translation-example -l tr

```

Copy to clipboard

For more information, run `manim_translate --help`.

## Available languages [\#](https://voiceover.manim.community/en/stable/translate.html\#available-languages "Permalink to this heading")

Manim Voiceover follows the [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard for language codes. For example, the language code for English is `en`, and the language code for Vietnamese is `vi`.

Check out [`DEEPL_SOURCE_LANG`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.defaults.DEEPL_SOURCE_LANG "manim_voiceover.defaults.DEEPL_SOURCE_LANG") for languages you can translate from, and [`DEEPL_TARGET_LANG`](https://voiceover.manim.community/en/stable/api.html#manim_voiceover.defaults.DEEPL_TARGET_LANG "manim_voiceover.defaults.DEEPL_TARGET_LANG") for languages you can translate to.

The [DeepL API documentation](https://www.deepl.com/docs-api/translate-text/) has more detailed information about the available languages. If DeepL has added support for a new language and it is not yet available in Manim Voiceover, please [open an issue](https://github.com/ManimCommunity/manim-voiceover/issues/new/choose) or [submit a pull request](https://github.com/ManimCommunity/manim-voiceover/pulls) to get it included.

## Editing and maintaining translations [\#](https://voiceover.manim.community/en/stable/translate.html\#editing-and-maintaining-translations "Permalink to this heading")

The translations generated by `manim_translate` can be edited manually in the `.po` files. You can also use a GUI tool such as [Poedit](https://poedit.net/) to edit the translations. The `.po` files are in the [gettext](https://en.wikipedia.org/wiki/Gettext) format, which is a standard for storing translations. You can find more information about the format [here](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html).

Running `manim_translate` will not overwrite your existing translations, and instead will only fill in the missing translations. If you make changes to the original scene, you can run `manim_translate` again. This will insert the new strings into the `locale/<domain>.pot` and `locale/<domain>/LC_MESSAGES/<domain>.po` files, and use DeepL to translate the new strings into the target languages.

Important

We recommend to start a [git](https://git-scm.com/) repository for your project, and include the `.po` files. This will make it easier to track changes to the translations and to merge changes from other contributors. It will also allow you to revert back to an earlier version of the translations if you make a mistake.

Do not include `.mo` files in your git repository. These are binary files that are automatically generated from the `.po` files. Add the line `*.mo` to your `.gitignore` file to prevent them from being added to your git repository.
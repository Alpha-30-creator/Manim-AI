ContentsMenuExpandLight modeDark modeAuto light/dark mode

[Back to top](https://voiceover.manim.community/en/stable/installation.html#)

[Edit this page](https://github.com/ManimCommunity/manim-voiceover/edit/main/docs/source/installation.rst "Edit this page")

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Installation [\#](https://voiceover.manim.community/en/stable/installation.html\#installation "Permalink to this heading")

Install Manim Voiceover from PyPI with the extras `azure` and `gtts`:

```
pip install --upgrade "manim-voiceover[azure,gtts]"

```

Copy to clipboard

Check whether your installation works correctly:

```
wget https://github.com/ManimCommunity/manim-voiceover/raw/main/examples/gtts-example.py
manim -pql gtts-example.py --disable_caching

```

Copy to clipboard

Important

Manim needs to be called with the `--disable_caching` flag due to a [bug](https://github.com/ManimCommunity/manim/pull/907).
Don’t forget to include it every time you render.

[The example above](https://github.com/ManimCommunity/manim-voiceover/blob/main/examples/gtts-example.py) uses
[gTTS](https://github.com/pndurette/gTTS/) which calls the Google
Translate API and therefore needs an internet connection to work. If it
throws an error, there might be a problem with your internet connection
or the Google Translate API.

## Extras [\#](https://voiceover.manim.community/en/stable/installation.html\#extras "Permalink to this heading")

Manim Voiceover does not install all dependencies by default. It will detect on the fly which packages are missing and will ask for your permission to install them, so you don’t have to worry about installing them manually.

If you want to install all of the dependencies, use the `all` extra:

```
pip install --upgrade "manim-voiceover[all]"

```

Copy to clipboard

You can see other extras in the [pyproject.toml](https://github.com/ManimCommunity/manim-voiceover/blob/main/pyproject.toml) file.

## Installing PortAudio [\#](https://voiceover.manim.community/en/stable/installation.html\#installing-portaudio "Permalink to this heading")

Manim Voiceover lets you record voiceovers during rendering using [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/).
PyAudio depends on [PortAudio](http://www.portaudio.com/) which needs to be installed separately.

On Debian based distros:

```
sudo apt install portaudio19-dev
sudo pip install pyaudio
# Or install from apt globally:
sudo apt install python3-pyaudio

```

Copy to clipboard

On macOS, you can install it using [Homebrew](https://brew.sh/):

```
brew install portaudio
pip install pyaudio

```

Copy to clipboard

On Windows, PortAudio should come prepackaged with the binaries, so just install PyAudio with pip:

```
python -m pip install pyaudio

```

Copy to clipboard

For more information, see the [PyAudio documentation](https://people.csail.mit.edu/hubert/pyaudio/#downloads).

## Installing SoX [\#](https://voiceover.manim.community/en/stable/installation.html\#installing-sox "Permalink to this heading")

Manim Voiceover can make the output from speech synthesizers faster
or slower using [SoX](http://sox.sourceforge.net/) (version 14.4.2 or
higher is required).

Install SoX on Mac with Homebrew:

```
brew install sox

```

Copy to clipboard

Install SoX (and a necessary mp3 handler) on Debian based distros:

```
sudo apt-get install sox libsox-fmt-all

```

Copy to clipboard

Or install [from\\
source](https://sourceforge.net/projects/sox/files/sox/).

## Installing gettext [\#](https://voiceover.manim.community/en/stable/installation.html\#installing-gettext "Permalink to this heading")

Manim Voiceover uses [gettext](https://www.gnu.org/software/gettext/) to
store and fetch translations of voiceover text. If you plan to translate
your videos automatically, you need to install gettext.

On Debian based distros:

```
sudo apt install gettext

```

Copy to clipboard

On macOS, you can install it using [Homebrew](https://brew.sh/):

```
brew install gettext

```

Copy to clipboard
# FAQ: Getting Help [¶](https://docs.manim.community/en/stable/faq/help.html\#faq-getting-help "Link to this heading")

## How do I animate X? Why do I get error Y? Can someone help me? [¶](https://docs.manim.community/en/stable/faq/help.html\#how-do-i-animate-x-why-do-i-get-error-y-can-someone-help-me "Link to this heading")

Before asking the community, please make sure that the issue you are having
is not already discussed in our [FAQ section](https://docs.manim.community/en/stable/faq/index.html) sufficiently
well so that you can resolve the problem yourself. You can also try to
use your favorite search engine, if you are lucky you might find a blog post,
a question on [StackOverflow](https://stackoverflow.com/questions/tagged/manim),
or a post in the [r/manim subreddit](https://reddit.com/r/manim).

If this is not the case, please take a moment to properly prepare your question:
the better you manage to explain what exactly it is you are struggling with,
the more efficient people will be able to help you. Regardless of the platform
you choose in the next step, StackOverflow has a good guide on
[asking good questions](https://stackoverflow.com/help/how-to-ask).

As soon as you have a good idea of what exactly you want to ask, pick one of the
following communication channels:

- The community is most active [in our Discord server](https://manim.community/discord/).
Click the link to join, then pick one of the `#manim-help` channels in the sidebar,
and post your question there. If you are comfortable with using Discord, try to search
for your problem using the search function of our server; perhaps people have been
talking about it before!

- We are also monitoring questions on
[StackOverflow](https://stackoverflow.com/questions/tagged/manim) that are tagged
with `manim`.

- Many people are also active in our [r/manim subreddit](https://reddit.com/r/manim),
feel free to post there if you are an avid Redditor – but be aware that Discord
or StackOverflow might be better choices.

- And finally, you can also start a new [discussion on GitHub](https://github.com/ManimCommunity/manim/discussions)
if you dislike all other options.


In all of these channels, please make sure to abide by Manim’s
[Code of Conduct](https://docs.manim.community/en/stable/conduct.html) – in short, be _excellent_ to one another:
be friendly and patient, considerate, and respectful.

* * *

## What should I do if nobody answers my question? [¶](https://docs.manim.community/en/stable/faq/help.html\#what-should-i-do-if-nobody-answers-my-question "Link to this heading")

Try and see whether your question can be improved: did you include all relevant
information (in case of errors: the full stack trace, the code that you were
rendering, and the command you used to run Manim?). In case you used a very long
example, is it possible to construct a more minimal version that has the same
(faulty) behavior?

If you posted in one of our help channels on Discord and your question got buried,
you are allowed to ping the `@Manim Helper` role to bring it to the attention of
the volunteers who are willing to take a look. Please refrain from pinging the role
immediately when asking your question for the first time, this is considered impolite.

You can also try to post your question to a different channel if you feel that you
are not having any success with your initial choice – but please do not spam your
question in all of our communication channels (and in particular for Discord:
please don’t use multiple help channels at once).

In the end, it is as for most open-source projects: our community members are
volunteers. If you do not receive a quick answer to your question, it may be
because nobody knows the answer, or because your question is not clear enough,
or it could be that everyone who can help you with your problem is busy doing
other things.

* * *

## The library does not behave as documented, or something broke in a new release. What should I do? [¶](https://docs.manim.community/en/stable/faq/help.html\#the-library-does-not-behave-as-documented-or-something-broke-in-a-new-release-what-should-i-do "Link to this heading")

Sounds like you have found a bug. One of the best ways of contributing to the
development of Manim is by reporting it!

Check our list of known issues and feature requests
[in our GitHub repository](https://github.com/ManimCommunity/manim/issues). If the
problem you have found is not listed there yet (use the search function; also check
whether there is a corresponding closed issue, it is possible that your problem
has already been resolved and will be fixed with the next release), please consider
the following steps to submit a new issue.

Note

If you are unsure whether or not you should file a new issue for some odd behavior
that you found, feel free to ask the community developers, preferably in one of
our `#manim-dev` channels in [our Discord](https://manim.community/discord/).

1. Make sure you are running the latest released version of Manim, your problem
might otherwise already be fixed in a more recent version. Check the
[Changelog](https://docs.manim.community/en/stable/changelog.html) for a full list of changes between Manim releases.

2. Choose the correct category for your report when
[creating a new issue](https://github.com/ManimCommunity/manim/issues/new/choose).
We have dedicated issue templates for _bug reports_, _feature requests_, and
_installation issues_. If your report falls into one of these
categories, read the issue template carefully! Instructions are given in the
`<!-- ... -->` sections of the text field. If you want to suggest a new feature
without concrete implementation details, see
[the instructions given in this answer](https://docs.manim.community/en/stable/faq/help.html#creating-suggestions).

3. For bug reports: prepare a minimal example that can be used to illustrate the
issue. Examples with hundreds of lines are very inefficient and tedious to debug.
Your problem needs to be reproducible for others, so please make sure to prepare
a suitable example.

4. This is mentioned in the bug report template as well, but it is very important:
if you report that some code raises an error, make sure to include the full
terminal output, from the command you used to run the library up to and including
the last line with the error message. Read carefully: if the message mentions
that there is another relevant log file, include this other file as well!


* * *

## I have an idea for a really cool feature that should be implemented, where should I share my idea? [¶](https://docs.manim.community/en/stable/faq/help.html\#i-have-an-idea-for-a-really-cool-feature-that-should-be-implemented-where-should-i-share-my-idea "Link to this heading")

New suggestions and proposals should be made by
[creating a new discussion](https://github.com/ManimCommunity/manim/discussions/new?category=suggestions-and-proposals)
in the [_Suggestions and Proposals_ category](https://github.com/ManimCommunity/manim/discussions/categories/suggestions-and-proposals)
in our GitHub repository. Once the raw idea has been formed into a more concrete,
implementable proposal that is supported by the community, and someone has expressed
interest in working on the new feature, a corresponding
[issue](https://github.com/ManimCommunity/manim/issues) will be created. Do **not** create
issues for suggesting new features directly, they will be closed down.
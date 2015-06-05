import re
# mash all successive dashes (two or more):
dashes = re.compile(r"-{2,}")
dashesNotHyphens = re.compile(r"[^\w](-)[^\w]")

def removeSymbols(text):
    """Removes all symbols as they serve no
    semantical purpose for us."""

    # string.punctuation also includes "-" which we want to keep.
    # Furthermore, we also want to remove some additional symbols:
    for c in "<>|[]{}()@#$€£%&*_=+,.?!'\"«»“”;:/\\~`":
        # it's faster to determine this first instead of blindly replacing:
        if c in text:
            text = text.replace(c, " ")

    # replace multiple dashes with space:
    text = dashes.sub(" ", text)
    # replace leftover dashes that don't act as hyphens connecting two words:
    text = dashesNotHyphens.sub(" ", text)

    return text
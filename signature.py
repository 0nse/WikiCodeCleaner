import re

# [[User:Any text|Any text]] ([[User talk:Any text|Any text]]) -- the mid bar is optional:
user = re.compile(r"\[\[User:[^\]]+\]\] \(\[\[User talk:[^\]]+\]\]\)")
# e.g. 13:41, 9 June 2015 (UTC) -- the characters are the valid characters for all months:
timestamp = re.compile(r"\d{2}:\d{2}, \d{1,2} [JFMASOND][ebruaynchpilgstovm]+ \d{4} \(\w+\)")

def removeSignature(text):
    # @see https://en.wikipedia.org/wiki/Wikipedia:Signatures
    text = user.sub("", text)
    text = timestamp.sub("", text)

    return text
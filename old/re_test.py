import re

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())

pair = re.compile(r'.*([0-9]).*\1hello(\1)$')
m = pair.match('NotAffected3NotAffected3hello3')
print m.group(2)

import re
line = 'asdf fjdk; afed, fjek,asdf, foo'

print(re.split(r'[;,\s]\s*', line))

fields = re.split(r'(;|,|\s)\s*', line)

print(fields)
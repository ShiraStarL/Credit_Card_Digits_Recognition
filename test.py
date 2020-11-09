import re

line = 'a sdf     fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))
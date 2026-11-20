import sys, json
import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
row = json.loads(sys.argv[1])
s = open('build_log.py').read()
i = s.index('rows = ['); j = s.index('\n]\n', i)
line = ' (' + ', '.join(json.dumps(x, ensure_ascii=False) for x in row) + '),'
s = s[:j] + '\n' + line + s[j:]
open('build_log.py', 'w').write(s)

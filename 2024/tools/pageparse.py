import sys
from re import findall,DOTALL

with open(sys.argv[1] if (len(sys.argv) == 2) else 'input') as f:
    inp = f.read().strip()

print("in:",inp)
samples=findall(r"<pre><code>(.*)</code></pre>",inp,flags=DOTALL)
print("samples:",samples)
for s in samples:
    print("sample:\n",s,end="")
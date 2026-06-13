with open('/Users/sumitsaraswat/Portfolio/script.js', 'r') as f:
    js = f.read()

import re

# Remove the WebGL section
js = re.sub(r'// 9\. WEBGL THREE\.JS PARTICLE SYSTEM.*?catch \(err\) \{.*?\}\n', '', js, flags=re.DOTALL)

with open('/Users/sumitsaraswat/Portfolio/script.js', 'w') as f:
    f.write(js)

print("WebGL removed from script.js")

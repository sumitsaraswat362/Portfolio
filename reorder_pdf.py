import re

filepath = '/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html'
with open(filepath, 'r') as f:
    content = f.read()

# Split by the specific comments
parts = re.split(r'(?=<!-- PAGE \d: PROJECT \d \([^)]+\) -->)', content)

# parts[0] is up to Page 1
# parts[1] is Meta (currently Page 2)
# parts[2] is EcoNudge (currently Page 3)
# parts[3] is Annapurna (currently Page 4)
# parts[4] is CrisisGuard (currently Page 5)
# parts[5] is MedSafe (currently Page 6)
# parts[6] is Contact (currently Page 7)
# Wait, let's verify if the comments are exactly matching.
# Let's find them using re.split r'<!-- PAGE \d: PROJECT \d \([^)]+\) -->'

pattern = r'(<!-- PAGE \d: PROJECT \d \([^)]+\) -->)'
split_content = re.split(pattern, content)

# split_content will be:
# [0] Header/Page 1
# [1] <!-- PAGE 2: PROJECT 1 (META) -->
# [2] Meta HTML
# [3] <!-- PAGE 3: PROJECT 2 (ECONUDGE) -->
# [4] EcoNudge HTML
# [5] <!-- PAGE 4: PROJECT 3 (ANNAPURNA) -->
# [6] Annapurna HTML
# [7] <!-- PAGE 5: PROJECT 4 (CRISISGUARD) -->
# [8] CrisisGuard HTML
# [9] <!-- PAGE 6: PROJECT 5 (MEDSAFE) -->
# [10] MedSafe HTML

meta_marker = split_content[1]
meta_html = split_content[2]
econudge_marker = split_content[3]
econudge_html = split_content[4]
annapurna_marker = split_content[5]
annapurna_html = split_content[6]

# Update Annapurna (now Project 1, Page 2)
annapurna_marker = '<!-- PAGE 2: PROJECT 1 (ANNAPURNA) -->'
annapurna_html = annapurna_html.replace('3. Annapurna', '1. Annapurna')
annapurna_html = annapurna_html.replace('04 / ANNAPURNA', '02 / ANNAPURNA')
annapurna_html = annapurna_html.replace('<div class="meta-value">FarAway Hackathon Project</div>', '<div class="meta-value">Team Project</div>')

# Update Meta (now Project 2, Page 3)
meta_marker = '<!-- PAGE 3: PROJECT 2 (META) -->'
meta_html = meta_html.replace('1. Meta', '2. Meta')
meta_html = meta_html.replace('02 / META', '03 / META')

# Update EcoNudge (now Project 3, Page 4)
econudge_marker = '<!-- PAGE 4: PROJECT 3 (ECONUDGE) -->'
econudge_html = econudge_html.replace('2. EcoNudge', '3. EcoNudge')
econudge_html = econudge_html.replace('03 / ECONUDGE', '04 / ECONUDGE')

# Reassemble
new_content = (
    split_content[0] +
    annapurna_marker + annapurna_html +
    meta_marker + meta_html +
    econudge_marker + econudge_html +
    ''.join(split_content[7:])
)

with open(filepath, 'w') as f:
    f.write(new_content)

print("PDF Portfolio projects reordered successfully!")

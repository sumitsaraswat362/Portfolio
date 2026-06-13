import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'r') as f:
    content = f.read()

# Current Order: 1: Meta, 2: EcoNudge, 3: CrisisGuard, 4: MedSafe, 5: Annapurna
cover_split = content.split('<!-- PAGE 2: PROJECT 1 (META) -->')
header = cover_split[0]
rest = cover_split[1]

proj1_split = rest.split('<!-- PAGE 3: PROJECT 2 (ECONUDGE) -->')
meta = proj1_split[0]
rest = proj1_split[1]

proj2_split = rest.split('<!-- PAGE 4: PROJECT 3 (CRISISGUARD) -->')
econudge = proj2_split[0]
rest = proj2_split[1]

proj3_split = rest.split('<!-- PAGE 5: PROJECT 4 (MEDSAFE) -->')
crisisguard = proj3_split[0]
rest = proj3_split[1]

proj4_split = rest.split('<!-- PAGE 6: PROJECT 5 (ANNAPURNA) -->')
medsafe = proj4_split[0]
annapurna_footer = proj4_split[1]

annapurna_split = annapurna_footer.split('</body>')
annapurna = annapurna_split[0]
footer = '\n</body>' + annapurna_split[1]

def update_section(html, new_proj_num, new_page_num):
    # Regex to catch the current project number "X. Project Name"
    html = re.sub(r'<h1 class="project-title"(.*?)>\d+\.', rf'<h1 class="project-title"\1>{new_proj_num}.', html)
    # Regex to catch the current page number "0X / LABEL"
    html = re.sub(r'<div class="page-number">\d+ / (.*?)</div>', rf'<div class="page-number">{new_page_num} / \1</div>', html)
    return html

# New Order: 
# 1. Meta (stays 1, page 2)
# 2. EcoNudge (stays 2, page 3)
# 3. Annapurna (was 5, now 3, page 4)
# 4. CrisisGuard (was 3, now 4, page 5)
# 5. MedSafe (was 4, now 5, page 6)

new_meta = update_section(meta, '1', '02')
new_econudge = update_section(econudge, '2', '03')
new_annapurna = update_section(annapurna, '3', '04')
new_crisisguard = update_section(crisisguard, '4', '05')
new_medsafe = update_section(medsafe, '5', '06')

final_html = header + \
    '<!-- PAGE 2: PROJECT 1 (META) -->\n' + new_meta + \
    '<!-- PAGE 3: PROJECT 2 (ECONUDGE) -->\n' + new_econudge + \
    '<!-- PAGE 4: PROJECT 3 (ANNAPURNA) -->\n' + new_annapurna + \
    '<!-- PAGE 5: PROJECT 4 (CRISISGUARD) -->\n' + new_crisisguard + \
    '<!-- PAGE 6: PROJECT 5 (MEDSAFE) -->\n' + new_medsafe + \
    footer

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'w') as f:
    f.write(final_html)

print("Portfolio reordered successfully: Annapurna is now #3.")

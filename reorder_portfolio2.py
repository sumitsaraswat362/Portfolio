import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'r') as f:
    content = f.read()

# Current Order is 1: Meta, 2: MedSafe, 3: EcoNudge, 4: CrisisGuard, 5: Vocalis
cover_split = content.split('<!-- PAGE 2: PROJECT 1 (META) -->')
header = cover_split[0]
rest = cover_split[1]

proj1_split = rest.split('<!-- PAGE 3: PROJECT 2 (MEDSAFE) -->')
meta = proj1_split[0]
rest = proj1_split[1]

proj2_split = rest.split('<!-- PAGE 4: PROJECT 3 (ECONUDGE) -->')
medsafe = proj2_split[0]
rest = proj2_split[1]

proj3_split = rest.split('<!-- PAGE 5: PROJECT 4 (CRISISGUARD) -->')
econudge = proj3_split[0]
rest = proj3_split[1]

proj4_split = rest.split('<!-- PAGE 6: PROJECT 5 (VOCALIS) -->')
crisisguard = proj4_split[0]
vocalis_footer = proj4_split[1]

vocalis_split = vocalis_footer.split('</body>')
vocalis = vocalis_split[0]
footer = '\n</body>' + vocalis_split[1]

def update_section(html, new_proj_num, new_page_num):
    # Regex to catch the current project number "X. Project Name"
    html = re.sub(r'<h1 class="project-title"(.*?)>\d+\.', rf'<h1 class="project-title"\1>{new_proj_num}.', html)
    # Regex to catch the current page number "0X / LABEL"
    html = re.sub(r'<div class="page-number">\d+ / (.*?)</div>', rf'<div class="page-number">{new_page_num} / \1</div>', html)
    return html

# New Order: 
# 1. Meta (stays 1, page 2)
# 2. EcoNudge (was 3, now 2, page 3)
# 3. CrisisGuard (was 4, now 3, page 4)
# 4. MedSafe (was 2, now 4, page 5)
# 5. Vocalis (stays 5, page 6)

new_meta = update_section(meta, '1', '02')
new_econudge = update_section(econudge, '2', '03')
new_crisisguard = update_section(crisisguard, '3', '04')
new_medsafe = update_section(medsafe, '4', '05')
new_vocalis = update_section(vocalis, '5', '06')

final_html = header + \
    '<!-- PAGE 2: PROJECT 1 (META) -->\n' + new_meta + \
    '<!-- PAGE 3: PROJECT 2 (ECONUDGE) -->\n' + new_econudge + \
    '<!-- PAGE 4: PROJECT 3 (CRISISGUARD) -->\n' + new_crisisguard + \
    '<!-- PAGE 5: PROJECT 4 (MEDSAFE) -->\n' + new_medsafe + \
    '<!-- PAGE 6: PROJECT 5 (VOCALIS) -->\n' + new_vocalis + \
    footer

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'w') as f:
    f.write(final_html)

print("Portfolio reordered successfully.")

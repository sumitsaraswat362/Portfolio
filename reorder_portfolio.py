import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'r') as f:
    content = f.read()

# Split into parts
cover_split = content.split('<!-- PAGE 2: PROJECT 1 (APPLE) -->')
header = cover_split[0]
rest = cover_split[1]

proj1_split = rest.split('<!-- PAGE 3: PROJECT 2 (META HACKATHON COMBINED) -->')
vocalis = proj1_split[0]
rest = proj1_split[1]

proj2_split = rest.split('<!-- PAGE 4: PROJECT 3 (ECONUDGE SDK) -->')
meta = proj2_split[0]
rest = proj2_split[1]

proj3_split = rest.split('<!-- PAGE 5: PROJECT 4 (CRISISGUARD) -->')
econudge = proj3_split[0]
rest = proj3_split[1]

proj4_split = rest.split('<!-- PAGE 6: PROJECT 5 (MEDSAFE AI) -->')
crisisguard = proj4_split[0]
medsafe_footer = proj4_split[1]

medsafe_split = medsafe_footer.split('</body>')
medsafe = medsafe_split[0]
footer = '\n</body>' + medsafe_split[1]

# Function to update title and page number
def update_section(html, old_proj_num, new_proj_num, old_page_num, new_page_num, title_prefix, page_label):
    # Update project title number
    html = re.sub(rf'<h1 class="project-title"(.*?)>{old_proj_num}\.', rf'<h1 class="project-title"\1>{new_proj_num}.', html)
    # Update page number at bottom
    html = re.sub(rf'<div class="page-number">{old_page_num} / (.*?)</div>', rf'<div class="page-number">{new_page_num} / \1</div>', html)
    return html

# New Order: 
# 1. Meta (was 2, page 3 -> now 1, page 2)
# 2. MedSafe (was 5, page 6 -> now 2, page 3)
# 3. EcoNudge (was 3, page 4 -> now 3, page 4)
# 4. CrisisGuard (was 4, page 5 -> now 4, page 5)
# 5. Vocalis (was 1, page 2 -> now 5, page 6)

new_meta = update_section(meta, '2', '1', '02', '02', 'Meta OpenEnv', 'META OPENENV HACKATHON')
new_medsafe = update_section(medsafe, '5', '2', '05', '03', 'MedSafe AI', 'MEDSAFE AI')
new_econudge = update_section(econudge, '3', '3', '03', '04', 'EcoNudge SDK', 'ECONUDGE SDK')
new_crisisguard = update_section(crisisguard, '4', '4', '04', '05', 'CrisisGuard AI', 'CRISISGUARD AI')
new_vocalis = update_section(vocalis, '1', '5', '01', '06', 'Vocalis', 'VOCALIS (ACCESSIBILITY CONCEPT)')

# Add back the HTML comments for clarity
final_html = header + \
    '<!-- PAGE 2: PROJECT 1 (META) -->\n' + new_meta + \
    '<!-- PAGE 3: PROJECT 2 (MEDSAFE) -->\n' + new_medsafe + \
    '<!-- PAGE 4: PROJECT 3 (ECONUDGE) -->\n' + new_econudge + \
    '<!-- PAGE 5: PROJECT 4 (CRISISGUARD) -->\n' + new_crisisguard + \
    '<!-- PAGE 6: PROJECT 5 (VOCALIS) -->\n' + new_vocalis + \
    footer

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'w') as f:
    f.write(final_html)

print("Portfolio reordered successfully.")

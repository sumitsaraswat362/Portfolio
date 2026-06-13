import re

with open('/Users/sumitsaraswat/Portfolio/index.html', 'r') as f:
    html = f.read()

# Split the file at the start of the first project
start_marker = '<!-- PROJECT: CRISISGUARD -->'
parts = html.split(start_marker)
header = parts[0]
rest = start_marker + parts[1]

# Extract CrisisGuard
crisis_split = rest.split('<!-- PROJECT: ECONUDGE SDK -->')
crisisguard = crisis_split[0]
rest = '<!-- PROJECT: ECONUDGE SDK -->' + crisis_split[1]

# Extract EcoNudge
eco_split = rest.split('<!-- PROJECT: CLINICAL TRIAL AUDITOR -->')
econudge = eco_split[0]
rest = '<!-- PROJECT: CLINICAL TRIAL AUDITOR -->' + eco_split[1]

annapurna_html = """<!-- PROJECT: ANNAPURNA -->
    <section class="apple-section">
      <div class="apple-shell">
        <div class="swift-site-feature-grid reveal">
          <div>
            <p class="apple-eyebrow">Autonomous Cold-Chain AI</p>
            <h2 class="apple-display-section" style="margin-top: 16px;">Annapurna</h2>
            <p class="apple-subhead" style="margin-top: 16px;">An AI-powered logistics platform that detects refrigeration failures and actively reroutes cargo via an intelligent distress marketplace. Rescuing billions in food waste.</p>
            <div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 24px;">
              <span class="apple-tag">Next.js</span>
              <span class="apple-tag">Supabase</span>
              <span class="apple-tag">Edge AI</span>
              <span class="apple-tag">IoT / LoRaWAN</span>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px;">
              <a class="apple-button apple-button-primary" href="https://annapurna-alpha.vercel.app" target="_blank">Visit Site</a>
              <a class="apple-button apple-button-secondary" href="https://github.com/sumitsaraswat362/Annapurna" target="_blank">GitHub</a>
            </div>
          </div>
          <div class="spatial-card" data-cursor="project" data-href="https://annapurna-alpha.vercel.app">
            <div class="mac-window-wrapper">
              <div class="mac-titlebar">
                <div class="mac-traffic-lights">
                  <span class="light red"></span>
                  <span class="light yellow"></span>
                  <span class="light green"></span>
                </div>
                <div style="margin: 0 auto; font-size: 12px; color: var(--text-3);">annapurna.app</div>
              </div>
              <div class="mac-screen">
                <img src="Landing.png" alt="Annapurna Dashboard">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

"""

new_html = header + annapurna_html + econudge + crisisguard + rest

with open('/Users/sumitsaraswat/Portfolio/index.html', 'w') as f:
    f.write(new_html)

print("Web portfolio reordered successfully.")

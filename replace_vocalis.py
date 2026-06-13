import re

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'r') as f:
    content = f.read()

vocalis_start = '<!-- PAGE 6: PROJECT 5 (VOCALIS) -->'
parts = content.split(vocalis_start)

annapurna_html = """<!-- PAGE 6: PROJECT 5 (ANNAPURNA) -->
  <div class="page">
    <div class="decor-line"></div>
    <div class="image-col">
      <img src="annapurna_macbook.png" class="img-contain-landscape" alt="Annapurna UI">
    </div>
    <div class="content-col">
      <div class="project-header">
        <h1 class="project-title" style="font-size: 28px;">5. Annapurna — Autonomous Cold-Chain AI</h1>
      </div>

      <div class="meta-grid">
        <div class="meta-item">
          <div class="meta-label">Type</div>
          <div class="meta-value">FarAway Hackathon Project</div>
        </div>
        <div class="meta-item">
          <div class="meta-label">Role</div>
          <div class="meta-value">Lead Architect</div>
        </div>
      </div>

      <div class="section-title">One-Sentence Summary</div>
      <p class="content-text">An autonomous, AI-powered cold-chain logistics platform that detects refrigeration failures and actively reroutes cargo via an intelligent distress marketplace.</p>

      <div class="section-title">The Impact</div>
      <p class="content-text">In India, millions of dollars of perishable food rot in transit. Annapurna shifts logistics from passive tracking to active intervention. If a truck's fridge fails, edge sensors immediately alert the system, which predicts spoilage time and automatically reroutes the cargo to local buyers at a discounted rate, rescuing the food before it wastes.</p>

      <div class="section-title">What I Built</div>
      <p class="content-text">Leading a team of 4, I architected the core AI logic and designed the full Next.js/Supabase interface. The system features TinyML sensor integration, an AI Vision Cargo Scanner for quality checks, and fallback offline mesh networking via LoRaWAN. I focused on making complex fleet telemetry feel as elegant and readable as an Apple Health dashboard.</p>

      <div class="links">
        <a href="https://annapurna-alpha.vercel.app" class="link-item">Live Website ↗</a>
        <a href="https://github.com/sumitsaraswat362/Annapurna" class="link-item secondary">GitHub</a>
      </div>
      <div class="page-number">06 / ANNAPURNA (AUTONOMOUS LOGISTICS)</div>
    </div>
  </div>
</body>
</html>
"""

new_content = parts[0] + annapurna_html

with open('/Users/sumitsaraswat/Portfolio/SumitSaraswat_Portfolio_Academy.html', 'w') as f:
    f.write(new_content)

print("Vocalis replaced with Annapurna successfully.")

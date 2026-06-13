import re

with open('/Users/sumitsaraswat/Portfolio/style.css', 'r') as f:
    css = f.read()

# 1. Update Root Variables for "Frosted Silver" Titanium theme
new_root = """:root {
  /* ---------- TITANIUM / FROSTED SILVER MODE ---------- */
  --bg: #e5e5ea;
  --bg-elevated: #f2f2f7;
  --bg-card: rgba(255, 255, 255, 0.4);
  --text-1: #1c1c1e;
  --text-2: #86868b;
  --text-3: #aeaeb2;
  --accent: #007aff;
  --accent-hover: #0040dd;
  --border: rgba(255, 255, 255, 0.6);
  --border-hover: rgba(255, 255, 255, 0.9);
  
  /* Claymorphism & Liquid Glass Shadows */
  --shadow-card: 
    inset 2px 2px 5px rgba(255,255,255,0.8),
    inset -3px -3px 7px rgba(0,0,0,0.05),
    0 20px 40px rgba(0, 0, 0, 0.08);
  --shadow-card-hover: 
    inset 2px 2px 5px rgba(255,255,255,1),
    inset -3px -3px 7px rgba(0,0,0,0.03),
    0 30px 60px rgba(0, 0, 0, 0.15);
    
  --glass-bg: rgba(255, 255, 255, 0.35);
  --glass-blur: blur(50px) saturate(200%);
  --cursor-color: #000000;
  --loader-bg: #e5e5ea;
  --gradient-hero: linear-gradient(135deg, #1c1c1e 0%, #6e6e73 100%);
  --orb-opacity: 0.8;
  --nav-bg: rgba(255, 255, 255, 0.5);
  --toggle-bg: rgba(255, 255, 255, 0.4);
}"""

css = re.sub(r':root\s*\{.*?(?=\n\[data-theme="light"\])', new_root + '\n', css, flags=re.DOTALL)

# Remove the light mode override since the default IS the light frosted silver mode now.
css = re.sub(r'\[data-theme="light"\]\s*\{.*?\}\n', '', css, flags=re.DOTALL)

# 2. Add Bleeding Edge Scroll-Driven Animations to the cards
scroll_animations = """
/* ---------- BLEEDING EDGE SCROLL ANIMATIONS ---------- */
@keyframes scroll-scale-fade {
  from {
    opacity: 0;
    transform: scale(0.9) translateY(100px);
  }
  to {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.apple-section, .bento-tile, .petros-card {
  animation: scroll-scale-fade linear both;
  animation-timeline: view();
  animation-range: entry 10% cover 30%;
}

/* Remove old JS reveal classes to let CSS take over */
.reveal { opacity: 1; transform: none; transition: none; }
"""
css += scroll_animations

# 3. Update Nav and Buttons to be Liquid Glass/Claymorphic
nav_buttons = """
/* ===================================================================
   LIQUID GLASS & CLAYMORPHIC BUTTONS
   =================================================================== */
.apple-nav-link,
.apple-button {
  display: inline-flex;
  align-items: center; justify-content: center;
  border-radius: 980px;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
  cursor: none;
  
  /* Rest State: Frosted Silver Clay */
  background: rgba(255, 255, 255, 0.4);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.8);
  color: var(--text-1);
  
  /* Claymorphism */
  box-shadow: 
    inset 2px 2px 4px rgba(255, 255, 255, 0.9), 
    inset -2px -2px 4px rgba(0, 0, 0, 0.05), 
    0 8px 20px rgba(0, 0, 0, 0.05);
}

.apple-nav-link:hover,
.apple-nav-link.active,
.apple-button:hover {
  background: rgba(255, 255, 255, 0.7);
  transform: translateY(-2px) scale(1.02);
  box-shadow: 
    inset 2px 2px 6px rgba(255, 255, 255, 1), 
    inset -2px -2px 6px rgba(0, 0, 0, 0.02), 
    0 15px 30px rgba(0, 0, 0, 0.1);
}

.apple-button-primary {
  background: var(--accent);
  color: #fff;
  border-color: rgba(255,255,255,0.3);
  box-shadow: 
    inset 2px 2px 5px rgba(255,255,255,0.4),
    inset -2px -2px 5px rgba(0,0,0,0.2),
    0 10px 20px rgba(0, 122, 255, 0.3);
}
.apple-button-primary:hover {
  background: var(--accent-hover);
  color: #fff;
  box-shadow: 
    inset 2px 2px 5px rgba(255,255,255,0.5),
    inset -2px -2px 5px rgba(0,0,0,0.3),
    0 15px 30px rgba(0, 122, 255, 0.4);
}
"""

css = re.sub(r'/\* ===================================================================\s*LIQUID GLASS BUTTONS.*?/\* Theme Toggle \*/', nav_buttons + '\n/* Theme Toggle */', css, flags=re.DOTALL)

# 4. Make Orbs Frosted Silver/Titanium themed
orbs = """
.orb-1 {
  width: 60vw; height: 60vw;
  background: radial-gradient(circle, rgba(142, 142, 147, 0.5) 0%, transparent 70%);
  top: -15vh; left: -15vw;
}
.orb-2 {
  width: 50vw; height: 50vw;
  background: radial-gradient(circle, rgba(209, 209, 214, 0.8) 0%, transparent 70%);
  bottom: -20vh; right: -10vw;
  animation-delay: -8s;
}
.orb-3 {
  width: 40vw; height: 40vw;
  background: radial-gradient(circle, rgba(229, 229, 234, 0.9) 0%, transparent 70%);
  top: 35%; left: 35%;
  animation-delay: -16s;
}
"""
css = re.sub(r'\.orb-1 \{.*?(?=@keyframes orb-float)', orbs, css, flags=re.DOTALL)

with open('/Users/sumitsaraswat/Portfolio/style.css', 'w') as f:
    f.write(css)

print("style.css rewritten for Frosted Silver theme.")

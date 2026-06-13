with open('/Users/sumitsaraswat/Portfolio/script.js', 'a') as f:
    f.write("""
  // ===================================================================
  // 9. SKEUOMORPHIC 3D TILT EFFECT (APPLE HIG INTERACTIVE)
  // ===================================================================
  const cards = document.querySelectorAll('.spatial-card, .bento-tile, .petros-card, .apple-profile-card, .hero-code');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -5; // max 5 deg tilt
      const rotateY = ((x - centerX) / centerX) * 5;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
      card.style.transition = 'none';
      
      // Dynamic glare effect
      let glare = card.querySelector('.glare');
      if (!glare) {
        glare = document.createElement('div');
        glare.className = 'glare';
        glare.style.position = 'absolute';
        glare.style.top = '0';
        glare.style.left = '0';
        glare.style.width = '100%';
        glare.style.height = '100%';
        glare.style.pointerEvents = 'none';
        glare.style.borderRadius = 'inherit';
        glare.style.zIndex = '10';
        card.appendChild(glare);
      }
      
      const px = (x / rect.width) * 100;
      const py = (y / rect.height) * 100;
      glare.style.background = `radial-gradient(circle at ${px}% ${py}%, rgba(255,255,255,0.4) 0%, transparent 60%)`;
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      card.style.transition = 'transform 0.5s cubic-bezier(0.25, 1, 0.5, 1)';
      
      const glare = card.querySelector('.glare');
      if (glare) glare.style.background = 'none';
    });
  });
""")

print("script.js updated with 3D tilt tracking.")

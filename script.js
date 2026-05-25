document.addEventListener("DOMContentLoaded", () => {
  // Register GSAP Plugins
  gsap.registerPlugin(ScrollTrigger, TextPlugin);

  // 1. Navigation Active State Handling
  const sections = ['home', 'work', 'about'];
  const links = document.querySelectorAll('[data-nav]');

  function updateNav() {
    let current = '';
    
    sections.forEach(secId => {
      const el = document.getElementById(secId);
      if (el) {
        const rect = el.getBoundingClientRect();
        // Check if top of section is near the top of the viewport
        if (rect.top <= 300 && rect.bottom >= 300) {
          current = secId;
        }
      }
    });

    links.forEach(link => {
      if (link.dataset.nav === current) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  window.addEventListener('scroll', updateNav, { passive: true });
  updateNav(); // Init

  // 2. Dynamic Typewriter Effect for Skills
  const skills = ["AI Engineer", "Full-Stack Developer", "Healthcare Innovator", "Privacy Advocate"];
  let cursorTl = gsap.timeline({ repeat: -1 }).to('.cursor', { opacity: 0, duration: 0.5, ease: "steps(1)" });
  
  let masterTl = gsap.timeline({ repeat: -1, delay: 1 });
  skills.forEach(skill => {
    let tl = gsap.timeline({ repeat: 1, yoyo: true, repeatDelay: 2 });
    tl.to("#typewriter-text", { duration: 1.5, text: skill, ease: "none" });
    masterTl.add(tl);
  });

  // 3. Hero Text Slide-In Reveal
  gsap.from("#hero-headline", {
    y: 100,
    opacity: 0,
    duration: 1.2,
    ease: "power4.out",
    delay: 0.2
  });

  gsap.from(".hero-content .apple-subhead, .hero-content .apple-button", {
    y: 30,
    opacity: 0,
    duration: 1,
    stagger: 0.15,
    ease: "power3.out",
    delay: 0.6
  });

  gsap.from(".swift-site-panel-stack", {
    x: 40,
    opacity: 0,
    duration: 1.2,
    ease: "power3.out",
    delay: 0.8
  });

  // 4. Mac Window Scroll Reveals
  const macWindows = document.querySelectorAll('.gsap-mac-window');
  
  macWindows.forEach(window => {
    gsap.from(window, {
      scrollTrigger: {
        trigger: window,
        start: "top 85%", // trigger when top of element hits 85% of viewport
        toggleActions: "play none none reverse"
      },
      y: 50,
      opacity: 0,
      scale: 0.96,
      duration: 1,
      ease: "power3.out"
    });
  });

  // 5. Text Side Reveals (for Work and About sections)
  const textBlocks = document.querySelectorAll('.swift-site-feature-grid > div:not(.gsap-mac-window), .about-grid > div');
  
  textBlocks.forEach(block => {
    gsap.from(block, {
      scrollTrigger: {
        trigger: block,
        start: "top 85%",
        toggleActions: "play none none reverse"
      },
      y: 30,
      opacity: 0,
      duration: 1,
      ease: "power3.out"
    });
  });

});

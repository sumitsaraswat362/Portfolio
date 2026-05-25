document.addEventListener("DOMContentLoaded", () => {
  gsap.registerPlugin(ScrollTrigger, TextPlugin);

  // ===================================================================
  // 1. LIGHT/DARK THEME TOGGLE
  // ===================================================================
  const toggle = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("theme") || "dark";
  if (savedTheme === "light") document.documentElement.setAttribute("data-theme", "light");

  toggle.addEventListener("click", () => {
    const isLight = document.documentElement.getAttribute("data-theme") === "light";
    const newTheme = isLight ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", newTheme === "light" ? "light" : "");
    if (newTheme === "light") {
      document.documentElement.setAttribute("data-theme", "light");
    } else {
      document.documentElement.removeAttribute("data-theme");
    }
    localStorage.setItem("theme", newTheme);

    // Update WebGL particle colors
    if (window.particleMaterial) {
      window.particleMaterial.color.setHex(newTheme === "light" ? 0x0071e3 : 0x2997ff);
      window.particleMaterial.opacity = newTheme === "light" ? 0.3 : 0.6;
    }
  });

  // ===================================================================
  // 2. SMART CUSTOM CURSOR
  // ===================================================================
  const dot = document.querySelector(".cursor-dot");
  const ring = document.querySelector(".cursor-ring");
  let mouseX = 0, mouseY = 0;
  let ringX = 0, ringY = 0;

  document.addEventListener("mousemove", (e) => {
    mouseX = e.clientX;
    mouseY = e.clientY;
    gsap.to(dot, { x: mouseX, y: mouseY, duration: 0.1, ease: "power2.out" });
  });

  // Smooth ring follow
  function animateRing() {
    ringX += (mouseX - ringX) * 0.12;
    ringY += (mouseY - ringY) * 0.12;
    ring.style.left = ringX + "px";
    ring.style.top = ringY + "px";
    requestAnimationFrame(animateRing);
  }
  animateRing();

  // Cursor morph: project cards
  document.querySelectorAll("[data-cursor='project']").forEach(el => {
    el.addEventListener("mouseenter", () => {
      ring.classList.add("hover-project");
      dot.style.opacity = "0";
    });
    el.addEventListener("mouseleave", () => {
      ring.classList.remove("hover-project");
      dot.style.opacity = "1";
    });
  });

  // Cursor morph: links and buttons
  document.querySelectorAll("a, button, .apple-nav-link, .apple-button, .expertise-pill").forEach(el => {
    el.addEventListener("mouseenter", () => ring.classList.add("hover-link"));
    el.addEventListener("mouseleave", () => ring.classList.remove("hover-link"));
  });

  // ===================================================================
  // 3. CINEMATIC LOADER
  // ===================================================================
  const loaderTl = gsap.timeline();
  loaderTl
    .to(".loader-text", { opacity: 1, filter: "blur(0px)", duration: 0.8, ease: "power2.out" })
    .to(".loader-sub", { opacity: 1, duration: 0.5, ease: "power2.out" }, "-=0.3")
    .to(".loader-text, .loader-sub", { opacity: 0, filter: "blur(8px)", duration: 0.6, delay: 0.6, ease: "power2.in" })
    .to("#loader", { yPercent: -100, duration: 0.9, ease: "power4.inOut" })
    .set("#loader", { display: "none" });

  // ===================================================================
  // 4. NAVIGATION
  // ===================================================================
  const sections = ["home", "work", "about"];
  const navLinks = document.querySelectorAll("[data-nav]");

  function updateNav() {
    let current = "";
    sections.forEach(secId => {
      const el = document.getElementById(secId);
      if (el) {
        const rect = el.getBoundingClientRect();
        if (rect.top <= 300 && rect.bottom >= 300) current = secId;
      }
    });
    navLinks.forEach(link => {
      link.classList.toggle("active", link.dataset.nav === current);
    });
  }
  window.addEventListener("scroll", updateNav, { passive: true });
  updateNav();

  // Magnetic nav buttons
  document.querySelectorAll(".apple-nav-link, .theme-toggle").forEach(link => {
    link.addEventListener("mousemove", (e) => {
      const rect = link.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      gsap.to(link, { x: x * 0.35, y: y * 0.35, duration: 0.3, ease: "power2.out" });
    });
    link.addEventListener("mouseleave", () => {
      gsap.to(link, { x: 0, y: 0, duration: 0.6, ease: "elastic.out(1, 0.3)" });
    });
  });

  // ===================================================================
  // 5. TYPEWRITER + HERO ANIMATIONS
  // ===================================================================
  const skills = ["AI Engineer", "Full-Stack Developer", "Healthcare Innovator", "Privacy Advocate"];
  gsap.timeline({ repeat: -1 }).to(".cursor", { opacity: 0, duration: 0.5, ease: "steps(1)" });

  const masterTl = gsap.timeline({ repeat: -1, delay: 3.5 });
  skills.forEach(skill => {
    const tl = gsap.timeline({ repeat: 1, yoyo: true, repeatDelay: 2 });
    tl.to("#typewriter-text", { duration: 1.5, text: skill, ease: "none" });
    masterTl.add(tl);
  });

  // Hero reveals (after loader)
  const heroHeadline = document.getElementById("hero-headline");
  gsap.set(heroHeadline, { opacity: 0, y: 80 });
  gsap.to(heroHeadline, { opacity: 1, y: 0, duration: 1.2, ease: "power4.out", delay: 2.6 });

  gsap.from(".hero-content .apple-eyebrow", { y: 20, opacity: 0, duration: 0.8, ease: "power3.out", delay: 2.4 });
  gsap.from(".hero-content .apple-subhead, .hero-content .apple-button", {
    y: 25, opacity: 0, duration: 1, stagger: 0.12, ease: "power3.out", delay: 2.9
  });
  gsap.from(".swift-site-panel-stack", { x: 30, opacity: 0, duration: 1.2, ease: "power3.out", delay: 3.1 });

  // ===================================================================
  // 6. SCROLL-DRIVEN REVEALS (IntersectionObserver)
  // ===================================================================
  const revealElements = document.querySelectorAll(".reveal");
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });
  revealElements.forEach(el => revealObserver.observe(el));

  // ===================================================================
  // 6b. GSAP SCROLL ANIMATIONS FOR PROJECT WINDOWS
  // ===================================================================
  document.querySelectorAll(".spatial-card").forEach(card => {
    gsap.from(card, {
      scrollTrigger: {
        trigger: card,
        start: "top 88%",
        toggleActions: "play none none reverse"
      },
      y: 60,
      opacity: 0,
      scale: 0.94,
      duration: 1.1,
      ease: "power3.out"
    });
  });

  // Text blocks alongside project cards
  document.querySelectorAll(".swift-site-feature-grid > div:not(.spatial-card)").forEach(block => {
    gsap.from(block, {
      scrollTrigger: {
        trigger: block,
        start: "top 88%",
        toggleActions: "play none none reverse"
      },
      y: 40,
      opacity: 0,
      duration: 1,
      ease: "power3.out"
    });
  });

  // ===================================================================
  // 7. SCROLL-SCRUBBED KINETIC TYPOGRAPHY
  // ===================================================================
  // Delay this so it doesn't conflict with the initial reveal
  setTimeout(() => {
    gsap.to("#hero-headline", {
      scrollTrigger: {
        trigger: ".apple-hero",
        start: "80px top",
        end: "bottom top",
        scrub: 1
      },
      opacity: 0.15,
      scale: 0.96,
      y: -20,
      ease: "none"
    });

    // Also fade out the subhead and buttons on scroll
    gsap.to(".hero-content .apple-subhead, .hero-content .apple-eyebrow", {
      scrollTrigger: {
        trigger: ".apple-hero",
        start: "100px top",
        end: "bottom top",
        scrub: 1
      },
      opacity: 0,
      y: -15,
      ease: "none"
    });
  }, 4000);

  // ===================================================================
  // 7b. CLICKABLE SPATIAL CARDS — Open live demos
  // ===================================================================
  document.querySelectorAll(".spatial-card[data-href]").forEach(card => {
    card.style.cursor = "none";
    card.addEventListener("click", () => {
      window.open(card.dataset.href, "_blank");
    });
  });

  // ===================================================================
  // 8. SPATIAL 3D TILT (VisionPro Depth)
  // ===================================================================
  document.querySelectorAll(".spatial-card").forEach(card => {
    const inner = card.querySelector(".mac-window-wrapper, .certificate-wrapper");
    if (!inner) return;

    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;

      gsap.to(inner, {
        rotateX, rotateY,
        duration: 0.4,
        ease: "power2.out",
        transformPerspective: 800
      });

      // Move the glare
      const glareX = (x / rect.width) * 100;
      const glareY = (y / rect.height) * 100;
      inner.style.setProperty("--glare-x", glareX + "%");
      inner.style.setProperty("--glare-y", glareY + "%");
    });

    card.addEventListener("mouseleave", () => {
      gsap.to(inner, {
        rotateX: 0, rotateY: 0,
        duration: 0.7,
        ease: "elastic.out(1, 0.5)"
      });
    });
  });

  // ===================================================================
  // 9. WEBGL THREE.JS PARTICLE SYSTEM
  // ===================================================================
  try {
    const canvas = document.getElementById("webgl-canvas");
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas, alpha: true, antialias: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

    // Particles
    const particleCount = 600;
    const geometry = new THREE.BufferGeometry();
    const positions = new Float32Array(particleCount * 3);
    const velocities = [];

    for (let i = 0; i < particleCount; i++) {
      positions[i * 3] = (Math.random() - 0.5) * 20;
      positions[i * 3 + 1] = (Math.random() - 0.5) * 20;
      positions[i * 3 + 2] = (Math.random() - 0.5) * 20;
      velocities.push({
        x: (Math.random() - 0.5) * 0.005,
        y: (Math.random() - 0.5) * 0.005,
        z: (Math.random() - 0.5) * 0.005
      });
    }
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));

    const isLight = savedTheme === "light";
    const material = new THREE.PointsMaterial({
      color: isLight ? 0x0071e3 : 0x2997ff,
      size: 0.04,
      transparent: true,
      opacity: isLight ? 0.3 : 0.6,
      blending: THREE.AdditiveBlending,
      sizeAttenuation: true
    });
    window.particleMaterial = material;

    const particles = new THREE.Points(geometry, material);
    scene.add(particles);

    // Lines connecting nearby particles
    const lineGeometry = new THREE.BufferGeometry();
    const lineMaterial = new THREE.LineBasicMaterial({
      color: isLight ? 0x0071e3 : 0x2997ff,
      transparent: true,
      opacity: 0.08,
      blending: THREE.AdditiveBlending
    });
    window.lineMaterial = lineMaterial;
    const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
    scene.add(lines);

    camera.position.z = 8;

    let mouse3D = { x: 0, y: 0 };
    document.addEventListener("mousemove", (e) => {
      mouse3D.x = (e.clientX / window.innerWidth) * 2 - 1;
      mouse3D.y = -(e.clientY / window.innerHeight) * 2 + 1;
    });

    function animateWebGL() {
      requestAnimationFrame(animateWebGL);

      const pos = geometry.attributes.position.array;
      const linePositions = [];

      for (let i = 0; i < particleCount; i++) {
        pos[i * 3] += velocities[i].x;
        pos[i * 3 + 1] += velocities[i].y;
        pos[i * 3 + 2] += velocities[i].z;

        // Boundary wrap
        for (let j = 0; j < 3; j++) {
          if (pos[i * 3 + j] > 10) pos[i * 3 + j] = -10;
          if (pos[i * 3 + j] < -10) pos[i * 3 + j] = 10;
        }

        // Connect nearby particles
        for (let k = i + 1; k < particleCount; k++) {
          const dx = pos[i * 3] - pos[k * 3];
          const dy = pos[i * 3 + 1] - pos[k * 3 + 1];
          const dz = pos[i * 3 + 2] - pos[k * 3 + 2];
          const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);
          if (dist < 1.5) {
            linePositions.push(pos[i * 3], pos[i * 3 + 1], pos[i * 3 + 2]);
            linePositions.push(pos[k * 3], pos[k * 3 + 1], pos[k * 3 + 2]);
          }
        }
      }

      geometry.attributes.position.needsUpdate = true;
      lineGeometry.setAttribute("position", new THREE.BufferAttribute(new Float32Array(linePositions), 3));

      // Gentle mouse reaction
      particles.rotation.x += 0.0005;
      particles.rotation.y += 0.0008;
      particles.rotation.x += mouse3D.y * 0.0003;
      particles.rotation.y += mouse3D.x * 0.0003;
      lines.rotation.copy(particles.rotation);

      renderer.render(scene, camera);
    }
    animateWebGL();

    window.addEventListener("resize", () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    });
  } catch (err) {
    console.warn("WebGL not supported, falling back to CSS background:", err);
  }
});

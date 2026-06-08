// ── Navigation ──
document.addEventListener('DOMContentLoaded', () => {
  // Active nav link
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Mobile toggle
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggle && navLinks) {
    toggle.addEventListener('click', () => {
      navLinks.classList.toggle('open');
    });
  }

  // Scroll-based navbar shadow
  window.addEventListener('scroll', () => {
    const nav = document.querySelector('.navbar');
    if (nav) {
      nav.style.boxShadow = window.scrollY > 20 
        ? '0 4px 32px rgba(0,0,0,0.4)' : 'none';
    }
  });
});

// ── Plotly default config ──
const PLOTLY_CONFIG = {
  responsive: true,
  displayModeBar: false,
  scrollZoom: false
};

const PLOTLY_LAYOUT_BASE = {
  paper_bgcolor: 'transparent',
  plot_bgcolor: 'transparent',
  font: { family: 'DM Sans, sans-serif', color: '#94A3B8', size: 12 },
  margin: { t: 20, r: 20, b: 50, l: 60 },
  xaxis: {
    gridcolor: 'rgba(255,255,255,0.05)',
    linecolor: 'rgba(255,255,255,0.08)',
    tickcolor: 'transparent',
    tickfont: { color: '#64748B', size: 11 }
  },
  yaxis: {
    gridcolor: 'rgba(255,255,255,0.05)',
    linecolor: 'rgba(255,255,255,0.08)',
    tickcolor: 'transparent',
    tickfont: { color: '#64748B', size: 11 }
  },
  legend: { 
    bgcolor: 'transparent', 
    font: { color: '#94A3B8', size: 12 },
    orientation: 'h',
    y: -0.15
  }
};

// ── Fetch helper ──
async function fetchData(file) {
  const base = getBasePath();
  const res = await fetch(`${base}data/${file}`);
  return res.json();
}

function getBasePath() {
  const path = window.location.pathname;
  if (path.includes('/pages/')) return '../';
  return './';
}

// ── Counter animation ──
function animateCounter(el, target, duration = 1500, prefix = '', suffix = '') {
  const start = performance.now();
  const update = (time) => {
    const elapsed = time - start;
    const progress = Math.min(elapsed / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.floor(eased * target);
    el.textContent = prefix + current.toLocaleString() + suffix;
    if (progress < 1) requestAnimationFrame(update);
  };
  requestAnimationFrame(update);
}

// ── Intersection observer for animations ──
function observeAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.animate-on-scroll').forEach(el => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
}

document.addEventListener('DOMContentLoaded', observeAnimations);

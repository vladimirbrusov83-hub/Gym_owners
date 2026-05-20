// Copy buttons for prompt blocks
document.querySelectorAll('.prompt-block').forEach(block => {
  const pre = block.querySelector('pre');
  if (!pre) return;

  const btn = document.createElement('button');
  btn.className = 'copy-btn';
  btn.textContent = 'Copy';
  block.appendChild(btn);

  btn.addEventListener('click', () => {
    navigator.clipboard.writeText(pre.textContent.trim()).then(() => {
      btn.textContent = 'Copied';
      btn.classList.add('copied');
      setTimeout(() => {
        btn.textContent = 'Copy';
        btn.classList.remove('copied');
      }, 2000);
    });
  });
});

// Mobile nav toggle
const hamburger = document.querySelector('.nav-hamburger');
const mobileMenu = document.querySelector('.mobile-menu');

if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
  });
}

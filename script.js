const particles = document.querySelector('.particles');
let particleCount = 0;

function createParticle() {
  if (particleCount < 20) {
    const particle = document.createElement('span');
    particles.appendChild(particle);

    const size = Math.random() * 10;

    particle.style.width = `${size}px`;
    particle.style.height = `${size}px`;

    particle.style.left = `${Math.random() * 100}vw`;
    particle.style.animationDuration = `${Math.random() * 2 + 1}s`;

    particleCount++;
  }
}

setInterval(createParticle, 100);

// Додайте цю функцію, щоб зупинити створення частинок
function stopParticles() {
  clearInterval(particleInterval);
}

// Викликайте stopParticles() при необхідності зупинити створення частинок

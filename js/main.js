document.addEventListener('DOMContentLoaded', () => {
  // Мобильное меню
  const nav = document.querySelector('.nav');
  const toggle = document.querySelector('.nav-toggle');
  toggle.addEventListener('click', () => {
    nav.classList.toggle('open');
  });

  // Плавная прокрутка
  document.querySelectorAll('nav a').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      // закрыть меню на мобилках
      if (nav.classList.contains('open')) nav.classList.remove('open');
    });
  });

  // Анимация секций при скролле
  const sections = document.querySelectorAll('.section');
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.2 });

  sections.forEach(sec => io.observe(sec));

  // Раскрытие деталей участников
  document.querySelectorAll('.member-toggle').forEach(btn => {
    btn.addEventListener('click', () => {
      const parent = btn.closest('.member');
      parent.classList.toggle('open');
    });
  });

  // Показ секций
  function showSection(sectionId) {
    document.querySelectorAll('.content-section').forEach(section => {
      section.classList.remove('active');
    });

    const target = document.getElementById(sectionId);
    if (target) target.classList.add('active');
  }

  // Показ подробностей о ресурсе
  function showDetails(id) {
    document.querySelectorAll('.member-details').forEach(detail => {
      detail.style.display = 'none';
    });

    const element = document.getElementById(id);
    if (element) element.style.display = 'block';
  }
});

(() => {
  'use strict';
  const $ = selector => document.querySelector(selector);
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let moving = !reduced.matches;
  const motion = $('#motion');
  const setMotion = value => {
    moving = value;
    document.body.classList.toggle('motion-off', !value);
    motion.setAttribute('aria-pressed', String(value));
    motion.innerHTML = `Motion ${value ? 'on' : 'off'} <span>${value ? '◉' : '○'}</span>`;
    window.dispatchEvent(new CustomEvent('portfolioMotion', {detail:value}));
  };
  document.body.classList.toggle('motion-off', !moving);
  motion.setAttribute('aria-pressed', String(moving));
  if (!moving) motion.innerHTML = 'Motion off <span>○</span>';
  motion.addEventListener('click', () => setMotion(!moving));
  reduced.addEventListener('change', event => setMotion(!event.matches));
  $('#year').textContent = new Date().getFullYear();

  const menu = $('#menu'), menuButton = $('#menu-button');
  const closeMenu = () => {
    menu.hidden = true;
    document.body.classList.remove('menu-open');
    document.body.style.overflow = '';
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.innerHTML = 'Index <span>＋</span>';
  };
  menuButton.addEventListener('click', () => {
    if (!menu.hidden) { closeMenu(); return; }
    menu.hidden = false;
    document.body.classList.add('menu-open');
    document.body.style.overflow = 'hidden';
    menuButton.setAttribute('aria-expanded', 'true');
    menuButton.innerHTML = 'Close <span>×</span>';
    menu.querySelector('a').focus();
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', event => {
    if (menu.hidden) return;
    if (event.key === 'Escape') { closeMenu(); menuButton.focus(); }
    if (event.key === 'Tab') {
      const focusable = [menuButton, ...menu.querySelectorAll('a')];
      const i = focusable.indexOf(document.activeElement);
      if (event.shiftKey && i <= 0) {event.preventDefault(); focusable.at(-1).focus();}
      else if (!event.shiftKey && i === focusable.length - 1) {event.preventDefault(); menuButton.focus();}
    }
  });
  const cursor = $('.cursor');
  if (window.matchMedia('(pointer:fine)').matches) {
    document.addEventListener('pointermove', event => {
      cursor.style.opacity = '1'; cursor.style.left = event.clientX+'px'; cursor.style.top = event.clientY+'px';
    });
    document.addEventListener('pointerover', event => {
      const target = event.target.closest('[data-cursor]');
      cursor.classList.toggle('big', !!target);
      if (target) cursor.querySelector('span').textContent = target.dataset.cursor;
    });
    document.addEventListener('pointerout', event => {if (!event.relatedTarget) cursor.style.opacity = '0';});
  }
  const reveal = new IntersectionObserver(entries => entries.forEach(entry => {
    if (entry.isIntersecting) {entry.target.classList.add('seen'); reveal.unobserve(entry.target);}
  }), {threshold:0.1});
  document.querySelectorAll('[data-reveal]').forEach(node => reveal.observe(node));

  const raw = 'https://raw.githubusercontent.com/emmanuelacheampong0/emmanuelacheampong0/main/assets/projects/';
  const repo = 'https://github.com/emmanuelacheampong0/emmanuelacheampong0';
  const projects = [
    {title:'Small game.<br>Big learning.', category:'Python foundations / browser playable', description:'Roshambo turns a familiar ruleset into reusable functions, fair decisions, randomized computer behavior and a complete little game.', learning:'Built to understand functions, loops, debugging and incremental testing.', demo:'games/roshambo/', action:'Play Roshambo', source:repo+'/tree/main/games/roshambo', status:'Playable · Python + browser edition', color:'#201b31', preview:'<div class="rps-preview" aria-label="Roshambo game preview"><span class="preview-label">ROSHAMBO / PLAY</span><div class="rps-discs"><span>R</span><span>P</span><span>S</span></div><span class="preview-caption">A familiar ruleset. A new way to learn.</span></div>'},
    {title:'Choose your length.<br>Find the word.', category:'Neddle / word logic & playful systems', description:'Pick a word length from 4 to 8 letters, then find the hidden word in six guesses. Clear feedback and replay keep each round easy to follow.', learning:'Built to understand strings, sequences, game state and duplicate-letter edge cases.', demo:'games/neddle/', action:'Play Neddle', source:repo+'/tree/main/games/neddle', status:'Playable · 4–8 letters · six guesses', color:'#18362b', preview:'<div class="word-preview" aria-label="Neddle preview: choose a word length from four to eight letters"><span class="preview-label">4–8 LETTERS / SIX TRIES</span><span class="word-title">Neddle.</span><div class="word-row"><span>4</span><span>5</span><span>6</span><span>7</span><span>8</span></div><span class="preview-caption">Choose your challenge.</span></div>'},
    {title:'Our stories.<br>Our power.', category:'Black Arts Movement / digital exhibition', description:'An immersive visual story about Black identity, memory and resistance, bringing my Ghanaian/Akan perspective into a digital collage and interactive exhibition.', learning:'Exploring composition, cultural storytelling and Adinkra as a visual language of values and memory.', demo:'projects/black-arts/', action:'Explore the movement', source:'https://github.com/emmanuelacheampong0/Black-Arts-Movement', status:'Live exhibition · Photoshop + HTML', color:'#3b2025', preview:`<img src="${raw}black-arts-collage.jpg" alt="Digital collage: Our People, Our Stories, Our Art, Our Power">`},
    {title:'Make care<br>feel clear.', category:'Voima / product design & health communication', description:'Brand systems, campaign visuals and product communication for a youth-led sickle-cell initiative and its emerging AI companion concept.', learning:'Connecting audience needs, trustworthy messaging, visual consistency, early-user recruitment and engagement feedback.', demo:'projects/voima/', action:'View the case study', source:'https://github.com/emmanuelacheampong0/Voima-Project', status:'Case study · Social Media & Engagement Lead', color:'#3e2026', preview:`<img src="${raw}voima-brand.jpg" alt="Voima brand banner, a youth-led sickle-cell initiative">`}
  ];
  let active = -1, manualUntil = 0;
  const work = $('#work'), stage = $('.stage'), preview = $('#project-preview');
  const showProject = index => {
    if (index === active) return;
    active = index; const p = projects[index];
    $('#project-title').innerHTML = p.title;
    $('#project-category').textContent = p.category;
    $('#project-description').textContent = p.description;
    $('#project-learning').textContent = p.learning;
    $('#project-demo').href = p.demo;
    $('#project-demo').innerHTML = p.action+' <span>↗</span>';
    $('#project-source').href = p.source;
    $('#art-tag').textContent = p.status;
    $('.stage-number').textContent = String(index+1).padStart(2,'0')+' — 04';
    stage.style.backgroundColor = p.color;
    preview.innerHTML = p.preview;
    preview.classList.remove('changed');
    void preview.offsetWidth;
    preview.classList.add('changed');
    document.querySelectorAll('[data-project]').forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.project) === index)));
  };
  showProject(0);
  document.querySelectorAll('[data-project]').forEach(button => button.addEventListener('click', () => {
    const index = Number(button.dataset.project); showProject(index); manualUntil = Date.now()+1300;
    const range = Math.max(1, work.offsetHeight - window.innerHeight);
    window.scrollTo({top:work.offsetTop + range*((index+.12)/4), behavior:moving?'smooth':'instant'});
  }));
  let scrollQueued = false;
  const onScroll = () => {
    scrollQueued = false;
    $('header').classList.toggle('scrolled', window.scrollY > 35);
    if (Date.now() < manualUntil) return;
    const range = Math.max(1, work.offsetHeight-window.innerHeight);
    const progress = Math.max(0,Math.min(.999,(window.scrollY-work.offsetTop)/range));
    if (window.scrollY >= work.offsetTop-100 && window.scrollY < work.offsetTop+work.offsetHeight) showProject(Math.floor(progress*4));
  };
  window.addEventListener('scroll', () => {if (!scrollQueued) {scrollQueued = true; requestAnimationFrame(onScroll);}}, {passive:true});
  window.addEventListener('resize', onScroll); onScroll();
  $('#project-art').addEventListener('pointermove', event => {
    if (!moving || event.pointerType === 'touch') return;
    const r = event.currentTarget.getBoundingClientRect();
    preview.style.transform = `rotate(-3deg) rotateY(${(event.clientX-r.left-r.width/2)/r.width*12}deg) rotateX(${-(event.clientY-r.top-r.height/2)/r.height*10}deg)`;
  });
  $('#project-art').addEventListener('pointerleave', () => {preview.style.transform='';});
  let shape = 0;
  const setShape = value => {
    shape = value;
    $('.sculpture').dataset.shape = String(value);
    document.querySelectorAll('[data-shape]').forEach(button => button.setAttribute('aria-pressed', String(Number(button.dataset.shape) === value)));
    window.dispatchEvent(new CustomEvent('portfolioShape', {detail:value}));
  };
  document.querySelectorAll('[data-shape]').forEach(button => button.addEventListener('click', () => setShape(Number(button.dataset.shape))));
  $('#spark').addEventListener('click', () => setShape((shape+1)%3));
  setShape(0);
  // The lightweight sculpture remains playable when WebGL is unavailable.
  const orb = $('.fallback-orb');
  let orbDrag = false, orbX = 0, orbTurn = -25;
  orb.addEventListener('pointerdown', event => {
    orbDrag = true; orbX = event.clientX; orb.setPointerCapture(event.pointerId);
  });
  orb.addEventListener('pointermove', event => {
    if (!orbDrag) return;
    orbTurn += (event.clientX - orbX) * .7; orbX = event.clientX;
    orb.style.rotate = orbTurn+'deg';
  });
  ['pointerup','pointercancel','lostpointercapture'].forEach(type => orb.addEventListener(type, () => {orbDrag=false;}));
})();

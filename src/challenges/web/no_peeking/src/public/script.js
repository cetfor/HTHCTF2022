(() => {
  const scripts = document.querySelectorAll('script');
  scripts.forEach((script) => script.remove());

  const chr = (c) => c.charCodeAt(0);
  
  const form = document.querySelector('form');
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const input = document.querySelector('input[type="text"]');
    const output = [];
    for (const char of input.value.split('').map(chr)) {
      if (chr('a') <= char && char <= chr('z')) {
        output.push(chr('a') + ((char - chr('a') + 13) % 26));
      } else if (chr('A') <= char && char <= chr('Z')) {
        output.push(chr('A') + ((char - chr('A') + 13) % 26));
      } else {
        output.push(char);
      }
    }
    
    const target = 'UGU{v_ungr_wninfpevcg}';
    let value = output.map((c) => String.fromCharCode(c)).join('');
    if (value === target) {
      document.querySelector('.content').textContent = 'Correct!';
    } else {
      input.removeAttribute('style');
      input.offsetWidth;
      input.style.animation = 'shake 0.25s';
    }
  });
})();

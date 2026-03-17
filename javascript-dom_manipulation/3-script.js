const tag = document.querySelector('header');
const toggleHeader = document.getElementById('toggle_header');
if (tag.classList.length === 0) {
  tag.classList.add('green');
}

toggleHeader.addEventListener('click', () => {
  if (tag.classList.value.includes('green')) {
    tag.classList.replace('green', 'red');
  } else if (tag.classList.value.includes('red')) {
    tag.classList.replace('red', 'green');
  }
});

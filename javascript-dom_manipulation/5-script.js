const tag = document.querySelector('header');
const updateHeader = document.getElementById('update_header');
updateHeader.addEventListener('click', () => {
  tag.textContent = 'New Header!!!';
});

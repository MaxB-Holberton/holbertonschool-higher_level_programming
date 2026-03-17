const theList = document.querySelector('.my_list');
const addItem = document.getElementById('add_item');

addItem.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  theList.appendChild(newItem);
});

document.getElementById('add_item').addEventListener('click', function () {
  const ul = document.querySelector('ul.my_list');
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
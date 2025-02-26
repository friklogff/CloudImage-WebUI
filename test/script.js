document.addEventListener('DOMContentLoaded', () => {
  // Fetch the JSON data
  fetch('images.json')
    .then(response => response.json())
    .then(data => {
      const coverflowList = document.getElementById('coverflow-list');
      const controls = document.getElementById('controls');

      data.forEach((item, index) => {
        // Create the cover item
        const input = document.createElement('input');
        input.type = 'radio';
        input.name = 'cover-item';
        input.id = item.id;
        input.setAttribute('aria-label', `Select album ${index + 1}`);

        const li = document.createElement('li');
        li.className = 'coverflow-item';

        const label = document.createElement('label');
        label.htmlFor = item.id;

        const figure = document.createElement('figure');
        figure.className = 'album-cover';

        const img = document.createElement('img');
        img.src = item.image;
        img.alt = item.name;

        const figcaption = document.createElement('figcaption');
        figcaption.className = 'album-name';
        figcaption.textContent = item.name;

        figure.appendChild(img);
        figure.appendChild(figcaption);
        label.appendChild(figure);
        li.appendChild(label);

        coverflowList.appendChild(input);
        coverflowList.appendChild(li);

        // Create the control label
        const controlLabel = document.createElement('label');
        controlLabel.htmlFor = item.id;
        controlLabel.textContent = index + 1;
        controls.appendChild(controlLabel);
      });
    })
    .catch(error => console.error('Error fetching the JSON data:', error));
});
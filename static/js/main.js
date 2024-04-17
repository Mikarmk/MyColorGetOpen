document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const colorPalette = document.querySelector('#color-palette');

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const imageFile = formData.get('image');

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/');
        xhr.send(formData);

        xhr.onload = function() {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                const hexColors = response.hex;
                const rgbColors = response.rgb;

                colorPalette.innerHTML = '';
                for (let i = 0; i < hexColors.length; i++) {
                    const colorBox = document.createElement('div');
                    colorBox.classList.add('color-box');
                    colorBox.style.backgroundColor = hexColors[i];
                    const span = document.createElement('span');
                    span.textContent = `RGB: ${rgbColors[i]}`;
                    colorBox.appendChild(span);
                    colorPalette.appendChild(colorBox);
                }
            }
        };
    });
})
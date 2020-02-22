const colorPicker = document.getElementById("colorPicker");
const sizePicker = document.getElementById("sizePicker");
const pixelCanvas = document.getElementById("pixelCanvas");
const inputHeight = document.getElementById('inputHeight');
const inputWidth = document.getElementById('inputWidth');


function makeGrid(height, width) {
    for (let i = 0; i < height; i++) {
        const row = pixelCanvas.insertRow(i);
        for (let j = 0; j < width; j++) {
            row.insertCell(j);
            pixelCanvas.addEventListener('click', function(event) {
                event.preventDefault();
            });
        }
    }
}

sizePicker.addEventListener('click', function(event) {
    event.preventDefault();
})

makeGrid(inputHeight, inputWidth);

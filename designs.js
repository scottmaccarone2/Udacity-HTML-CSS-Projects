var colorPicker = document.getElementById("colorPicker");
var sizePicker = document.getElementById("sizePicker");
var pixelCanvas = document.getElementById("pixelCanvas");
var inputHeight = document.getElementById('inputHeight');
var inputWidth = document.getElementById('inputWidth');


function makeGrid(height, width) {
    for (let i = 0; i < height; i++) {
        const row = pixelCanvas.insertRow(i);
        for (let j = 0; j < width; j++) {
            const cell = row.insertCell(j);
            pixelCanvas.addEventListener('click', function(event) {
                event.preventDefault();
                cell.style.backgroundColor = colorPicker;
            });
        }
    }
}

sizePicker.addEventListener('click', function(event) {
    event.preventDefault();
    makeGrid(inputHeight, inputWidth);
})

makeGrid(inputHeight, inputWidth);

// select appropriate elements by id and isolate values where needed
var colorPicker = document.getElementById("colorPicker");
var sizePicker = document.getElementById("sizePicker");
var pixelCanvas = document.getElementById("pixelCanvas");
var inputHeight = document.getElementById('inputHeight').value;
var inputWidth = document.getElementById('inputWidth').value;


function makeGrid(height, width) {
    // nested for loops to build out the rows and columns
    for (let i = 0; i < height; i++) {
        const row = pixelCanvas.insertRow(i);
        for (let j = 0; j < width; j++) {
            const cell = row.insertCell(j);
            // add a click event listener so that when the user clicks on a
            // cell, we can apply the color selected from the `colorPicker`
            // to that specific cell clicked on
            pixelCanvas.addEventListener('click', function(event) {
                event.preventDefault();
                // isolate the value from the colorPicker
                var color = colorPicker.value;
                // color the cell that was clicked on (the event target)
                event.target.style.backgroundColor = color;
            });
        }
    }
}

// code to remove the previous grid and replace it with a new grid with the
// appropriate color selected for each cell
sizePicker.addEventListener('click', function(event) {
    event.preventDefault();
    // need to remove the grid
    pixelCanvas.firstChild.remove();
    // select height & width elements by id and isolate the values
    var sizeHeight = document.getElementById('inputHeight').value;
    var sizeWidth = document.getElementById('inputWidth').value;
    // replace the grid with new grid
    makeGrid(sizeHeight, sizeWidth);
})

makeGrid(inputHeight, inputWidth);

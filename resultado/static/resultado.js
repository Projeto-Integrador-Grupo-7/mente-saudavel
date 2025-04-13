const slider = document.getElementById('feelingRange');

function changeColor() {

    const value = slider.value;
    const percent = (value - 1) / 4; // de 0 a 1
    const red = Math.round(255 * percent);
    const green = Math.round(230 * (1 - percent));
    const color = `rgb(${red}, ${green}, 0)`;
    const gradPercent = value * 20;
    slider.style.background = `linear-gradient(to right, ${color} ${gradPercent}%, #ccc ${gradPercent}%)`;
}

changeColor();
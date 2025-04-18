const slider = document.getElementById('feelingRange');

function changeColor() {
    const value = parseInt(slider.value, 10);
    let color;

    if (value === 0) {
        color = '#ccc';
    } else if (value >= 1 && value <= 7) {
        color = 'green';
    } else if (value >= 8 && value <= 14) {
        color = 'gold';
    } else if (value >= 15) {
        color = 'red';
    }

    const gradPercent = (value / 20) * 100;
    slider.style.background = `linear-gradient(to right, ${color} ${gradPercent}%, #ccc ${gradPercent}%)`;
}

changeColor();
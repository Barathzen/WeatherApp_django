document.addEventListener('DOMContentLoaded', function () {
    updateTime();
    setInterval(updateTime, 1000);
    updateDate();
});

function updateTime() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');

    const liveTimeElement = document.getElementById('live-time');
    liveTimeElement.textContent = `${hours}:${minutes}:${seconds}`;
}

function updateDate() {
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    const formattedDate = now.toLocaleDateString('en-US', options);

    const liveDateElement = document.getElementById('live-date');
    liveDateElement.textContent = formattedDate;
}

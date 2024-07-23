document.addEventListener("DOMContentLoaded", function() {
    const progressCircles = document.querySelectorAll('.progress-circle');

    progressCircles.forEach(circle => {
        const progress = circle.getAttribute('data-progress');
        const progressBar = circle.querySelector('.progress-bar');
        const progressValue = progress * 3.6; // Convert percentage to degrees
        progressBar.style.background = `conic-gradient(#4caf50 ${progressValue}deg, #ddd ${progressValue}deg)`;
    });
});
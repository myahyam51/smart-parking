window.onload = function () {
    console.log("Smart Parking System Loaded Successfully!");
};

const bookButton = document.querySelector(".hero button");

if (bookButton) {
    bookButton.addEventListener("click", function () {
        alert("Welcome! Reservation feature will be available soon.");
    });
}


const cards = document.querySelectorAll(".card");

cards.forEach(card => {
    card.addEventListener("click", function () {

        if (card.classList.contains("available")) {
            alert("This parking space is available.");
        } else {
            alert("This parking space is occupied.");
        }

    });
});


cards.forEach(card => {
    card.addEventListener("mouseenter", function () {
        card.style.transform = "scale(1.05)";
    });

    card.addEventListener("mouseleave", function () {
        card.style.transform = "scale(1)";
    });
});
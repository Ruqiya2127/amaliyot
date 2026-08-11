document.addEventListener("DOMContentLoaded", function () {

    // =========================
    // PRODUCT CARD ANIMATION
    // =========================

    const cards = document.querySelectorAll(".product-card");

    cards.forEach((card, index) => {

        card.style.animationDelay = `${index * 0.08}s`;

    });


    // =========================
    // BUTTON EFFECT
    // =========================

    const buttons = document.querySelectorAll(
        ".detail-button, .back-button"
    );

    buttons.forEach(button => {

        button.addEventListener("click", function () {

            this.style.transform = "scale(0.96)";

            setTimeout(() => {
                this.style.transform = "";
            }, 150);

        });

    });


    // =========================
    // PRODUCT TITLE HOVER
    // =========================

    const productTitles = document.querySelectorAll(
        ".product-title a"
    );

    productTitles.forEach(title => {

        title.addEventListener("mouseenter", function () {
            this.style.letterSpacing = "0.3px";
        });

        title.addEventListener("mouseleave", function () {
            this.style.letterSpacing = "0";
        });

    });


    // =========================
    // NAVBAR SCROLL EFFECT
    // =========================

    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {

        if (window.scrollY > 50) {

            navbar.style.boxShadow =
                "0 6px 25px rgba(0, 0, 0, 0.2)";

        } else {

            navbar.style.boxShadow =
                "0 4px 15px rgba(0, 0, 0, 0.12)";

        }

    });


    // =========================
    // IMAGE ERROR
    // =========================

    const images = document.querySelectorAll(
        ".detail-image img"
    );

    images.forEach(image => {

        image.addEventListener("error", function () {

            this.src =
                "https://demofree.sirv.com/nope-not-here.jpg";

        });

    });

});
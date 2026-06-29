const rain = document.querySelector(".rain");

for (let i = 0; i < 200; i++) {

    let drop = document.createElement("span");

    drop.classList.add("drop");

    drop.style.left = Math.random() * 100 + "vw";

    drop.style.animationDuration = (0.5 + Math.random() * 0.5) + "s";

    drop.style.animationDelay = Math.random() * 2 + "s";

    rain.appendChild(drop);
}
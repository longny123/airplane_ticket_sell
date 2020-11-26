const sign_in_btn = document.querySelector("#sign-in-btn")
const sign_up_btn = document.querySelector("#sign-up-btn")
const container = document.querySelector(".container")
const stars = document.querySelectorAll("#star");


sign_up_btn.addEventListener('click', () =>{
    container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener('click', () =>{
    container.classList.remove("sign-up-mode");
});


stars.forEach(star => {
    let duration = Math.random() * (1.2 - 0.6) + 0.6;
    star.style.animation = `stars ${duration}s infinite linear`;
});

window.addEventListener("load", () => {
    const preloader = document.querySelector(".preloader");
    preloader.classList.add("preload-finish");
})
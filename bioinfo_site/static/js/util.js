function navbar_burger() {
    let burger_button = document.querySelector('.navbar-burger');
    let nav_menu = document.querySelector('.navbar-menu');
    burger_button.addEventListener('click', () => {
        burger_button.classList.toggle('is-active');
        nav_menu.classList.toggle('is-active');
    });
}
navbar_burger();
const nav__links = document.querySelector('.nav__links');
const menuBtn = document.getElementById('menu-btn');
const menuIcon = document.getElementById('menu-icon');

menuBtn.addEventListener('click' , () => {
    nav__links.classList.toggle('open')

    isOpen = nav__links.classList.contains('open')
    menuIcon.setAttribute('class' , isOpen ? 'ri-close-line' : 'ri-menu-fold-line')
})

nav__links.addEventListener('click' , () => {
    nav__links.classList.remove('open')
    menuIcon.setAttribute('class' , 'ri-menu-fold-line')
})



// alert
const alerts = document.querySelectorAll('.alert')

setTimeout( () => {
    alerts.forEach( e => {
        e.classList.add('hide')
    })
} , 5000)
// === alert ===
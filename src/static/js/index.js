const submenu = document.querySelector(".submenu")
const team = document.querySelector("#team__submenu")
team.addEventListener('click',()=>{
    submenu.classList.toggle('show__team')
})

const aside__left = document.querySelector('.aside__left')
const click__left__open = document.querySelector('#click__left__open')
const click__left__close = document.querySelector('#click__left__close')

click__left__open.addEventListener('click',()=>{
    console.log('*********')
    aside__left.classList.add('move__left')
})
click__left__close.addEventListener('click',()=>{
    aside__left.classList.remove('move__left')
})

const aside__right = document.querySelector('.aside__right')
const click__right__open = document.querySelector('#click__right__open')
const click__right__close = document.querySelector('#click__right__close')

click__right__open.addEventListener('click',()=>{
    console.log('*********')
    aside__right.classList.add('move__right')
})
click__right__close.addEventListener('click',()=>{
    aside__right.classList.remove('move__right')
})


const grande    = document.querySelector('.bodycarrousel')
const punto     = document.querySelectorAll('.punto')

punto.forEach( ( cadaPunto , i )=> {
    punto[i].addEventListener('click',()=>{
        let posicion  = i
        console.log(i)
        let operacion = posicion * -50
        grande.style.transform = `translateX(${ operacion }%)`

        punto.forEach( ( cadaPunto , i )=>{
            punto[i].classList.remove('activo')
        })
        punto[i].classList.add('activo')

    })
})
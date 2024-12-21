const closeList = document.querySelector("#close");
const burger = document.querySelector("#burger");
const list = document.querySelector('#list')
const listItem = document.querySelectorAll('.list-item')
const closeMenu=document.querySelector('#closeMenu')
const lang = document.querySelector('.lang')
const langs = document.querySelector('.langs')
const langItems = document.querySelector('.lang-items')

burger.addEventListener("click",()=>{
    list.classList.add("right-0");
})
closeMenu.addEventListener("click",()=>{
    list.classList.remove("right-0");
})
if(list.classList.contains("right-0")){
    window.addEventListener("click", ()=>{
        list.classList.remove("right-0");
    })
}
listItem.forEach((item) => (
    item.addEventListener('click', () => {
        list.classList.remove('right-0')
    })
))

lang.addEventListener('click', () => {
    langItems.classList.toggle('grid-rows-[1fr]')
})
window.addEventListener('scroll', () => {
    if (window.scrollY > 0) {
        langItems.classList.remove('grid-rows-[1fr]')
    }
})

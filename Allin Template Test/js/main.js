let slideIndex = 1;
function setSlide(slideId, index){
    slideIndex = index;
    let slide = document.querySelector(`#${slideId}`)
    let slides = [...document.querySelector(`.slides`).children];
    slides.forEach((element)=>{
        element.classList.remove('active');
    })
    slide.classList.add('active');
}

setInterval(()=>{
    slideIndex += 1
    if(slideIndex === 5){
        slideIndex = 1
    }
    setSlide(`slide${slideIndex}`, slideIndex)
}, 4000)
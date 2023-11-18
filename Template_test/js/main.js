var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,

    spaceBetween: 10,

    breakpoints: {
      640: {
        slidesPerView: 2,
        spaceBetween: 5,
      },
      768: {
        slidesPerView: 4,
        spaceBetween: 5,
      },
      1024: {
        slidesPerView: 5,
        spaceBetween: 5,
      },
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });
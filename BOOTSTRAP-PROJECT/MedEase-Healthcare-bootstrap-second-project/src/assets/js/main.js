import "../scss/style.scss";
import * as bootstrap from "bootstrap";

import Swiper from "swiper";
import { Navigation, Pagination } from "swiper/modules";

import "swiper/css";
import "swiper/css/navigation";
import "swiper/css/pagination";

new Swiper(".expertiseSwiper", {
  modules: [Navigation, Pagination],

  slidesPerView: 3.25,
  spaceBetween: 24,
  speed: 500,
  loop: false,
  watchOverflow: true,

  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  pagination: {
    el: ".expertise-pagination",
    clickable: true,
  },

  breakpoints: {
    0: {
      slidesPerView: 1.1,
      spaceBetween: 12,
    },
    576: {
      slidesPerView: 1.7,
      spaceBetween: 16,
    },
    768: {
      slidesPerView: 2.2,
      spaceBetween: 20,
    },
    992: {
      slidesPerView: 3,
      spaceBetween: 24,
    },
    1200: {
      slidesPerView: 3.25,
      spaceBetween: 24,
    },
  },
});

new Swiper(".testimonialSwiper", {
    modules: [Navigation, Pagination],

    loop: false,
    speed: 600,

    slidesPerView: 1.8,
    slidesPerGroup: 1,
    spaceBetween: 24,

    navigation: {
        nextEl: ".testimonial-next",
        prevEl: ".testimonial-prev",
    },

    pagination: {
        el: ".testimonial-pagination",
        clickable: true,
    },

    breakpoints: {
        320: {
            slidesPerView: 1,
            spaceBetween: 16,
        },

        576: {
            slidesPerView: 1.1,
            spaceBetween: 20,
        },

        768: {
            slidesPerView: 1.3,
            spaceBetween: 20,
        },

        992: {
            slidesPerView: 1.6,
            spaceBetween: 24,
        },

        1200: {
            slidesPerView: 1.8,
            spaceBetween: 24,
        },
    },
});

new Swiper(".blogSwiper", {
    modules: [Navigation, Pagination],

    slidesPerView: 3.25,
    spaceBetween: 24,
    loop: false,
    watchOverflow: false,

    navigation: {
        nextEl: ".blog-next",
        prevEl: ".blog-prev",
    },

    pagination: {
        el: ".blog-pagination",
        clickable: true,
    },

    breakpoints: {
        320: {
            slidesPerView: 1.1,
            spaceBetween: 16,
        },
        576: {
            slidesPerView: 1.5,
            spaceBetween: 20,
        },
        768: {
            slidesPerView: 2.2,
            spaceBetween: 20,
        },
        992: {
            slidesPerView: 3.25,
            spaceBetween: 24,
        },
        1200: {
            slidesPerView: 3.25,
            spaceBetween: 24,
        },
    },
});
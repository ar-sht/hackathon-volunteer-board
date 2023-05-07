window.addEventListener('scroll', function () {
  let banner = document.querySelector('.banner');
  let bannerImg = document.querySelector('.banner-img');
  let scrollPosition = window.pageYOffset;
  banner.style.transform = 'translateY(' + scrollPosition * 0.07 + 'px)';
  bannerImg.style.transform = 'translateY(' + scrollPosition * 0.3 + 'px)';
});

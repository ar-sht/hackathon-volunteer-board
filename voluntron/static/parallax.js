window.addEventListener('scroll', function () {
  let banner = document.querySelector('.banner');
  let bannerImg = document.querySelector('.banner-img');
  let scrollPosition = window.pageYOffset;
  banner.style.transform = 'translateY(' + scrollPosition * 0.08 + 'px)';
  bannerImg.style.transform = 'translateY(' + scrollPosition * 0.5 + 'px)';
});

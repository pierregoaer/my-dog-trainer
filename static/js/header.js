const toggle = document.querySelector('.toggle-container');
const siteWrapper = document.querySelector('.site-wrapper');

const mobileNavIconContainer = document.querySelector('.mobile-nav-icon-container');
const mobileNavIcon = document.querySelectorAll('.mobile-nav-icon');
const mainNavigation = document.querySelector('.main-navigation');
const mainNavigationLinks = document.querySelectorAll('.main-navigation a');

mobileNavIconContainer.addEventListener('click', function () {
	mobileNavIconContainer.classList.toggle('active');
	siteWrapper.classList.toggle('hidden');
	mobileNavIcon.forEach(bar => bar.classList.toggle('active'));
	const visibility = mainNavigation.getAttribute('data-visible');
	if (visibility === 'false') mainNavigation.setAttribute('data-visible', true);
	if (visibility === 'true') mainNavigation.setAttribute('data-visible', false);
});

mainNavigationLinks.forEach(
	link =>
		(link.onclick = () => {
			mobileNavIcon.forEach(bar => bar.classList.remove('active'));
			mobileNavIconContainer.classList.remove('active');
			siteWrapper.classList.remove('hidden');
			const visibility = mainNavigation.getAttribute('data-visible');
			if (visibility === 'false') mainNavigation.setAttribute('data-visible', true);
			if (visibility === 'true') mainNavigation.setAttribute('data-visible', false);
		})
);
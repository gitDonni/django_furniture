let lastScroll = 0;
const defaultOffset = 200;
const header = document.querySelector('header');

const scrollPosition = () => window.pageYOffset || document.documentElement.scrollTop
const containHidden = () => header.classList.contains('hidden');

window.addEventListener('scroll', () => {
     if(scrollPosition() > lastScroll && !containHidden() && scrollPosition() > defaultOffset) {
        //scroll down
        header.classList.add('hidden');
        console.log('down')
    }
    else if(scrollPosition() < lastScroll && containHidden()){
        //scroll up
        console.log('up')
        header.classList.remove('hidden');
    }

    lastScroll = scrollPosition();
})
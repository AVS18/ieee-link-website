const categories = document.querySelectorAll('.right-col .categories');

const categoriesOption = {
    threshold: .2,
    rootMargin: "0px 0px 100px 0px "
}
const categoryObservers = new IntersectionObserver((
    entries,
    categoryObservers
) => {
    entries.forEach(entry => {
        const a = entry.target.classList
        if (entry.isIntersecting) {
            a.add('show');
        }
        else {
            a.remove('show');
        }
    })
}, categoriesOption);

categories.forEach((category) => {
    categoryObservers.observe(category);
})

//bottom box
const boxOption = {
    threshold: .2,
    rootMargin: "0px 0px -100px 0px "
}
const boxObservers = new IntersectionObserver((
    entries,
    boxObservers
) => {
    entries.forEach(entry => {
        const a = entry.target.classList
        if (entry.isIntersecting) {
            a.add('show');
        }
        else {
            a.remove('show');
        }
    })
}, boxOption);
const box1 = document.querySelector('.left-col .navigation')
boxObservers.observe(box1)

//information 
const infoObservers = new IntersectionObserver((
    entries,
    infoObservers
) => {
    entries.forEach(entry => {
        const a = entry.target.classList
        if (entry.isIntersecting) {
            a.add('show');
        }
        // else {
        //     a.remove('show');
        // }
    })
}, categoriesOption);
const contents = document.querySelectorAll('.left-col .information > p')
const ols = document.querySelectorAll('.left-col .information ol')
contents.forEach(i => {
    infoObservers.observe(i)
})
ols.forEach(i => {
    infoObservers.observe(i)
})

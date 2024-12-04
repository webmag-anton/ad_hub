const $categories = document.querySelectorAll('.categories-wrapper .category')

$categories.forEach(category => {
    category.addEventListener('click', console.log(category.dataset.category))
})
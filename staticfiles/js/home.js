document.addEventListener('DOMContentLoaded', () => {
    const $wrapper = document.querySelector('.categories-wrapper')
    const $categories = $wrapper.querySelectorAll('.category')
    const $subcategories = $wrapper.querySelector('#subcategories')

    // $categories.forEach(category => {
    //     category.addEventListener('click', toggleAccordeon(category.dataset.category))
    // })

    // function toggleAccordeon(categoryName) {
    //     subcategories
    // }


    $categories.forEach(category => {
        category.addEventListener('click', () => {
            const categoryName = category.dataset.categoryName

            fetch(`/get-subcategories/${categoryName}/`)
                .then(response => response.json())
                .then(data => {
                    $subcategories.innerHTML = ''

                    if (data.subcategories.length > 0) {
                        data.subcategories.forEach(subcategory => {
                            const $li = document.createElement('li');
                            $li.textContent = subcategory.name;
                            $subcategories.appendChild($li);
                        });
                    } else {
                        $subcategories.innerHTML = 'No subcategories found.';
                    }
                })
                .catch(error => {
                    console.error('Error fetching subcategories:', error);
                    $subcategories.innerHTML = 'Error loading subcategories.';
                })
        })
    })
})


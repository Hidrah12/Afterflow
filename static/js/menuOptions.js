function showOptionsMenu(name) {
    let nameOption = document.getElementById(name)
    if (nameOption.style.display === 'none') {
        let menuOptions = document.getElementsByClassName('menu-option')
        Array.from(menuOptions).map(ul => {
            if (ul.style.display === 'block') {
                ul.style.display = 'none'
            }
        })
        nameOption.style.display = 'block'
    } else {
        nameOption.style.display = 'none'
    }
}
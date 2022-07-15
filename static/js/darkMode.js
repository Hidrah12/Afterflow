(
    function(){
        let html = document.getElementById('html')
        let featuredImage = document.getElementById('featured-image')
        if (localStorage.getItem('theme')) {
            if (localStorage.getItem('theme') === 'dark') {
                html.classList.add('dark')
                featuredImage.src = '../../static/images/featured-dark-image.png'
            } else {
                html.classList.remove('dark')
                let img = document.getElementById('img-theme')
                img.src = "../../static/images/theme/light-mode.png"
                featuredImage.src = '../../media/featured/Captura_de_pantalla_40.png'
            }
        } else {
            localStorage.setItem('theme', 'dark')
            html.classList.add('dark')
        }
    }
)();

function changeTheme() {
    let html = document.getElementById('html')
    let img = document.getElementById('img-theme')
    let featuredImage = document.getElementById('featured-image')

    if (localStorage.getItem('theme') === 'dark') {
        html.classList.remove('dark')
        localStorage.theme = 'light'
        img.src = "../../static/images/theme/light-mode.png"
        featuredImage.src = '../../media/featured/Captura_de_pantalla_40.png'

    } else {
        html.classList.add('dark')
        localStorage.theme = 'dark'
        img.src = "../../static/images/theme/dark-mode.png"
        featuredImage.src = '../../static/images/featured-dark-image.png'
    }
}
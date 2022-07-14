(
    function(){
        let html = document.getElementById('html')

        if (localStorage.getItem('theme')) {
            if (localStorage.getItem('theme') === 'dark') {
                html.classList.add('dark')
            } else {
                html.classList.remove('dark')
                let img = document.getElementById('img-theme')
                img.src = "../../static/images/theme/light-mode.png"
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

    if (localStorage.getItem('theme') === 'dark') {
        html.classList.remove('dark')
        localStorage.theme = 'light'
        img.src = "../../static/images/theme/light-mode.png"
    } else {
        html.classList.add('dark')
        localStorage.theme = 'dark'
        img.src = "../../static/images/theme/dark-mode.png"
    }
}
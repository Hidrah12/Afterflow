let summarys = document.getElementsByClassName('parrafo')
Array.from(summarys).map(summary => {
    if (summary.innerHTML.length >= 100) {
        let slice = summary.innerHTML.slice(100,summary.length)
        let index = slice.lastIndexOf(' ')
        summary.innerHTML = summary.innerHTML.slice(0, index) + "..." + " <a href='#' class='text-cyan-300'>Leer más</a>"
    }
})
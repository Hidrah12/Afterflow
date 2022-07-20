let summarys = document.getElementsByClassName('parrafo')
Array.from(summarys).map(summary => {
    if (summary.innerHTML.length >= 100) {
        let slice = summary.innerHTML.slice(100,summary.length)
        alert(slice)
        let index = slice.indexOf(' ')
        summary.innerHTML = summary.innerHTML.slice(0, index) + "..." + " <a href='#' class='text-cyan-400'>Leer más</a>"
    }
})
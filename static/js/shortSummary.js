let summarys = document.getElementsByClassName('parrafo')
Array.from(summarys).map(summary => {
    if (summary.innerHTML.length >= 100) {
        summary.innerHTML = summary.innerHTML.slice(0, 200) + "..." + " <a href='#' class='text-cyan-400'>Leer más</a>"
    }
})
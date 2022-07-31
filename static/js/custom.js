// Cortar párrafo
let summarys = document.getElementsByClassName('paragraph')
Array.from(summarys).forEach(summary => {
    if (summary.innerHTML.length >= 100) {
        summary.innerHTML = summary.innerHTML.slice(0, 200) + "..." + ` <a href='' class='text-cyan-400 hover:text-cyan-500 text-base'>Leer más</a>`
    }
})

// Quitar ultima línea separadora
// let articles = document.getElementsByClassName('article')
// let lastId = Array.from(articles)[articles.length-1].id
// let div = document.getElementById(`div-${lastId}`)
// div.style.display = 'none'

// Cortar párrafo
let summarys = document.getElementsByClassName('paragraph')
Array.from(summarys).forEach(summary => {
    if (summary.innerHTML.length >= 100) {
        let index = 200
        while (summary.innerHTML[index] != ' ') {
            index += 1
        }
        summary.innerHTML = summary.innerHTML.slice(0, index) + "..." + ` <a href='#' class='read-more text-cyan-400 hover:text-cyan-500 text-base'>Leer más</a>`
    }
})
let urls = []
let titles = document.getElementsByClassName('title')
Array.from(titles).forEach(element => {
    urls.push(element.href)
})
let urlsReadMore = document.getElementsByClassName('read-more')
for (let index = 0; index < urlsReadMore.length; index++) {
    urlsReadMore[index].href = urls[index]
}
// Quitar ultima línea separadora
// let articles = document.getElementsByClassName('article')
// let lastId = Array.from(articles)[articles.length-1].id
// let div = document.getElementById(`div-${lastId}`)
// div.style.display = 'none'

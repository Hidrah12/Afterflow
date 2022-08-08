(
    function () {
        fetch(`/api/set/`)
    }
)();
function showMenuSession() {
    let menuSession = document.getElementById('menu-session')
    if (menuSession.style.display === 'none') {
        menuSession.style.display = 'block'
    }
    else {
        menuSession.style.display = 'none'
    }
}

function showSidePanel() {
    let sidePanel = document.getElementById('side-panel')
    let block = document.getElementById('block')
    if (sidePanel.classList.toString().includes('panel-lateral') ){
        sidePanel.classList.remove('panel-lateral')
        block.style.display = 'none'
    } else {
        sidePanel.classList.add('panel-lateral')
        block.style.display = 'block'
    }
}

function showOptionsMenu(optionName) {
    let optionSelected = document.getElementById(optionName)
    if (optionSelected.style.display === 'none') {
        let subMenus = document.getElementsByClassName('menu-option')
        Array.from(subMenus).map(subMenu => {
            if (subMenu.style.display === 'block') {
                subMenu.style.display = 'none'
            }
        })
        optionSelected.style.display = 'block'
    } else {
        optionSelected.style.display = 'none'
    }
}

function getMoreArticles(event) {
    event.preventDefault()
    fetch("/api/")
    .then(response => response.json())
    .then(function (data) {
        data.map(element => {
            if (element['Message']) {
                let btnGetMoreArticles = document.getElementById('btnGetMoreArticles')
                btnGetMoreArticles.style.display = 'none'
            } else {
                let contentArticles = document.getElementById('content-articles')
                contentArticles.innerHTML += `
                <article id="${element.id}" class="article last:mb-10 my-24 relative">
                    <h2 class="my-5 "><a href="#" class="title text-5xl sm:text-3xl font-extrabold font-['Roboto'] my-5 hover:text-cyan-400 transition-colors dark:text-slate-50 dark:hover:text-cyan-400 xr:text-[1.3rem]" title="${element.title}">${element.title}</a></h2>
                    <span class="italic text-[rgb(172,172,172)]">Publicado el ${element.publication_date} <a href="" class=" py-1 p-2 ml-2 rounded-sm text-xs font-normal bg-[#f3f1f1d4] text-slate-600 hover:bg-[#d8d8d8]">${element.category_for_development}</a></span>
                    <p class='paragraph text-xl sm:text-base leading-8 text-justify font-light my-5 font-["Roboto"] text-slate-800 dark:text-slate-300 whitespace-pre-wrap'>${element.summary}</p>
                </article>
                `
            }
        })
        let summarys = document.getElementsByClassName('paragraph')
        Array.from(summarys).map(summary => {
            if (summary.innerHTML.length >= 100) {
                summary.innerHTML = summary.innerHTML.slice(0, 200) + "..." + " <a href='#' class='text-cyan-400 hover:text-cyan-500 text-base'>Leer más</a>"
            }
        })
    })
}

function search(value) {
    if (value != '' && value != ' ') {
        let itemsFound = document.getElementById('items-found')
        itemsFound.innerHTML = ''
        itemsFound.style.display = 'block'
        fetch(`/api/search/${value}`)
        .then(response => response.json())
        .then( (data) => {
            if (data['message']) {
                itemsFound.innerHTML = `<span>${data['message']}</span>`
            }
            data.forEach(element => {
                itemsFound.innerHTML += `<a href='/post/${element.slug}' class='block dark:text-white dark:hover:bg-slate-600 dark:hover:text-cyan-400 text-slate-800 my-2 mx-2 p-2 hover:text-cyan-500 hover:bg-slate-50'>${element.title}</a>`
            })
        })   
    }
}

function removeCoincidences() {
    let itemsFound = document.getElementById('items-found')
    itemsFound.style.display = 'none'
}
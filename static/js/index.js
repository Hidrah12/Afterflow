
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
    } 
    else {
        sidePanel.classList.add('panel-lateral')
        block.style.display = 'block'
    }
}

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
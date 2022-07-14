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
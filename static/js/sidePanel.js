function showSidePanel() {
    let sidePanel = document.getElementById('side-panel')
    if (sidePanel.classList.toString().includes('panel-lateral') ){
        sidePanel.classList.remove('panel-lateral')
    } 
    else {
        sidePanel.classList.add('panel-lateral')
    }
}
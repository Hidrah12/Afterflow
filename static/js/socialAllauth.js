// Agregar el tema
let html = document.getElementById('html')
if (localStorage.getItem('theme') === 'dark') {
    html.classList.add('dark')
} else {
    html.classList.remove('dark')
}

// Agregar icono de google y github
let googleLink = document.getElementsByClassName("google");
let githubLink = document.getElementsByClassName("github");
Array.from(googleLink).map(element => {
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/google.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
Array.from(githubLink).map(element =>{
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/githubLogo.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
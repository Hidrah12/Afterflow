// Agregar el tema
const html = document.getElementById('html')
if (localStorage.getItem('theme') === 'dark') {
    html.classList.add('dark')
} else {
    html.classList.remove('dark')
}

// Agregar icono de google y github
const googleLink = document.getElementsByClassName("google");
const githubLink = document.getElementsByClassName("github");
Array.from(googleLink).map(element => {
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/google-logo.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
Array.from(githubLink).map(element =>{
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/github-logo.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
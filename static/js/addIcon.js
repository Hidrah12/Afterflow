let google = document.getElementsByClassName("google");
let github = document.getElementsByClassName("github");
Array.from(google).map(element => {
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/google.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
Array.from(github).map(element =>{
    element.className = "flex items-center"
    element.innerHTML = `<img src="../../static/images/githubLogo.png" class="w-7 inline-block mx-2"></img>${element.innerHTML}`
});
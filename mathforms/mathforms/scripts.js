const buttons = document.getElementsByTagName('button')

for(let i = 0; i < buttons.length; i++) {
    buttons[i].onclick = (event) => {
        document.body.style.background = event.target.innerText
    }
}
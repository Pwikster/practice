function openDesc(element) {

    element.style.display = "none"

    const desc = element.nextElementSibling
    desc.style.display = "block"
}


function closeDesc(element) {
    const desc = element.parentElement
    desc.style.display = "none"
    desc.previousElementSibling.style.display ="block"

}
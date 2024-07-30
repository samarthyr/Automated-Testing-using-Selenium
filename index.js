const aboutDiv=document.querySelector('#about')
const contactDiv=document.querySelector('#contact')
const servicesDiv=document.querySelector('#services')
const home=document.querySelector('.home')

document.querySelector('#contactButton').addEventListener('click', function() {
    aboutDiv.style.display = "none";
    servicesDiv.style.display = "none";
    home.style.display='none'
    contactDiv.style.display='block'
});
document.querySelector('#aboutusButton').addEventListener('click', function() {
    aboutDiv.style.display = "block";
    servicesDiv.style.display = "none";
    home.style.display='none'
    contactDiv.style.display='none'
});
document.querySelector('#servicesButton').addEventListener('click', function() {
    aboutDiv.style.display = "none";
    servicesDiv.style.display = "block";
    home.style.display='none'
    contactDiv.style.display='none'
});
document.querySelector('#homeButton').addEventListener('click', function() {
    aboutDiv.style.display = "none";
    servicesDiv.style.display = "none";
    home.style.display='block'
    contactDiv.style.display='none'
});
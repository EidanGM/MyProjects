const boton = document.getElementById("miBotonColorin");

boton.addEventListener("click", function() {
    console.log("¡El botón funciona!");
    const r = Math.floor(Math.random() * 256);
    const g = Math.floor(Math.random() * 256);
    const b = Math.floor(Math.random() * 256);
    boton.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
});
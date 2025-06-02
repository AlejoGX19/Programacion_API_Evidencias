function prenderApgarBimbilla(interrucptor){
    let pic;

    if (interrucptor == "0") {
        pic = "IMG/bombilloApgado.jpg";
    }else{
        pic = "IMG/bombillaEncendida.avif";
    }
    document.getElementById("bombilla").src = pic;
}
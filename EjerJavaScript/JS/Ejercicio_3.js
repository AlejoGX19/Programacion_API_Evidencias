function productPrice(){
    var productName = document.getElementById("productName").value;

    var price = 0;

    switch(productName.toUpperCase()) {
        case 'MAZAMORRA':
        price = 1000;
        break;
        case "BOCADILLO":
            price = 800;
            break;
        case "PANELA":
            price = 600;
            break;
        case "MAIZ":
            price = 300;
            break;
        default:
            alert("Producto no Encontrado");
            break; 
    }
    document.getElementById("result").innerHTML = Intl.NumberFormat().format(price);
}
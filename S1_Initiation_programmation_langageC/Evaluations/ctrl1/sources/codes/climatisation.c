if (temperature < 25) {
    puissance_climatisation = 0;
}
if (temperature >= 25 && temperature < 30){
    puissance_climatisation = 1; 
}
else{
    puissance_climatisation = 2;
}
var latLngUmsa = {lat : -16.504874671937966, lng : -68.13007235527039};
var latLngTati = {lat : -16.505515021716285, lng : -68.12296986579895};
var map;
var marcaU;
var marcaT;

var $latitud = $("#latitud");
var $longitud = $("#longitud");
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: latLngUmsa,
        zoom: 15
    });
    //
    marcaU = new google.maps.Marker({
        position: latLngUmsa,
        map: map,
        title: "U.M.S.A."
    });
    //
    map.addListener("click", function(e) {
        $latitud.val("" + e.latLng.lat());
        $longitud.val("" + e.latLng.lng());
    });
    //
}

function localizar() {
    if(marcaT===undefined) {
        marcaT = new google.maps.Marker({
            position: latLngTati,
            map: map,
            title: "Casa de Tati"
        });
        //
        var ventanaInfo = new google.maps.InfoWindow({
            content: "Aqui vive la Tati ..."
        });
        //
        marcaT.addListener("click", function() {
            ventanaInfo.open(marcaT.get("map"), marcaT);
        });
    } else {
        alert("localizada");
    }
}
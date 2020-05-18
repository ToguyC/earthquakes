//  create map object, tell it to live in 'map' div and give initial latitude, longitude, zoom values 
var map = L.map('map', {scrollWheelZoom:true}).setView([0, 0], 5);

//  add base map tiles from OpenStreetMap and attribution info to 'map' div
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

let markers = L.layerGroup().addTo(map);

// create custom icon
var earthquakeIcon = L.icon({
    iconUrl: 'https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-512.png',
    iconSize: [51, 51], // size of the icon
});

// create marker object, pass custom icon as option, add to map         
L.marker([0, 0], {icon: earthquakeIcon}).addTo(markers);

// Setup the leaflet map
function SetupMap(lat, long) {
    markers.clearLayers();

    L.marker([lat, long], {icon: earthquakeIcon}).addTo(markers);
    map.setView([lat, long], 5)
}
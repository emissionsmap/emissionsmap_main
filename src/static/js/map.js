// style choropleth map color
function getColor(d) {
    return d > 100 ? "#0D47A1" :
           d > 50  ? "#1976D2" :
           d > 20  ? "#1E88E5" :
           d > 10  ? "#2196F3" :
           d > 5   ? "#42A5F5" :
           d > 2   ? "#64B5F6" :
           d > 1   ? "#90CAF9" :
                      '#7BBDEFB';
}

function style(feature) {
    return {
        fillColor: getColor(feature.properties[2015]),
        weight: 2,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
    };
}


// get leaflet and configuration
var map = L.map('map',{ zoomControl: false }).setView([51.505, -0.09], 3);

var southWest = L.latLng(-50.98155760646617, -180),
northEast = L.latLng(82.99346179538875, 180);
var bounds = L.latLngBounds(southWest, northEast);

map.setMaxBounds(bounds);
map.on('drag', function() {
    map.panInsideBounds(bounds, { animate: false });
});



// // base and control layers
var osmBase = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 8,
    minZoom:2,
    attribution: '© OpenStreetMap ....................'
}).addTo(map);

googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
    maxZoom: 10,
    minZoom:2,
    subdomains:['mt0','mt1','mt2','mt3'],
    attribution: '© Google |'
});

googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 10,
    minZoom:2,
    subdomains:['mt0','mt1','mt2','mt3'],
    attribution: '© Google |'
});
// var punto = L.marker([37.88437176085360, -4.779524803161621]).bindPopup('Soy un puntazo');
// punto.addTo(map);

var baseMaps = {
    "base":osmBase, 
    "Satélite": googleHybrid,
    "Catastro": googleStreets,

};

var overlayMaps = {
    // "Puntazo": punto
};

L.control.layers(
    baseMaps, 
    overlayMaps,
    {
	position: 'topright',
	collapsed: true
}).addTo(map);

// geoJson
L.geoJSON(worldData, {
        style: style
    })
    .bindPopup((layer) => {
        if(layer.feature.properties.NAME){
            right__country.classList.add('move__country')
            }
        console.log(layer.feature.properties.NAME)
        return layer.feature.properties.NAME
    })
    .addTo(map);


//legend
var legend = L.control({position: 'bottomleft'});

legend.onAdd = function () {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 20, 50, 100, 200, 500, 1000]

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(map);
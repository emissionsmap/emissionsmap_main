// style choropleth map color
function getColor(d) {
    return d > 7000 ? "#0D47A1" :
           d > 5000  ? "#1976D2" :
           d > 3000  ? "#1E88E5" :
           d > 1000  ? "#2196F3" :
           d > 500   ? "#42A5F5" :
           d > 200   ? "#64B5F6" :
           d > 10   ? "#90CAF9" :
                      '#7BBDEFB';
}
    
// get leaflet and configuration
var mapamundi = L.map('map',{ zoomControl: false }).setView([51.505, -0.09], 3);

var southWest = L.latLng(-50.98155760646617, -180),
northEast = L.latLng(82.99346179538875, 180);
var bounds = L.latLngBounds(southWest, northEast);

mapamundi.setMaxBounds(bounds);
mapamundi.on('drag', function() {
    mapamundi.panInsideBounds(bounds, { animate: false });
});

// // base and control layers
var osmBase = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 10,
    minZoom:2,
    attribution: '© OpenStreetMap |'
}).addTo(mapamundi);

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

var baseMaps = {
    "base":osmBase, 
    "Satélite": googleHybrid,
    "Catastro": googleStreets,

};

L.control.layers(
    baseMaps, 
    overlayMaps = {},
    {
	position: 'topright',
	collapsed: true
}).addTo(mapamundi);


// Shown popup with info
let popup  = (feature, layer) => {
    layer.bindPopup((layer) => {
        if(layer.feature.properties.NAME){
            right__country.classList.add('move__country')
            }
        return `<div>
                <p style="text-align:right; font-style: italic;">
                    ${feature.properties.ISO_A3}
                </p>
                <h3>${feature.properties.NAME}</h3>
                </div>`
    })
};

let jsonmundo = mundo

let emisionesmundo = emisiones


function style(feature) {
    let data;
    emisionesmundo.forEach( e => {
        if(feature.properties.ISO_A3 === e.id){
            data = e.n2019
        }
        })   
    return {fillColor: getColor(data)};             
        
}
let layer =  L.geoJson(jsonmundo, {
            onEachFeature: popup,
            style: style,
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        });
layer.addTo(mapamundi);


//legend
var legend = L.control({position: 'bottomleft'});
legend.onAdd = function () {

    var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 10, 200, 500, 1000, 3000, 5000, 7000]

    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
    }
    return div;
};
legend.addTo(mapamundi);
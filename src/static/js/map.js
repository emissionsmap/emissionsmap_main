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

var southWest = L.latLng(-50, -180),
northEast = L.latLng(90, 180);
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
            let variablejson = layer.feature.properties.ISO_A3
            mifuncion(variablejson)
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

function pintadoDeMapa(otrorandommas){

    function style(feature) {
        let data;
        emisionesmundo.forEach( e => {
            if(feature.properties.ISO_A3 === e.id){
                data = e[`n${otrorandommas}`]
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
}
pintadoDeMapa(2019)


const updateChart = (var1,var2,var3,var4) => {
    document.querySelector('#items__timeline').onclick  = e => {
        const { value: property} = e.target

        pintadoDeMapa(property)

        const newDataConsumo = 
        [var1.filter(m => m.anio == property).map(m => m.petroleo)[0],
        var1.filter(m => m.anio == property).map(m => m.carbon)[0],
        var1.filter(m => m.anio == property).map(m => m.gas)[0],
        var1.filter(m => m.anio == property).map(m => m.nuclear)[0],
        var1.filter(m => m.anio == property).map(m => m.hidraulica)[0],
        var1.filter(m => m.anio == property).map(m => m.solar)[0],
        var1.filter(m => m.anio == property).map(m => m.eolica)[0],
        var1.filter(m => m.anio == property).map(m => m.otras_renovables)[0]]

        const newDataProduccion = 
        [var2.filter(m => m.anio == property).map(m => m.petroleo)[0],
        var2.filter(m => m.anio == property).map(m => m.carbon)[0],
        var2.filter(m => m.anio == property).map(m => m.gas)[0],
        var2.filter(m => m.anio == property).map(m => m.nuclear)[0],
        var2.filter(m => m.anio == property).map(m => m.hidraulica)[0],
        var2.filter(m => m.anio == property).map(m => m.solar)[0],
        var2.filter(m => m.anio == property).map(m => m.eolica)[0],
        var2.filter(m => m.anio == property).map(m => m.otras_renovables)[0]]

        const newDataTop = var3.filter(m => m.anio == property).map(m => m.emisiones)[0]
        const newLabelTop = var3.filter(m => m.anio == property).map(m => m.paises)[0]

        const newDataContinente = var4.map(m => m[`n${property}`])

        updateData(chartcountryradar, newDataConsumo)
        updateData(chartcountrybar, newDataProduccion)
        updateDataLabel(charttopbar, newDataTop,newLabelTop)
        updateData(chartpieworld, newDataContinente)    
    }
}

// *************************************************************************
// *************************************************************************

// ----------------------------default chart------------------------------------
const styles = {
    color: {
        solids: ['rgba(116, 72, 194, 1)', 'rgba(33, 192, 215, 1)', 'rgba(217, 158, 43, 1)', 'rgba(205, 58, 129, 1)', 'rgba(156, 153, 204, 1)', 'rgba(225, 78, 202, 1)',
        'rgba(116, 72, 194, 1)', 'rgba(33, 192, 215, 1)', 'rgba(217, 158, 43, 1)', 'rgba(205, 58, 129, 1)', 'rgba(156, 153, 204, 1)', 'rgba(225, 78, 202, 1)'],
        alphas: ['rgba(116, 72, 194, .4)', 'rgba(33, 192, 215, .4)', 'rgba(217, 158, 43, .4)', 'rgba(205, 58, 129, .4)', 'rgba(156, 153, 204, .4)', 'rgba(225, 78, 202, .4)',
        'rgba(116, 72, 194, .4)', 'rgba(33, 192, 215, .4)', 'rgba(217, 158, 43, .4)', 'rgba(205, 58, 129, .4)', 'rgba(156, 153, 204, .4)', 'rgba(225, 78, 202, .4)']
    }
}
Chart.defaults.font.size = 18;

const updateDataLabel = (chartId, data, label) => {
    const chart = Chart.getChart(chartId)
    chart.data.datasets[0].data = data
    chart.data.labels = label
    chart.update()
}

const updateData = (chartId, data) => {
    const chart = Chart.getChart(chartId)
    chart.data.datasets[0].data = data
    chart.update()
}

// ----------------------------------- world -------------------------------
const chartprediction = document.getElementById('chart7').getContext('2d');
const chartpieworld = document.getElementById('chart1').getContext('2d');
const charttopbar = document.getElementById('chart2').getContext('2d');
const chartline1 = document.getElementById('chart3').getContext('2d');
const chartline2 = document.getElementById('chart4').getContext('2d');

let huellaMundial = huellamundial
let prediccionMundial = prediccion
let temperaturaMundial = temperatura
let emisonescontinente = emisionesContinente
let topPaises = top10

document.getElementById('biocapacidad').innerHTML = huellaMundial.filter(m => m.anio === 2021).map(m => m.biocapacidad)
document.getElementById('huella').innerHTML = huellaMundial.filter(m => m.anio === 2021).map(m => m.huella_ecologica)
document.getElementById('tierra').innerHTML = huellaMundial.filter(m => m.anio === 2021).map(m => m.tierra)

// **********************

const linePredictionChart = e => {
    
    const data = {
        labels: e.map(m => m.anio),
        datasets: [
            {
                label: 'Emisiones de co2',
                borderColor: styles.color.solids[2],
                data: e.map(m => m.emision_co2),
            },
            {
                label: 'Producción de energía',
                borderColor: styles.color.solids[3],
                backgroundColor: styles.color.solids[3],
                data:e.map(m => m.produccion_energia),
            }]}

    const options = {
        maintainAspectRatio: false,
    }

    new Chart(chartprediction, { type: 'line', data, options })
}


const pieChartWorld = e => {

    const data = {
        labels: e.map(m => m.continente),
        datasets: [
            {   
                data:e.map(m => m.n2019),
                borderWidth: 1,
                borderColor: styles.color.solids.map(eachColor => eachColor),
                backgroundColor: styles.color.alphas.map(eachColor => eachColor)
            }]}

    const options = {
          scales:{
            r:{ticks:{display:false}}
          }
        }

    new Chart(chartpieworld, { type: 'polarArea', data, options })
}


const barChartWorld = e => {

    const data = {
        labels: e.filter(m => m.anio === 2019).map(m => m.paises)[0],
        datasets: [{
            label: 'Emisiones GHG (MtCO₂e)',
            data: e.filter(m => m.anio === 2019).map(m => m.emisiones)[0],
            borderColor: styles.color.solids.map(eachColor => eachColor),
            backgroundColor: styles.color.alphas.map(eachColor => eachColor)
        }]}

    const options = {
        plugins:{
            legend:{display:false}
        }
        }

    new Chart(charttopbar, { type: 'bar', data, options })
}


const line1Chart = e => {

    const data = {
        labels: e.map(m => m.anio),
        datasets: [
            {
                label: 'Variación de temperatura',
                borderColor: styles.color.solids[3],
                data: e.map(m => m.MAT),
            }]}

    const options = {
        maintainAspectRatio: false,
        }

    new Chart(chartline1, { type: 'line', data, options })
}


const line2Chart = e => {
    const data = {
        labels: e.map(m => m.anio),
        datasets: [
            {
                label: 'Biocapacidad PerCápita',
                borderColor: styles.color.solids[5],
                data: e.map(m => m.biocapacidad),
            },
            {
                label: 'Ecológica PerCápíta',
                borderColor: styles.color.solids[4],
                data:e.map(m => m.huella_ecologica),
            }]}

    const options = {
        maintainAspectRatio: false,
        }

    new Chart(chartline2, { type: 'line', data, options })
}

linePredictionChart(prediccionMundial);
pieChartWorld(emisonescontinente);
barChartWorld(topPaises);
line1Chart(temperaturaMundial);
line2Chart(huellaMundial);

// ----------------------------------- country -------------------------------
const chartcountrybar = document.getElementById('chart5').getContext('2d');
const chartcountryradar = document.getElementById('chart6').getContext('2d');

let huellaactual,consumopais,produccionpais;
let radarrandom;
let barrandom;

const countryRadarChart = e => {
    
    if(radarrandom){
        radarrandom.destroy()
    }

    const data = {
        labels: ['Petróleo','Carbón','Gas Natural','Nuclear','Hidráulica','Solar','Eólica','Otros Renovables'],
        datasets: [{
            label: 'Energia (TW/h)',
            data: 
            [e.filter(m => m.anio == 2021).map(m => m.petroleo)[0],
            e.filter(m => m.anio == 2021).map(m => m.carbon)[0],
            e.filter(m => m.anio == 2021).map(m => m.gas)[0],
            e.filter(m => m.anio == 2021).map(m => m.nuclear)[0],
            e.filter(m => m.anio == 2021).map(m => m.hidraulica)[0],
            e.filter(m => m.anio == 2021).map(m => m.solar)[0],
            e.filter(m => m.anio == 2021).map(m => m.eolica)[0],
            e.filter(m => m.anio == 2021).map(m => m.otras_renovables)[0]],
            borderColor: styles.color.solids[0],
            backgroundColor: styles.color.alphas[0],
        }]}

    const options = {
        plugins: {legend: { display: false }},
        scales: {r: { ticks: { display: false }}},
        tooltips: {
            titleFontSize:1,
            bodyFontSize: 20,
          }}

    radarrandom = new Chart(chartcountryradar, { type: 'radar', data, options })
}

const countryBarChart = e => {

    if(barrandom){
        barrandom.destroy()
    }

    const data = {
        labels: ['Petróleo','Carbón','Gas Natural','Nuclear','Hidráulica','Solar','Eólica','Otros Renovables'],
        datasets: [{
            label: 'Energia (TW/h)',
            data: 
            [e.filter(m => m.anio == 2021).map(m => m.petroleo)[0],
            e.filter(m => m.anio == 2021).map(m => m.carbon)[0],
            e.filter(m => m.anio == 2021).map(m => m.gas)[0],
            e.filter(m => m.anio == 2021).map(m => m.nuclear)[0],
            e.filter(m => m.anio == 2021).map(m => m.hidraulica)[0],
            e.filter(m => m.anio == 2021).map(m => m.solar)[0],
            e.filter(m => m.anio == 2021).map(m => m.eolica)[0],
            e.filter(m => m.anio == 2021).map(m => m.otras_renovables)[0]],
            backgroundColor: styles.color.alphas,
            borderColor: styles.color.solids,
        }]}
    const options = {
            indexAxis: 'y',
            plugins:{
                legend:{display:false}
            }
          };

    barrandom = new Chart(chartcountrybar, { type: 'bar', data, options })
}

var mifuncion = function(parametro){

    huellaactual = huellapais.filter(m => m.codigo == parametro);
    consumopais = consumoenergiapais.filter(m => m.codigo == parametro);
    produccionpais = produccionenergiapais.filter(m => m.codigo == parametro);
    
    document.getElementById('pais_titulo').innerHTML = huellaactual.map(m => m.pais)
    document.getElementById('huellac_pais').innerHTML = huellaactual.map(m => m.huella_carbono)
    document.getElementById('huellae_pais').innerHTML = huellaactual.map(m => m.huella_ecologica)
    document.getElementById('bio_pais').innerHTML = huellaactual.map(m => m.biocapacidad)
    document.getElementById('tierra_pais').innerHTML = huellaactual.map(m => m.tierra)

    countryRadarChart(consumopais)
    countryBarChart(produccionpais)
    updateChart(consumopais,produccionpais,topPaises,emisonescontinente)
}
mifuncion('PER')
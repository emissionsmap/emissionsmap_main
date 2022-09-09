// parte de la personalización de los gráficos se tomaron de https://github.com/GarajedeIdeas/CodePills-VisualJS-CHARTJS
// como inspiración
const styles = {
    color: {
        solids: ['rgba(116, 72, 194, 1)', 'rgba(33, 192, 215, 1)', 'rgba(217, 158, 43, 1)', 'rgba(205, 58, 129, 1)', 'rgba(156, 153, 204, 1)', 'rgba(225, 78, 202, 1)',
        'rgba(116, 72, 194, 1)', 'rgba(33, 192, 215, 1)', 'rgba(217, 158, 43, 1)', 'rgba(205, 58, 129, 1)', 'rgba(156, 153, 204, 1)', 'rgba(225, 78, 202, 1)'],
        alphas: ['rgba(116, 72, 194, .5)', 'rgba(33, 192, 215, .5)', 'rgba(217, 158, 43, .5)', 'rgba(205, 58, 129, .5)', 'rgba(156, 153, 204, .5)', 'rgba(225, 78, 202, .5)',
        'rgba(116, 72, 194, .5)', 'rgba(33, 192, 215, .5)', 'rgba(217, 158, 43, .5)', 'rgba(205, 58, 129, .5)', 'rgba(156, 153, 204, .5)', 'rgba(225, 78, 202, .5)']
    }
}

// Defaults
Chart.defaults.global.defaultFontColor = '#fff'
Chart.defaults.global.elements.line.borderWidth = 1
Chart.defaults.global.elements.rectangle.borderWidth = 1
Chart.defaults.scale.gridLines.color = '#444'
Chart.defaults.scale.ticks.display = false

fetch('http://127.0.0.1:8000/api/historico_huella_mundial/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('biocapacidad').innerHTML = data.filter(m => m.anio === 2022).map(m => m.biocapacidad_percap)
        document.getElementById('huella').innerHTML = data.filter(m => m.anio === 2022).map(m => m.huella_ecologica_percap)
        document.getElementById('tierra').innerHTML = data.filter(m => m.anio === 2022).map(m => m.tierra)
    } )

fetch('http://127.0.0.1:8000/api/huella_actual_por_pais/')
    .then(response => response.json())
    .then(data => {
        document.getElementById('pais_titulo').innerHTML = data.filter(m => m.codigo === "PER").map(m => m.pais)
        document.getElementById('huellac_pais').innerHTML = data.filter(m => m.codigo === "PER").map(m => m.huella_carbono)
        document.getElementById('huellae_pais').innerHTML = data.filter(m => m.codigo === "PER").map(m => m.huella_ecologica)
        document.getElementById('bio_pais').innerHTML = data.filter(m => m.codigo === "PER").map(m => m.biocapacidad)
        document.getElementById('tierra_pais').innerHTML = data.filter(m => m.codigo === "PER").map(m => m.tierra)
    } )
   

const fetchCoastersData = (...urls) => {
    const promises = urls.map(url => fetch(url).then(response => response.json()))
    return Promise.all(promises)
}

fetchCoastersData('http://127.0.0.1:8000/api/temperatura/',
            'http://127.0.0.1:8000/api/electricidad_por_fuente/',
            'http://127.0.0.1:8000/api/fosil_renovable_nuclear/',
            'http://127.0.0.1:8000/api/historico_huella_mundial/',
            'http://127.0.0.1:8000/api/energia_co2/',)
.then(([temperatura,fuentes,fosil,huella,emision]) => {
    printCharts(temperatura,fuentes,fosil,huella,emision)
})

function printCharts(temperatura,fuentes,fosil,huella,emision) {

    // document.body.classList.add('running')
    radialChart('chart1')
    barChart( emision,'chart2')
    line1Chart(temperatura,'chart3')
    line2Chart(huella,'chart4')
    countryBarsChart(fuentes,'chart5')
    countryRadarChart(fosil,'chart6')
}

function radialChart(id) {

    const data = {
        labels: ['Asia', 'America', 'Europa', 'Africa', 'Oceania'],
        datasets: [
            {
                data:[10000,8000,6000,2000,4000],
                borderWidth: 1,
                borderColor: styles.color.solids.map(eachColor => eachColor),
                backgroundColor: styles.color.alphas.map(eachColor => eachColor)
            }
        ]
    }

    const options = {
        legend: {
            position: 'right'
        },
        tooltips: {
            callbacks: {
              title: function(tooltipItem, data) {
                return data['labels'][tooltipItem[0]['index']];
              },
              label: function(tooltipItem, data) {
                return data['datasets'][0]['data'][tooltipItem['index']];
              },
            },
            titleFontSize: 22,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'polarArea', data, options })
}

function barChart(emision, id) {

    const data = {
        labels: ['United States','China','Russia','Japan','India','Germany','Canada','Korea','Italy','Mexico'],
        datasets: [{
            data: [42,39,25,20,15,9,6,4,4,3],
            backgroundColor: styles.color.alphas,
            borderColor: styles.color.solids
        }]
    }

    const options = {
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                gridLines: {
                    display: false
                },
                ticks: {
                    display: true
                }
            }]
        },
        tooltips: {
            titleFontSize: 22,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'bar', data, options })

}


function line1Chart(temperatura,id) {
    const data = {
        labels: temperatura.map(m => m.anio),
        datasets: [
            {
                label: 'Variación de temperatura',
                borderColor: styles.color.solids[3],
                // backgroundColor: styles.color.solids[3],
                data: temperatura.map(m => m.temperatura_media),
            }]}

    const options = {
        maintainAspectRatio: false,
        scaleFontColor: '#fff',
        scales: {
            yAxes: [{
                ticks: {
                    display: true
                }
            }],
            xAxes: [{
                barPercentage: 0.4,
                ticks: {
                    display: true
                }
            }]},
        tooltips: {
            titleFontSize: 22,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'line', data, options })

}

function line2Chart(huella, id) {
    const data = {
        labels: huella.map(m => m.anio),
        datasets: [
            {
                label: 'Biocapacidad PerCápita',
                borderColor: styles.color.solids[5],
                data: huella.map(m => m.biocapacidad_percap),
            },
            {
                label: 'Huella Ecológica PerCápíta',
                borderColor: styles.color.solids[4],
                data:huella.map(m => m.huella_ecologica_percap),
            }
        ]
    }

    const options = {
        maintainAspectRatio: false,
        scaleFontColor: '#fff',
        scales: {
            yAxes: [{
                ticks: {
                    display: true
                }
            }],
            xAxes: [{
                barPercentage: 0.4,
                ticks: {
                    display: true
                }
            }]
        },
        tooltips: {
            titleFontSize: 22,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'line', data, options })

}

// country chart
function countryRadarChart(fosil,id) {
    
    const data = {
        labels: ['Combustibles Fósiles','Energias Renovables','Energia Nuclear'],
        datasets: [
            {
                label: 'Electricidad Producción fuente',
                data: [
                    fosil.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.combustibles_fosiles)[0],
                    fosil.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.renovables)[0],
                    fosil.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.nucelar)[0],
                ],
                borderColor: styles.color.solids[0],
                backgroundColor: styles.color.alphas[0]
            },
        ]
    }
    const options = {
        legend: {
            display:false
        },
        tooltips: {
            titleFontSize:1,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'radar', data, options })
}



function countryBarsChart(fuentes,id) {
    console.log(fuentes.filter(m => m.codigo === "AGO" && m.anio === 2020).map(m => m['petroleo','carbon']))
    const data = {
        labels: ['Petróleo','Carbón','Gas Natural','Nuclear','Hidráulica','Solar','Eólica','Otros Renovables'],
        datasets: [{
            label: 'Cantidad de emision',
            data: [
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.petroleo)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.carbon)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.gas)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.nuclear)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.hidro)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.solar)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.viento)[0],
                fuentes.filter(m => m.codigo === "PER" && m.anio === 2020).map(m => m.otras_renovables)[0]
            ],
            backgroundColor: styles.color.alphas,
            borderColor: styles.color.solids,
        }]
    }
    const options = {
        legend: {
            display: false
        },
        scales: {
            yAxes: [{
                gridLines: {
                    display: false
                },
                ticks: {
                    display: true
                }
            }]
        },
        tooltips: {
            titleFontSize:15,
            bodyFontSize: 20,
          }
    }

    new Chart(id, { type: 'horizontalBar', data, options })

}

printCharts()
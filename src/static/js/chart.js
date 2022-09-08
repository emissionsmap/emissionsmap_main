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


// fetch('https://api.com/')
//     .then(response => response.json())
//     .then(data => printCharts(data))

printCharts()
function printCharts() {

    // document.body.classList.add('running')
    radialChart( 'chart1')
    barChart( 'chart2')
    line1Chart( 'chart3')
    line2Chart('chart4')

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

function barChart(id) {


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


function line1Chart(id) {


    const data = {
        labels: ['1995-1997', '1998-2000', '2001-2003', '2004-2006', '2007-2009', '2013-2015', '2016-2018', '2019-2021'],
        datasets: [
            {
                label: 'Variación de co2',
                borderColor: styles.color.solids[5],
                data: [42,39,25,20,15,9,6,4,4]
            },
            {
                label: 'Variación de temperatura',
                borderColor: styles.color.solids[3],
                backgroundColor: styles.color.solids[3],
                data: [23,18,21,20,7,4,2,1,1]
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

function line2Chart(id) {

    const data = {
        labels: ['1995-1997', '1998-2000', '2001-2003', '2004-2006', '2007-2009', '2013-2015', '2016-2018', '2019-2021'],
        datasets: [
            {
                label: 'Variación de co2',
                borderColor: styles.color.solids[5],
                data: [13,18,13,10,9,9,8,12,6]
            },
            {
                label: 'Variación de temperatura',
                borderColor: styles.color.solids[4],
                data: [3,8,13,10,12,15,18,19,19]
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
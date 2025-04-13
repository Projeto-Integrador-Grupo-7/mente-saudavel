class Filter {
    onClickLimpar() {
        const filterForm = document.getElementById('filter-form');
    
        filterForm.reset();

        document.getElementById('filterDataInicio').value = '';
        document.getElementById('filterDataFim').value = '';
        document.getElementById('filterSexo').value = '';
        document.getElementById('filterIdade').value = '';

        filterForm.submit();
    }
}

class GraficoResultado {
    onLoad() {
        const graficoDadosElement = document.getElementById("graficoDadosJson");
        const graficoDados = JSON.parse(graficoDadosElement.textContent);

        const canvasContext = document.getElementById('graficoPizza').getContext('2d');
        new Chart(canvasContext, {
            type: 'pie',
            data: {
                labels: graficoDados.descricao,
                datasets: [{
                    label: 'Usuários',
                    data: graficoDados.valores,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(86, 255, 123, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(86, 255, 123, 1)',
                        'rgba(54, 162, 235, 1)',
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: false,
                plugins: {
                    legend: {
                        position: 'left',
                        labels: {
                            font: {
                                size: 14,
                                family: 'Arial',
                                weight: 'bold',
                            },
                            padding: 20,
                            boxWidth: 20,
                            boxHeight: 20,
                        }
                    },
                    tooltip: {
                        enabled: true,
                    },
                    datalabels: {
                        formatter: (value, context) => {
                            const total = context.chart.data.datasets[0].data.reduce((acc, val) => acc + val, 0);
                            const porcentagem = ((value / total) * 100).toFixed(1);
                            return `${porcentagem}%`;
                        },
                        color: 'rgb(61, 61, 61)',
                        font: {
                            size: 12,
                            weight: 'bold',
                        },
                        anchor: 'end',
                        align: 'start',
                        offset: 20,
                    }
                }
            },
            plugins: [ChartDataLabels]
        });
    }
}

const filter = new Filter();
const grafico = new GraficoResultado();
grafico.onLoad();

document.getElementById('btnLimpar').addEventListener('click', () => {
    filter.onClickLimpar();
});
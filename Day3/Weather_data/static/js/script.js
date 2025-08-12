// Expects Chart.js to be loaded (via CDN) and window.__WEATHER__ set by the template
(function () {
  if (!window.__WEATHER__) return;

  const { labels, temps, title } = window.__WEATHER__;
  const ctx = document.getElementById('tempChart');
  if (!ctx) return;

  // Simple Chart.js line chart
  // Chart.js API reference for line charts[13][15][7]
  new Chart(ctx, {
    type: 'line',
    data: {
      labels,
      datasets: [{
        label: title,
        data: temps,
        borderColor: 'rgba(37,99,235,1)',
        backgroundColor: 'rgba(37,99,235,0.15)',
        borderWidth: 2,
        tension: 0.25,
        pointRadius: 3,
        fill: true
      }]
    },
    options: {
      responsive: true,
      scales: {
        x: { title: { display: true, text: 'Time' } },
        y: { title: { display: true, text: '°C' }, beginAtZero: false }
      },
      plugins: {
        legend: { display: false },
        title: { display: false }
      }
    }
  });
})();

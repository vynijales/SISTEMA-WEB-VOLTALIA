function findIndexById(list, id) {
  for (let i = 0; i < list.length; i++) {
    if (list[i][2] == id) {
      return i;
    }
  }
  // Se o id não for encontrado, retorna -1
  return -1;
}

let setColorsBars = (value) => {
  // return "red"
  if (value <= 60) return "red"
  else if (value <= 80) return "yellow"
  else if (value <= 100) return "green"
  else return "blue"
}


mapboxgl.accessToken =
  "pk.eyJ1IjoidnluaWphbGVzIiwiYSI6ImNsZjh4YWo5bDBpaHMzcmtlZzM3MGJoZ2gifQ._Wm3t6w7QFppRKUvL6CXYA";

document.addEventListener('DOMContentLoaded', function () {

  // MAPBOX GL
  let data = {
    type: "FeatureCollection",
    features: coordinates.map((coordinate, index) => {
      return {
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: coordinate,
        },
        properties: {
          weight: weights[index],
        },
      };
    }),
  };

  let map = new mapboxgl.Map({
    container: "map",
    style: "mapbox://styles/mapbox/streets-v11",
    center: [45.34907, 16.90874],
    zoom: 5,
  });

  map.on("load", function () {
    // Adiciona o mapa de calor
    map.addLayer({
      id: "heatmap",
      type: "circle",
      source: {
        type: "geojson",
        data: data,
      },
      paint: {
        "circle-color": [
          "interpolate",
          ["linear"],
          ["get", "weight"],
          0,
          "hsl(0, 100%, 50%)",
          0.6,
          "hsl(60, 100%, 50%)",
          1,
          "hsl(120, 100%, 50%)",
        ],
        "circle-radius": {
          stops: [
            [0, 5],
            [2, 10],
            [4, 15],
            [6, 20],
            [8, 25],
          ],
        },
        "circle-opacity": 0.5,
        "circle-radius": 30,
      },
    });

    // Adiciona os marcadores
    coordinates.forEach((element, index) => {
      let marker = new mapboxgl.Marker().setLngLat(element).addTo(map);

      // Adiciona o pop-up ao clicar no marcador
      let popup = new mapboxgl.Popup({ offset: 25 }).setHTML(
        `ID: <a href="#container" class="nodecoration" style="text-decoration:none;">${element[2]}</a><br>Latitude: ${element[0]}<br>Longitude:${element[1]}<br>Performance: ${weights[index] * 100}%`
      );

      marker.setPopup(popup);
    });
    legend.style.display = "block";
  });

  // HIGHCHARTS
  let select = document.getElementById("floatingSelect");
  let opcaoTexto = select.options[select.selectedIndex].text;


  const chart = Highcharts.chart('container', {
    chart: {
      type: 'column', // Altera o tipo do gráfico para colunas verticais
      zoomType: 'xy' // Permite o zoom em ambos os eixos
    },
    title: {
      text: `Performance dos equipamentos`
    },
    xAxis: {
      categories: coordinates.map(element => element[2]), // Seta o valor do ID
      title: {
        text: 'ID'
      }
    },
    yAxis: {
      max: 100,
      title: {
        text: 'Performance (%)'
      }
    },
    series: [{
      name: opcaoTexto,
      data: weights.map(element => element * 100),
      dataLabels: {
        enabled: true,
        formatter: function () {
          if (this.y != 0) {
            return this.y.toFixed(2) + "%"
          };
        }
      }
    }],
    plotOptions: {
      column: { // Ajusta as opções de colunas
        dataLabels: {
          enabled: true
        },
        showInLegend: false, // Remove a legenda
        minPointLength: 10, // Seta o tamanho mínimo de píxels das colunas para 10
        point: {
          events: {
            click: function () {
              const zoom = 10;
              const id = this.category; // Pega o ID do ponto clicado
              const index = findIndexById(coordinates, id); // Encontra o índice em coordinates correspondente ao ID
              const lat = coordinates[index][0]; // Extrai a latitude
              const lng = coordinates[index][1]; // Extrai a longitude
              // Centraliza o mapa nas coordenadas encontradas
              map.setCenter([lat, lng]);
              map.setZoom(zoom);
              window.scrollTo(0, 0);

            }
          }
        }
      }
    },
    tooltip: {
      formatter: function () {
        return `<b>ID ${this.point.category} </b>: ${this.y.toFixed(2)}%`;
      }
    },
    credits: {
      enabled: false
    }
  });
});


function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

function getMonthlyData() {

  var queryUrl = `data.csv`;
  d3.json(queryUrl).then(function(data) {
    var otu_id = unpack(data.dataset.data, 0);
    var otu_label = unpack(data.dataset.data, 1);
    var s940 = unpack(data.dataset.data, 2);
    var s941 = unpack(data.dataset.data, 3);
    var s943 = unpack(data.dataset.data, 4);
    var s944 = unpack(data.dataset.data, 5);
    buildTable(otu_id, otu_label, s940, s941, s943, s944);
  });
}

function buildTable(otu_id, otu_label, s940, s941, s943, s944) {
  var table = d3.select("#summary-table");
  var tbody = table.select("tbody");
  var trow;
  for (var i = 0; i < 12; i++) {
    trow = tbody.append("tr");
    trow.append("td").text(otu_id[i]);
    trow.append("td").text(otu_label[i]);
    trow.append("td").text(s940[i]);
    trow.append("td").text(s941[i]);
    trow.append("td").text(s943[i]);
    trow.append("td").text(s944[i]);
  }
}

function buildPlot() {
  var url = `datacsv`;

  d3.json(url).then(function(data) {

    // Grab values from the response json object to build the plots
    //
    // var name = data.dataset.name;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;

    var otu_id = unpack(data.dataset.data, 0);
    var otu_label = unpack(data.dataset.data, 1);
    var s940 = unpack(data.dataset.data, 2);
    var s941 = unpack(data.dataset.data, 3);
    var s943 = unpack(data.dataset.data, 4);

    getMonthlyData();

    var trace1 = {
      type: "scatter",
      mode: "lines",
      name: 'namex',
      x: otu_id,
      y: s940,
      line: {
        color: "#17BECF"
      }
    };

    // Candlestick Trace
    var trace2 = {
      type: "candlestick",
      x: otu_id,
      high: s940,
      low: s941,
      open: s943,
      close: s944
    };

    var data = [trace1, trace2];

    var layout = {
      title: `${otu_id} otu-id`,
      xaxis: {
        range: [startDate, endDate],
        type: "date"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      },
      showlegend: false
    };

    Plotly.newPlot("plot", data, layout);

  });
}

buildPlot();

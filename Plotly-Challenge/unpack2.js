
function unpack(rows, index) {
  return rows.map(function(row) {
    return row[index];
  });
}

// Submit Button handler
function handleSubmit() {
  // Prevent the page from refreshing
  d3.event.preventDefault();

  // Select the input value from the form
  var sample = d3.select("#sampleInput").node().value;
  console.log(sample);

  // clear the input value
  d3.select("#sampleInput").node().value = "";

  // Build the plot with the new sample
  buildPlot(sample);
}

function buildPlot(sample) {
  var sample = "940";

  var url = `data.csv`;
  x=d3.json(url);
  console.log(x);

  d3.json(url).then(function(data) {

    // Grab values from the response json object to build the plots
     var name = sample;
    // var stock = data.dataset.dataset_code;
    // var startDate = data.dataset.start_date;
    // var endDate = data.dataset.end_date;

    var otu_id = unpack(data.dataset.data, 0);
    var otu_label = unpack(data.dataset.data, 1);
    var s940 = unpack(data.dataset.data, 2);
    var s941 = unpack(data.dataset.data, 3);
    var s943 = unpack(data.dataset.data, 4);
    var s944 = unpack(data.dataset.data, 5);
    console.log('----------------');
    console.log('s940',s940);

    var trace1 = {
      type: "scatter",
      mode: "lines",
   //   name: name,
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
      high: s943,
      low: s941,
      open: s940,
      close: s944
    };

    var data = [trace1, trace2];

    var layout = {
      title: `${sample} is selected sample`,
      xaxis: {
        range: [1, 3667],
        type: "linear"
      },
      yaxis: {
        autorange: true,
        type: "linear"
      }
    };

    Plotly.newPlot("plot3", data, layout);
  });
}

// Add event listener for submit button
d3.select("#submit").on("click", handleSubmit);

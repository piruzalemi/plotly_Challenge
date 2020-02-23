const url = "dataSamples.json";

// Fetch the JSON data and console log it
d3.json("dataSamples.json").then(function(data) {
  console.log('Surprise This section occurs after inialization!')
  console.log(data);
});

// Promise Pending
const dataPromise = d3.json(url);
console.log("Data Promise: ", dataPromise);

  // ------------------------------------------
  // function that builds the metadata panel
  // -------------------------------------------

var wfreqGlobal = 20;
function buildMetadata(sample, z) {
  console.log("____entered function buildMetadata___")
  console.log('sample:', sample)
  // Use `d3.json` to fetch the metadata for a sample
  d3.json(url).then(function(m_data) {
    console.log(m_data);

    var mData = m_data.metadata;
    // -------------------------------------------  
    //          F I L T E R
    // -------------------------------------------
    var results=mData.filter(obj=>obj.id==sample);
    var results1=results[0];
    id =results1.id
    wfreqGlobal=results1.wfreq * 10
    console.log("meta data id:.........>", id)
    console.log("meta data wfreq:.........>", wfreqGlobal)
    
    console.log(results);
    console.log("results1:", results1);
    //console.log(results1.ethnicity);
    
    console.log("hey I am in meta data building results1 for boxpanel!!!");

    // Used d3 to select the panel with id of `#sample-metadata`    
    var boxpanel = d3.select('#sample-metadata');

    // Used `.html("") to clear any existing metadata
    boxpanel.html("");
    // ------------------------------------------------
    //                    L o o p:   
    //  Used `Object.entries` to add each key and 
    //           value pair to the panel
    // ------------------------------------------------
    Object.entries(results1).forEach(([key,value])=>[  
      boxpanel.append("p").text(key + ": " + value)
    ])

  });
  // --------------------------------------------------------
  // Hint: Inside the loop, you will need to use d3 to append new
  // tags for each key-value in the metadata.

  // BONUS: Build the Gauge Chart
  // buildGauge(data.WFREQ);
}

function buildCharts(sample) {
  // Piruz Code -------
  // @TODO: Use `d3.json` to fetch the sample data for the plots
  // Samples like 940, 941, etc. have 3 keys:
  //   otu-ids
  //   sample-Values
  //   otu_labels
  console.log("Hi1.........................You are in buildCharts ..............")
  d3.json(url).then((data) => {

    var sdata = data;
    console.log(data)
    // --------------------------------------------------------
    //        G E T     T H E    N E C.    D A T A
    // -------------------------------------------------------

  //console.log(newSample)  
  //??????
  var len = data.samples.length;
  console.log("1: len", len)
  console.log("2: sample", sample)
  
  for (i = 0; i < len; i++) {
    if (data.samples[i].id == sample){

      var ds_Id=data.samples[i].id
      var ds_otu_ids=data.samples[i].otu_ids
      var ds_sample_values=data.samples[i].sample_values
      var ds_otu_labels=data.samples[i].otu_labels
      console.log ("ds_id:********", ds_Id)
      console.log("ds_sample_values*****",ds_sample_values)

    }}

  // var ds=data.samples
  // var ds_Id=data.samples[0].id
  // var ds_otu_ids=data.samples[0].otu_ids
  // var ds_sample_values=data.samples[0].sample_values
  // var ds_otu_labels=data.samples[0].otu_labels

  //sdata = unsorted_data.slice(0, 10);
  
  var s_otu_ids= ds_otu_ids.slice(0,10);
  var s_otu_labels= ds_otu_labels.slice(0,10);
  var ssamples= ds_sample_values.slice(0,10);
 
   // ----------------------------------------------------------
   //                       P L O T
   // ----------------------------------------------------------
   // Trace1 for the SAMPLE Data
   var trace1 = {
     //x: sotu.map(row => row.ssamples),
     x: ssamples,
     y: s_otu_ids.map(s_otu_id => 'otu--' + s_otu_id ),
     //y: sdata.map(row => row.s_otu_ids),
     //text: sdata.map(row => row.s_otu_labels),
     name: "OTU SAMPLES",
     type: "bar",
     orientation: "h"
   };
 
   // data
   var chartData = [trace1];
 
   // Apply the group bar mode to the layout
   var layout = {
     title: `Alemi Bio Diversity Plot for: ${sample}`,
     margin: {
       l: 100,
       r: 100,
       t: 100,
       b: 100
     }
   };
 
   // Render the plot to the div tag with id "plot"
   Plotly.newPlot("plot", chartData, layout);


   var trace1 = {
    x: ssamples,
    y: s_otu_ids,
    mode: 'markers',
    marker: {
      color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
      opacity: [1, 0.8, 0.6, 0.4],
      size: [40, 60, 80, 100]
    }
  };
  
  var data = [trace1];
  
  var layout = {
    title: `Alemi Bubble Responsive! - ${sample} OTU Sample:`,
    showlegend: false,
    height: 600,
    width: 600
  };
  
  Plotly.newPlot('bubble', data, layout, {responsive: true})

  //wfreqGlobal=results1.wfreq * 10
  console.log("wfreqGlobal for chart...............:", wfreqGlobal)

  var data = [
    {
      domain: { x: [0, 1], y: [0, 1] },
      value: wfreqGlobal,
      title: { text: "Wash Freq * 10 factor" },
      type: "indicator",
      mode: "gauge+number"
    }
  ];
  
  var layout = { width: 300, height: 250, margin: { t: 0, b: 0 } };
  Plotly.newPlot('gauge', data, layout);
 
    // @TODO: Build a Bubble Chart using the sample data
    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 
    // sample_values, otu_ids, and labels (10 each).
});
}

function init() {
  // Grab a reference to the dropdown select element
  console.log("______ Initialized ________")
  var wfreqGlobal = 50;
  var selector = d3.select("#selDataset");

  // -----------------------------------------------------------
  // Use the list of data names to populate the select options
  //                                      Piruz Alemi 02/21/2020
  //  "names":["940", "941", "943", "944", "945",...]
  //  Note Sample names are the above values like 940, 943...
  //  We read the data, and "names" is a key in a dictionary with an array
  //                         of sample values. each sample is like 940
  // -----------------------------------------------------------
  //  GET The first data set name: names
  d3.json(url).then((data) => {
    var sn=data.names
    // console.log("sn:",sn)
    //                   Loop:
    //                   Load the Table with Sample values
    sn.forEach((sample) => {
      //console.log("samples:", sample)
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });
    // ---------------------------------------------------------------
    // Use the first sample from the list to build the initial plots
    // ---------------------------------------------------------------
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    //const firstSample = data[0];
    const firstSample = data.names[0];
    var ds=data.samples
    var ds_Id=data.samples[0].id
    var ds_otu_ids=data.samples[0].otu_ids
    var ds_sample_values=data.samples[0].sample_values
    var ds_otu_labels=data.samples[0].otu_labels
    console.log("______ loaded the table ________")
    console.log("First Sample:", firstSample)
    buildMetadata(firstSample);
    buildCharts(firstSample);
    
});
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  console.log("_________   Entered function optionChanged       _______")
  console.log("_________ * * *  a new sample is selected  * * * _______")
  var selector = d3.select("#selDataset");
 
  d3.json(url).then((data2) => {

    var sn2=data2.samples
    var i;
    var len = sn2.length;
    console.log("length:", len)
    // ------------------------------------------------------
    //                    L O O P:
    //     Find the relevant data for the newSample selected
    // ------------------------------------------------------
    // ???????      ???????????
    for (i = 0; i < len; i++) {
      if (data2.samples[i].id == newSample){
        console.log(true)
        console.log('counter, newSample:---->',i, newSample)
        console.log(data2.samples[i])

        var ds_Id=data2.samples[i].id
        var ds_otu_ids=data2.samples[i].otu_ids
        var ds_sample_values=data2.samples[i].sample_values
        var ds_otu_labels=data2.samples[i].otu_labels
        console.log("newSample:", newSample)
        buildMetadata(newSample);
        buildCharts(newSample);
        

      }
    }
    // ---------------------------------------------------------------
    // !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    //const firstSample = data[0];
    // var ds=data2.samples
    // var ds_Id=data2.samples[0].id
    // var ds_otu_ids=data2.samples[0].otu_ids
    // var ds_sample_values=data2.samples[0].sample_values
    // var ds_otu_labels=data2.samples[0].otu_labels
    // console.log("______ New Sample ________")
    // console.log("new Sample---------------------------:", newSample)
    // buildCharts(firstSample);
    // buildMetadata(firstSample);
});

  // buildCharts(newSample);
  // console.log(".......Next Function output............")
  // buildMetadata(newSample);
};

// Initialize the dashboard
init();

// -----------------------------------------------------------------------
    //console.log("Hi2....You read Json data in buildCharts..............")
    // console.log("Piruz Code on ds", ds)
    // console.log("Piruz Code on ds_Id:", ds_Id)
    // console.log("Piruz Code on ds_otu_Ids:", ds_otu_ids)
    // console.log("Piruz Code on ds_otu_sample_values:", ds_sample_values)
   // console.log("Piruz Code on ds_otu_labels:", ds_otu_labels)
   
   //let unsorted_data = { "2010-01": { "item1": 324, "item2": 1075, "item3": 940, "item4": 441, "item5": 1040, "item6": 898, "item7": 1343 }, "2011-02": { "item1": 295, "item2": 958, "item3": 904, "item4": 434, "item5": 1038, "item6": 793, "item7": 1246 }, "2012-03": { "item1": 314, "item2": 1062, "item3": 980, "item4": 494, "item5": 1158, "item6": 914, "item7": 1461 }, "2008-04": { "item1": 336, "item2": 1022, "item3": 987, "item4": 488, "item5": 1014, "item6": 792, "item7": 1382 }, "2007-05": { "item1": 332, "item2": 1073, "item3": 1002, "item4": 512, "item5": 1104, "item6": 840, "item7": 1368 }, "2005-06": { "item1": 311, "item2": 981, "item3": 837, "item4": 432, "item5": 1002, "item6": 801, "item7": 1265 }, "2014-07": { "item1": 321, "item2": 1049, "item3": 921, "item4": 489, "item5": 963, "item6": 881, "item7": 1340 }, "2015-08": { "item1": 294, "item2": 1071, "item3": 960, "item4": 506, "item5": 910, "item6": 885, "item7": 1312 }, "2016-09": { "item1": 281, "item2": 1020, "item3": 952, "item4": 502, "item5": 1068, "item6": 914, "item7": 1397 }, "2009-10": { "item1": 319, "item2": 1058, "item3": 985, "item4": 546, "item5": 1184, "item6": 1031, "item7": 1448 }, "2005-11": { "item1": 300, "item2": 1021, "item3": 967, "item4": 474, "item5": 1176, "item6": 1009, "item7": 1387 }, "2017-12": { "item1": 307, "item2": 1027, "item3": 924, "item4": 427, "item5": 1024, "item6": 844, "item7": 1300 } };
   
  // ----------------------------------------------------
  //             S O R T        F U N C T I O N
  // ----------------------------------------------------
  //  let unsorted_data = data.samples[0].sample_values
  //  console.log('UNsorted data:........', unsorted_data)
  //  function sortData(key, data, type) {
  //    console.log("_____sort the data ______")
  //    let ordered = [];
  //    let compareFunction = function(a, b) {
  //      return data[b][key] - data[a][key];
  //    };
  //    if (type === "asc") {
  //      compareFunction = function(a, b) {
  //        return data[a][key] - data[b][key];
  //      }
  //    }
  //    Object.keys(data).sort(compareFunction).forEach(function(key) {
  //      ordered[key] = data[key];
  //    });
  //    console.log("ordered data:", ordered)
  //    console.log(data[0])
  //    return ordered;
  //  }
   
   // console.log(sortData("item1", unsorted_data, 'asc'));
   //console.log('sortdata:', sortData("0", unsorted_data, 'asc'));

   // var sorted = sortData("sample_values", unsorted_data, 'asc')
   //console.log(typeof sorted)
  // Slice the first 10 objects for plotting
  // -----------------------------------------------------------
  //                 S   L   I   C   E
  // -----------------------------------------------------------
  //console.log("ORD:..............",sorted)

 // var ds_otu_ids=data.samples[0].otu_ids
 // var ds_sample_values=data.samples[0].sample_value
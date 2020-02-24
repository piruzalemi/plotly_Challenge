const urld = "data.csv";

// Get OTU Data
// Fetch the JSON data and console log it
d3.csv(urld).then(function(data) {
  console.log(data);
});

// Promise Pending
const dataPromise = d3.csv(urld);
console.log(dataPromise);


d3.csv(urld).then(function(otudata) {
  for (var i = 0; i < otudata.length; i++) {
      console.log(otudata[i]['otu_id']);
      console.log(otudata[i]['otu_label']);
      console.log(otudata[i].otu_label);
  }
});





//    ---------------------
//       Get Meta Data
//    ---------------------

const urlmeta = "metadata.csv";

// Fetch the JSON data and console log it
d3.csv(urlmeta).then(function(metadata) {
  console.log(metadata[5]['sample']);
  console.log(metadata[5]['WFREQ']);
});

// Promise Pending
const dataPromise2 = d3.csv(urlmeta);
console.log('promise2:', dataPromise2);


d3.csv(urlmeta).then(function(metadata) {
    for (var i = 0; i < metadata.length; i++) {
        console.log(metadata[i]['sample']);
        console.log(metadata[i]['WFREQ']);
        console.log(metadata[i].WFREQ);
    }
});

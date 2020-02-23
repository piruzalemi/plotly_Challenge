const CSVToJson = require("csvtojson");
const FileSystem = require("fs");

CSVToJson().fromFile("./source.csv").then(source =>{
console.log(source)
});

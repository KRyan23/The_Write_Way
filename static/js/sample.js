function add_reversed_data_from_js() {
    let list_data2 = list_data.push("test_input_from_js");

    document.getElementById("output_from_js").innerHTML = "from_js:" + list_data2;
 }

function add_data_from_js() {
 document.getElementById("output_from_js2").innerHTML = "from_js_original:" + list_data;

}
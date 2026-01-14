function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(uiBathrooms[i].value);
        }
    }
    return -1;
}

function getBHKValue() {
    var uiBHK = document.getElementsByName("uiBHK");
    for (var i in uiBHK) {
        if (uiBHK[i].checked) {
            return parseInt(uiBHK[i].value);
        }
    }
    return -1;
}

const baseURL = "";


async function onClickedEstimatePrice() {
    let sqft = document.getElementById("uiSqft").value;
    let bhk = getBHKValue();
    let bathrooms = getBathValue();
    let location = document.getElementById("uiLocations").value;

    if (!sqft || !location || bhk === -1 || bathrooms === -1) {
        alert("Please fill all fields properly.");
        return;
    }

    let response = await fetch(`${baseURL}/predict_home_price`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            total_sqft: sqft,
            bhk: bhk,
            bath: bathrooms,
            location: location
        })
    });

    let data = await response.json();
    let estPrice = data.estimated_price;

    document.getElementById("uiEstimatedPrice").innerHTML = `<h2>₹ ${estPrice} Lakhs</h2>`;
}

async function onPageLoad() {
    let response = await fetch(`${baseURL}/get_location_names`);

    let data = await response.json();
    let locations = data.locations;
    let uiLocations = document.getElementById("uiLocations");

    uiLocations.innerHTML = '<option disabled selected>Select a Location</option>';

    locations.forEach(loc => {
        let opt = document.createElement("option");
        opt.value = loc;
        opt.innerHTML = loc;
        uiLocations.appendChild(opt);
    });
}

window.onload = onPageLoad;



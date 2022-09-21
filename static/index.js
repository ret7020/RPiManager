function getReqApi(api_endpoint){
    return fetch(api_endpoint)
    .then(data => {
        return data.json();
    });
}

// Update interval
const interval = setInterval(function() {
    getReqApi('/api/poll_metrics').then(function(resp){
        if (resp["status"]){
            document.getElementById("metrics_table").innerHTML = resp["html_table"];
        }
    })
  }, 3000);
 
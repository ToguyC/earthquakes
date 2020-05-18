// Replace view data with all the data retrieved with the filters, offset and limit
function UpdateData(start, limit, filterQuery="") {
    $.ajax({
        url: '/get/' + start + '/' + limit,
        type: 'POST',
        data: {
            'start': start,
            'limit': limit,
            'filterQuery': filterQuery
        },
        success: (res) => {
            // Update pagination
            if (res.earthquakes.length > 0)
                $('.pagination-page').pagination('updateItems', res.earthquakes[0]["count"]);
            else
                $('.pagination-page').pagination('updateItems', 1);

            // Clear and insert of all data
            $("#earthquake-group").html("");
            for (let i = 0; i < res.earthquakes.length; i++) {
                $("#earthquake-group").append(
                    `<div class="card col-4" onclick="SetupMap(${res.earthquakes[i]["longitude"]}, ${res.earthquakes[i]["latitude"]})">
                        <div class="card-body">
                            <h6 class="card-title">${res.earthquakes[i]["title"]}</h6>
                            <p class="card-text">
                                ${res.earthquakes[i]["mag"]}, ${TimestampToDate(res.earthquakes[i]["time"])}, <a href="${res.earthquakes[i]["detail"]}">Detail</a>
                                ${res.earthquakes[i]["alert"]}, ${res.earthquakes[i]["status"]}, ${res.earthquakes[i]["tsunami"]}, ${res.earthquakes[i]["type"]}
                            </p>
                        </div>
                    </div>`
                );
            }
        },
        error: (err) => {
            console.log(err);
        }
    });
}
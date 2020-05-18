// Create the filter query and update the view
function SetFilter(start, limit) {
    let sort = $('#sort').val();
    let type = $('#type').val();
    let automatic = $('#automaticStatus')[0].checked;
    let reviewed = $('#reviewedStatus')[0].checked;
    let filterQuery = "";
    let statusList = "("; // Begining of the "IN" status array
    
    filterQuery += "WHERE type LIKE '" + type + "'";

    // Add the delected status in the "IN" aray
    if (automatic)
        statusList += "'automatic',";
    else
        statusList += "'',";

    if (reviewed)
        statusList += "'reviewed'";
    else
        statusList += "''";
    
    statusList += ")"

    filterQuery += " AND status IN " + statusList;

    filterQuery += " ORDER BY " + sort;
    
    // Update view
    UpdateData(start, limit, filterQuery);
}
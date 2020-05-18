// Convert timestamp with milliseconds in date with the format (YYYY.MM.DD HH:mm:SS)
function TimestampToDate(timestamp) {
    timestamp = String(timestamp);
    timestamp = timestamp.substring(0, timestamp.length - 3) + '000'; // Delete milliseconds
    timestamp = Number(timestamp);
    let date = new Date(timestamp);

    let year = date.getFullYear();
    let month = String("00" + (date.getMonth()+ 1)).slice(-2); // Month start at 0 and end at 11
    let day = String("00" + date.getDay()).slice(-2);

    let hour = String("00" + date.getHours()).slice(-2);
    let minutes = String("00" + date.getMinutes()).slice(-2);
    let seconds = String("00" + date.getSeconds()).slice(-2);

    return `${year}.${month}.${day} ${hour}:${minutes}:${seconds}`;
}
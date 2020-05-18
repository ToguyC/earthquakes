function overrideData() {
    $.ajax({
        url: '/override',
        type: 'POST',
        data: {},
        success: (res) => {
            console.log(res);
        },
        error: (err) => {
            console.log(err);
        }
    });
}
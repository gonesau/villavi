$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action':'searchdata'
            }, // parametros
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "desc"},
            {"data": "desc"},
        ],
        columnDefs: [
            {
                targets: [3],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/category/update/'+row.id+'/" class="btn btn-success btn-sm"><i class="far fa-edit"></i></a>';
                    buttons += '<a href="/erp/category/delete/'+row.id+'/" class="btn btn-danger btn-sm"><i class="far fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});
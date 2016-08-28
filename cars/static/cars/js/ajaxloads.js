/**
 * Created by Boris on 23.08.16.
 */
$(document).ready(function () {
    var brandSelect = $('.brand-select');
    var modelSelect = $('.model-select');
    var yearSelect = $('.year-select');
    var modificationSelect = $('.modification-select');
    brandSelect.change(function (event) {
        var target = $(event.target);
        $.get(
           target.data('url'),
           {
               brand_id: target.val()
           }
        ).done(function (data) {
           modelSelect.empty();
           modificationSelect.empty();
           $.each(data["models"], function(key, value) {
               modelSelect.append($("<option></option>").attr("value", value.id).text(value.name));
           });
           modelSelect.trigger('change');
        })
    });
    modelSelect.change(function (event) {
        var target = $(event.target);
        $.get(
            target.data('url'),
            {
                model_id: target.val()
            }
        ).done(function (data) {
            yearSelect.empty();
            $.each(data['years'], function (key, value) {
                yearSelect.append($("<option></option>").attr("value", value + "," + target.val()).text(value));
            });
            yearSelect.trigger('change');
        })
    });
    yearSelect.change(function (event) {
        var target = $(event.target);
        var val = target.val().split(',');
        $.get(target.data('url'),
            {
                year: val[0],
                model_id: val[1]
            }
        ).done(function (data) {
            modificationSelect.empty();
            $.each(data['modifications'], function (key, value) {
                modificationSelect.append($("<option></option>").attr("value", value.id).text(value.name));
            })
        })
    });
    brandSelect.trigger('change');
});
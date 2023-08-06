// Copyright (c) 2023, manish kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Car', {
    // refresh: function(frm) {

    // }
});
frappe.listview_settings['Car'] = {
    get_indicator(doc) {
        // customize indicator color
        if (doc.status === 'In Stock') {
            return [__("In Stock"), "green", "status,=,In Stock"];
        } else {
            return [__("Sold"), "red", "status,=,Sold"];
        }
    },

}

// frappe.listview_settings['Car'] = {
//     add_fields: ["status"],
//     get_indicator: function(doc) {
//         return [__(doc.status), {
//             "In Stock": "green",
//             "Sold": "red",
//         }[doc.status], "status,=," + doc.status];
//     }
// };
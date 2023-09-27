frappe.ui.form.on('Item', {
    refresh: function(frm) {
        // Add a custom button to generate and display the barcode
        frm.add_custom_button(__('Generate Barcode'), function() {
            // Replace with your code to generate and save the barcode image
            frappe.call({
                method: 'carsale.python_script.item.generate_barcode',
                args: {
                    item_code: frm.doc.item_code
                },
                callback: function(r) {
                    if (r.message && r.message.barcode_image) {
                        // Set the barcode image field with the generated image
                        frm.set_value('barcode_image', r.message.barcode_image);
                        frm.refresh_field('barcode_image');
                    } else {
                        frappe.msgprint(__('Failed to generate barcode.'));
                    }
                }
            });
        });
    }
});
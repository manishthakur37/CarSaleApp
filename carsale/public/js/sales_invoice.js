frappe.ui.form.on('Sales Invoice', {
    refresh: function(frm) {
        // Check if the invoice is unpaid
        if (frm.doc.docstatus === 1 && frm.doc.outstanding_amount > 0) {
            // Check if the Target Exchange Rate is filled
            if (!frm.doc.conversion_rate) {
                frappe.msgprint(__('Please fill the Target Exchange Rate before proceeding with online payment.'));
                return;
            }

            // Add the custom button to the toolbar
            frm.add_custom_button(__('Pay Online'), function() {
                frappe.call({
                    method: 'carsale.python_script.sales_invoice_extension.process_online_payment',
                    args: {
                        docname: frm.doc.name
                    },
                    callback: function(response) {
                        var payment_link = response.message.payment_link;
                        if (payment_link) {
                            // Fetch and display the payment amount from the Sales Invoice
                            var paymentAmount = frm.doc.grand_total;
                            var paymentPrompt = `You are about to pay ₹${paymentAmount} online. Do you want to proceed?`;

                            // Display a confirmation prompt with the payment amount
                            if (confirm(paymentPrompt)) {
                                // Open the payment link in a new tab
                                window.open(payment_link, '₹${paymentAmount}');

                                // Create a Payment Entry after successful payment
                                frappe.call({
                                    method: 'carsale.python_script.sales_invoice_extension.create_payment_entry',
                                    args: {
                                        docname: frm.doc.name,
                                        amount: paymentAmount
                                    },
                                    callback: function(response) {
                                        // Handle the response as needed
                                        if (response.message && response.message.success) {
                                            // Update the Sales Invoice status to "Paid"
                                            frappe.model.set_value(frm.doctype, frm.docname, 'status', 'Paid');
                                            frm.refresh_field('status');
                                            frappe.msgprint(__('Sales Invoice status updated to "Paid".'));
                                        }
                                    }
                                });
                            }
                        } else {
                            frappe.msgprint(__('Failed to generate payment link.'));
                        }
                    }
                });
            });
        }
    }
});
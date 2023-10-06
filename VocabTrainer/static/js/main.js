          // Check if there is a flash message with the class 'message'
    $(document).ready(function() {
        $('#check-button').click(function(e) {
            e.preventDefault(); // Prevent the default button click behavior
            $('form').submit(); // Trigger the form submission
        });

        $('form').submit(function(e) {
            e.preventDefault(); // Prevent the form from submitting normally
            sendAjaxRequest(); // Call a function to send the AJAX request
        });

        // Add an event listener for the "Enter" key press
        $('form').on('keyup keypress', function(e) {
            var keyCode = e.keyCode || e.which;
            if (keyCode === 13) { // 13 is the key code for "Enter"
                e.preventDefault(); // Prevent the default form submission
                sendAjaxRequest(); // Call a function to send the AJAX request
            }
        });

        function sendAjaxRequest() {
            // Send an AJAX request to your server
            $.ajax({
                type: 'POST',
                url: '', // Your form submission URL
                data: $('form').serialize(), // Serialize the form data
                dataType: 'json', // Expect JSON response
                success: function(data) {
                    // Display the response message
                    $('.message').text('')
                    $('.message').text(data.message);

                    if (data.is_correct) {
                        // Redirect to the next page after a delay
                        setTimeout(function() {
                            window.location.href = data.redirect_url;
                        }, 1500); // Adjust the delay as needed
                    }
                }
            });
        }
    });

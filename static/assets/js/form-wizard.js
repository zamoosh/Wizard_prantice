(function($) {
    "use strict";
    
    // WIZARD 1
    $('#wizard1').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>'
    });

    // WIZARD 2
    
    $.fn.steps.setStep = function (step) {
        var currentIndex = $(this).steps('getCurrentIndex');
        for (var i = 0; i < Math.abs(step - currentIndex); i++) {
            if (step > currentIndex) {
                $(this).steps('next');
            } else {
                $(this).steps('previous');
            }
        }
    };
    
    
    $(window).on('load', function () {
        $("#wizard2").steps({
            headerTag: 'h3',
            bodyTag: 'section',
            autoFocus: true,
            enableAllSteps: true,
            titleTemplate: `<span class="number">#index#</span> <span class="me-4">#title#</span>`,
            
            onFinished: function () {
                alert('finish!');
            },
            
            labels: {
                finish: "پایان",
                next: "ادامه",
                previous: "قبلی"
            },
            
            onStepChanging: function(event, currentIndex, newIndex) {
                if (currentIndex < newIndex) {

                    // Step 1 form validation
                    if (currentIndex === 0) {
                        let cellphone = $('#cellphone').parsley();
                        if (cellphone.isValid())
                            return true;
                        else {
                            cellphone.validate();
                            $('.parsley-required').html('این قسمت الزامی است');
                        }
                    }

                    // Step 2 form validation
                    if (currentIndex === 1) {
                        return true;
                        let first_name = $('#first_name').parsley();
                        let last_name = $('#last_name').parsley();
                        if (first_name.isValid() && last_name.isValid()) {
                            return true;
                        } else {
                            first_name.validate();
                            last_name.validate();
                        }
                    }

                    // Step 3 form validation
                    if (currentIndex === 2) {
                        return true;
                        let email = $('#email').parsley();
                        if (email.isValid()) {
                            return true;
                        } else {
                            email.validate();
                        }
                    }
                    // Always allow step back to the previous step even if the current step is not valid.
                } else {
                    return true;
                }
            }
        });
        $("#wizard2").steps('add', {
            title: "HTML code",
            content: "<strong>HTML code</strong>"
        });
        // $("#wizard2").steps('setStep', 0);
    });

    // WIZARD 3
    $('#wizard3').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
        stepsOrientation: 1
    });

    // DROPIFY
    $('.dropify-clear').on('click', function () {
        $('.dropify-render img').remove();
        $(".dropify-preview").css("display", "none");
        $(".dropify-clear").css("display", "none");
    });

    // ACCORDION WIZARD
    var options = {
        mode: 'wizard',
        autoButtonsNextClass: 'btn btn-primary float-end',
        autoButtonsPrevClass: 'btn btn-light',
        stepNumberClass: 'badge rounded-pill bg-primary me-1',
        onSubmit: function() {
            alert('Form submitted!');
            return true;
        }
    }
    $("#form").accWizard(options);

})(jQuery);

//Function to show image before upload

function readURL(input) {
    'use strict'
    
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('.dropify-render img').remove();
            var img = $('<img id="dropify-img">'); //Equivalent: $(document.createElement('img'))
            img.attr('src', e.target.result);
            img.appendTo('.dropify-render');
            $(".dropify-preview").css("display", "block");
            $(".dropify-clear").css("display", "block");
        };
        reader.readAsDataURL(input.files[0]);
    }
}
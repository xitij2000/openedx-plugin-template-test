//This is a test js file
let slot = $("#test-template-plugin-script").data('slot');
console.log(`Injecting script into "${slot}"`);

$(function(){
    $("a").mouseover(function(element){
        console.log('mousingover');
        $(element.target).fadeOut(
            function(){
                $(element.target).fadeIn();
            }
        );
    });
})


(function(){

    /* <textarea> resize script attributed to George Papadakis @ 
    /* http://georgepapadakis.me/demo/expanding-textarea.html */
    /*
    /* Code actually found @
    /* http://chuvash.eu/2011/12/14/the-cleanest-auto-resize-for-a-textarea/ */


    /* While this script is cool in it's functionality it only addresses the first
       textarea in any given document. This is not acceptable.
       A for loop needs to be written that will allow the targeting of all textarea elements
       on any given page and provide the auto-resize functionality that this script promises. */
    
    window.onload = function() {
        var t = document.getElementsByTagName('textarea')[0];
        var offset= !window.opera ? (t.offsetHeight - t.clientHeight) : (t.offsetHeight + parseInt(window.getComputedStyle(t, null).getPropertyValue('border-top-width'))) ;
     
        var resize  = function(t) {
            t.style.height = 'auto';
            t.style.height = (t.scrollHeight  + offset ) + 'px';    
        }
     
        t.addEventListener && t.addEventListener('input', function(event) {
            resize(t);
        });
     
        t['attachEvent']  && t.attachEvent('onkeyup', function() {
            resize(t);
        });
    }


    /* Date Picker by jQuery UI */

    $(function() {
        $( "#datepicker" ).datepicker();
    });

}());


   


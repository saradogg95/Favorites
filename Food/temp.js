"use strict";
function calculate(e){
    var t=e.querySelectorAll("input[type=text]"),
    a=t[0].value.replace(",","."),c=t[1].value.replace(",","."),
    n=0,
    r=!1;
    if(t[0].style.background="#fff",
    t[1].style.background="#fff",
    t[2].value="",
    isNumber(a)||(t[0].style.background="#fee",r=!0),isNumber(c)||(t[1].style.background="#fee",r=!0),r)
    return!1;
    switch(e.getAttribute("id"))
    {
    case"f1":n=a/100*c;break;
    case"f2":n=a/c*100;break;
    case"f3":n=(c-a)/a*100}t[2].value=n}
    
    function isNumber(e){
        return!isNaN(parseFloat(e))&&isFinite(e)
    }
    (function(){document.addEventListener("DOMContentLoaded",function(){Array.prototype.slice.call(document.querySelectorAll("input[type=submit]")).forEach(function(e){e.onclick=function(e){e.preventDefault(),calculate(this.parentNode.parentNode)}})},!1)}).call(void 0);
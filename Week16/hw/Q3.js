String.prototype.toPersianDigit = function (a) { return this.replace(/\d+/g, function (digit) { var enDigitArr = [], peDigitArr = []; for (var i = 0; i < digit.length; i++) { enDigitArr.push(digit.charCodeAt(i)); } for (var j = 0; j < enDigitArr.length; j++) { peDigitArr.push(String.fromCharCode(enDigitArr[j] + ((!!a && a == true) ? 1584 : 1728))); } return peDigitArr.join(''); }); }; function TraceNodes(Node) { if (Node.nodeType == 3)  Node.nodeValue = Node.nodeValue.toPersianDigit(); else for (var i = 0; i < Node.childNodes.length; i++) TraceNodes(Node.childNodes[i]); } TraceNodes(document);


let count1 = 0;
const price1 = 280000;
    function additem1() {
        document.getElementById("total1").innerHTML=count1+=1;
        document.getElementById("pricetot1").innerHTML=count1*price1;
    }
    function delitem1() {
        if (count1 >0) {
            document.getElementById("total1").innerHTML=count1-=1;
            document.getElementById("pricetot1").innerHTML=count1*price1;
        }
    }
let count2 = 0;
const price2 = 180000;
    function additem2() {
        document.getElementById("total2").innerHTML=count2+=1;
        document.getElementById("pricetot2").innerHTML=count2*price2;
    }
    function delitem2() {
        if (count2 >0) {
            document.getElementById("total2").innerHTML=count2-=1;
            document.getElementById("pricetot2").innerHTML=count2*price2;
        }
    }

let count3 = 0;
const price3 = 400000;
    function additem3() {
        document.getElementById("total3").innerHTML=count3+=1;
        document.getElementById("pricetot3").innerHTML=count3*price3;
    }
    function delitem3() {
        if (count3 >0) {
            document.getElementById("total3").innerHTML=count3-=1;
            document.getElementById("pricetot3").innerHTML=count3*price3;
        }
    }


let count4 = 0;
const price4 = 300000;
    function additem4() {
        document.getElementById("total4").innerHTML=count4+=1;
        document.getElementById("pricetot4").innerHTML=count4*price4;
    }
    function delitem4() {
        if (count4 >0) {
            document.getElementById("total4").innerHTML=count4-=1;
            document.getElementById("pricetot4").innerHTML=count4*price4;
        }
    }


let count5 = 0;
const price5 = 280000;
    function additem5() {
        document.getElementById("total5").innerHTML=count5+=1;
        document.getElementById("pricetot5").innerHTML=count5*price5;
    }
    function delitem5() {
        if (count5 >0) {
            document.getElementById("total5").innerHTML=count5-=1;
            document.getElementById("pricetot5").innerHTML=count5*price5;
        }
    }

let count6 = 0;
const price6 = 350000;
    function additem6() {
        document.getElementById("total6").innerHTML=count6+=1;
        document.getElementById("pricetot6").innerHTML=count6*price6;
    }
    function delitem6() {
        if (count6 >0) {
            document.getElementById("total6").innerHTML=count6-=1;
            document.getElementById("pricetot6").innerHTML=count6*price6;
        }
    }


let count7 = 0;
const price7 = 50000;
    function additem7() {
        document.getElementById("total7").innerHTML=count7+=1;
        document.getElementById("pricetot7").innerHTML=count7*price7;
    }
    function delitem7() {
        if (count7 >0) {
            document.getElementById("total7").innerHTML=count7-=1;
            document.getElementById("pricetot7").innerHTML=count7*price7;
        }
    }


let count8 = 0;
const price8 = 60000;
    function additem8() {
        document.getElementById("total8").innerHTML=count8+=1;
        document.getElementById("pricetot8").innerHTML=count8*price8;
    }
    function delitem8() {
        if (count8 >0) {
            document.getElementById("total8").innerHTML=count8-=1;
            document.getElementById("pricetot8").innerHTML=count8*price8;
        }
    }


let count9 = 0;
const price9 = 350000;
    function additem9() {
        document.getElementById("total9").innerHTML=count9+=1;
        document.getElementById("pricetot9").innerHTML=count9*price9;
    }
    function delitem9() {
        if (count9 >0) {
            document.getElementById("total9").innerHTML=count9-=1;
            document.getElementById("pricetot9").innerHTML=count9*price9;
        }
    }



let count10 = 0;
const price10 = 100000;
    function additem10() {
        document.getElementById("total10").innerHTML=count10+=1;
        document.getElementById("pricetot10").innerHTML=count10*price10;
    }
    function delitem10() {
        if (count10 >0) {
            document.getElementById("total10").innerHTML=count10-=1;
            document.getElementById("pricetot10").innerHTML=count10*price10;
        }
    }





var menu = [];
var sum;
var last;

window.onload=function(){ //lotteria.html이 로딩될 때
  menu = [];
  last = 0;
}

function popOpen(name, price) {

  var modalPop = $('.modal-wrap');
  var modalBg = $('.modal-bg'); 

  console.log("name");
  console.log(name);
  console.log("price");
  console.log(price);

  menu.push([name, price]);
  console.log("push")
  console.log(menu[menu.length-1]);

  $(modalPop).show();
  $(modalBg).show();

}

function popClose() {
var modalPop = $('.modal-wrap');
var modalBg = $('.modal-bg');

console.log("전체 주문");
console.log(menu);

sum = 0;
for(var m in menu) {
  sum += Number(menu[m][1]);
}

console.log("sum");
console.log(sum);

document.getElementById("countMenu").innerHTML="개수: " + menu.length + "개";
document.getElementById("sum").innerHTML="가격: " + sum + "원";

createMenu();

$(modalPop).hide();
$(modalBg).hide();

}


var menuCount = 0;

function count(action) {
    // 플러스 또는 마이너스 버튼 클릭 시 개수 변경 로직을 구현할 수 있습니다.
}

function createMenu() {
    var scroll = document.getElementById('scroll');

    for(last; last<menu.length; last++ ) {
      var newMenu = document.createElement('menucontain-left-menu-bottom');
      newMenu.className = 'menucontain-left-menu-bottom';
      newMenu.innerHTML = `
          <div class="c4">` + menu[last][0] + `</div>
          <div class="c4" id="result">` + `1` + `</div>
          <div class="c3">
              <button class="pointer">
                  <img src="../../image/kiosk/pointer.png" class="up" onclick='count("plus")' value='+' />
              </button>
              <button class="pointer">
                  <img src="{% static 'image/kiosk/pointer2.png'%}" class="down" onclick='count("minus")' value='-' />
              </button>
          </div>
          <div class="c2">` + menu[last][1] + `원</div>
          <button class="c2">토핑추가</button>
          <button class="c2">변경</button>
          <button class="c2">삭제</button>
      `;

      menuContainer.appendChild(newMenu);

      menuCount++;
    }
}

function popOpen1() {

var modalPop1 = $('.modal-wrap1');
var modalBg1 = $('.modal-bg1'); 

$(modalPop1).show();
$(modalBg1).show();

}

function popClose1() {
var modalPop1 = $('.modal-wrap1');
var modalBg1 = $('.modal-bg1');

$(modalPop1).hide();
$(modalBg1).hide();

}


function count(type)  {

const resultElement = document.getElementById('result');


let number = resultElement.innerText;


if(type === 'plus') {
  number = parseInt(number) + 1;
}else if(type === 'minus')  {
  number = parseInt(number) - 1;
}


resultElement.innerText = number;
}

function choiceMenu(menu) {
  console.log()
}
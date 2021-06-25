var skillname

eel.expose(skills);
function skills(json) {
  console.log(json);
  console.log(localStorage.getItem(json) + "/" + Date.now());
  if (document.getElementById("select-" + json)) {
    time = document.getElementById("select-" + json).value;
    skillname = document.getElementById("select-" + json).options[document.getElementById("select-" + json).selectedIndex].text;
  } else {
    time = 10;
    skillname = "Lighting Elbow"
  }
  if (localStorage.getItem(json)) {
    if (localStorage.getItem(json) <= Date.now()) {
      setmanaskills(time, json);
    } else {
    }
  } else {
    setmanaskills(time, json);
  }
}

function positionsskills(num, pos) {
  var first = [];
  if (localStorage.getItem("skillx")) {
    var firstx = localStorage.getItem("skillx");
  } else {
    var firstx = 928;
    localStorage.setItem("skillx", firstx);
  }
  if (localStorage.getItem("skilly")) {
    var firsty = localStorage.getItem("skilly");
  } else {
    var firsty = 928;
    localStorage.setItem("skilly", firsty);
  }
  if (localStorage.getItem("skillsep")) {
    var sep = localStorage.getItem("skillsep");
  } else {
    var sep = 36;
    localStorage.setItem("skillsep", sep);
  }

  first = { w: 60, h: 60, x: firstx - sep * (num - 1), y: firsty };
  if (pos > 1) {
    first["x"] = first["x"] + 72 * (pos - 1);
  }

  return first;
}
//  set your counter to 1

function cd(timer, skill, start) {
  //  create a loop function
  setTimeout(function () {
    //  call a 3s setTimeout when the loop is called
    start++;
    if (document.getElementById("cd-" + skill)) {
      document.getElementById("cd-" + skill).innerHTML = timer - start;
    }
    if (start < timer) {
      cd(timer, skill, start);
    } else {
    }
  }, 1000);
}

function setmanaskills(time, skill, config = "false", close = "false") {
  localStorage.setItem(skill, Date.now() + time * 1000 - 300);
  timeout = Math.round((Date.now() + time * 1000 - 300)/1000);
  if (localStorage.getItem("skillslots")) {
    var slots = localStorage.getItem("skillslots");
  } else {
    var slots = 12;
  }
  
  variables = positionsskills(slots, skill);
  var w = String(variables["w"]);
  var h = String(variables["h"]);
  var x = String(variables["x"]);
  var y = String(variables["y"]);
  var op = "50";
  cd(time, skill, 0);
  if (localStorage.getItem("skillcolor")) {
    var color = localStorage.getItem("skillcolor");
  } else {
    var color = "#fff";
  }
  if (localStorage.getItem("skillcolor")) {
    var op = localStorage.getItem("skillopacity");
  }
  console.log(
    "Generando skill: " +
      time +
      " " +
      w +
      " " +
      h +
      " " +
      x +
      " " +
      y +
      " " +
      op +
      " " +
      hexToRgb(color).r +
      " " +
      hexToRgb(color).g +
      " " +
      hexToRgb(color).b+ " " +
      config
  );
  eel.set_skill_overlay(
    String(time),
    w,
    h,
    x,
    y,
    op,
    String(hexToRgb(color).r),
    String(hexToRgb(color).g),
    String(hexToRgb(color).b),
    config,
    close,
    timeout,
    skillname

  );
}

function hexToRgb(hex) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result
    ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16),
      }
    : null;
}

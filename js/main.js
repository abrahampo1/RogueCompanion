//document.getElementById("button-name").addEventListener("click", ()=>{eel.get_random_name()}, false);
//document.getElementById("button-number").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-mine").addEventListener("click", ()=>{eel.get_date(); window.location.replace('timer.html')}, false);
document.getElementById("button-mana").addEventListener("click", ()=>{eel.get_mana_bar(); window.location.replace('mana_bar.html')}, false);
//document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);
document.getElementById("body").addEventListener("load", ()=>{eel.load()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}
eel.expose(settimers);
function settimers(description) {
  if(document.getElementById('json')){
    document.getElementById('json').innerHTML = json;
  }
}

eel.expose(ver);
function ver(json) {
  console.log(json)
  if(document.getElementById('version')){
    document.getElementById('version').innerHTML = "v" + json;
  }
}
var toggle = false;
chrome.browserAction.onClicked.addListener(function(tab) {
  toggle = !toggle;
  if(toggle){
    chrome.browserAction.setIcon({path: "./images/icon-19-on.png", tabId:tab.id});
    chrome.tabs.executeScript(null, {file: "content.js"});
}
  else{
    chrome.browserAction.setIcon({path: "./images/icon-19-off.png", tabId:tab.id});
    chrome.tabs.executeScript(null, {file: "content.js"});
  }
});

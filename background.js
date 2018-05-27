// When the extension is installed or upgraded ...
chrome.runtime.onInstalled.addListener(function() {
  // Replace all rules ...
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    // With a new rule ...
    chrome.declarativeContent.onPageChanged.addRules([
      {
        // That fires when a page's URL contains a 'g' ...
        conditions: [
          new chrome.declarativeContent.PageStateMatcher({
            pageUrl: { urlContains: '' },
          })
        ],
        // And shows the extension's page action.
        actions: [ new chrome.declarativeContent.ShowPageAction() ]
      }
    ]);
  });
});


chrome.pageAction.onClicked.addListener(function(tab) {
  browser.pageAction.setIcon({
    tabId: tab.id, path: "images/icon-19-on.png"
  })
  chrome.tabs.executeScript(null, {file: "content.js"});
});

// browser.pageAction.onClicked.addListener((tab) => {
//   browser.pageAction.setIcon({
//     tabId: tab.id, path: "icons/icon-48.png"
//   });
// });

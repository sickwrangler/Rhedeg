// Get the current page URL
var currentURL = window.location.href;

// Get the path part of the URL (excluding the domain)
var path = window.location.pathname;

// Get all the navigation links
var links = document.querySelectorAll('nav a');

// Iterate through each link and check if it matches the current page
for (var i = 0; i < links.length; i++) {
  var link = links[i];

  // Get the href attribute value of the link
  var linkHref = link.getAttribute('href');

  // Check if the current page URL contains the link's href value
  if (currentURL.includes(linkHref)) {
    link.classList.add('active'); // Add the "active" class
    break; // Stop iterating once a match is found
  }
}
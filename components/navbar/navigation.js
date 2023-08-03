class Header extends HTMLElement {
    constructor() {
      super();
    }
  
  
  connectedCallback() {
    this.innerHTML = `
    <style>
    /* Add a black background color to the top navigation */
    .topnav {
      background-color: lightgrey;
      overflow: hidden;
      z-index: 2;
      position: sticky;
    }
    
    /* Style the links inside the navigation bar */
    .topnav a {
      float: left;
      color: #f2f2f2;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
      font-size: 17px;
      color: black;
    }
    
    /* Change the color of links on hover */
    .topnav a:hover {
      background-color: #ddd;
      color: black;
    }
    
    /* Add a color to the active/current link */
    .topnav a.active {
      background-color: royalblue;
      color: white;
    }
    
    </style>

    <html>
    <head>
       
    <link rel="stylesheet" type="text/css" href="top_nav_styles.css" />
    </head>
    <div class="topnav">
        <nav>
        <a href="/index.html">Home</a>
        <a href="/Rhedeg/rhedeg.HTML">Rhedeg</a>
        <a href="/When/WhenShallIRun.HTML">When should you run?</a>
        <a href="/Map/Map.HTML">Map</a>
        <a href="/canlyniadaur/ClubActivities.HTML">Club activities</a>
    </nav>
      </div>
     
    
    </html>
    `;
    }
}
    customElements.define('header-component', Header);
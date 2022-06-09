<p align="center">
    <img src="palette.png" alt="App Logo" width="300px" height="300px" />
  </p>
  <h1 align="center">Color Pallette widget</h1>
  <!-- TABLE OF CONTENTS -->
  <h2 id="table-of-contents">:book: Table of Contents</h2>
  <details open="open">
    <summary>Table of Contents</summary>
    <ol>
      <li><a href="#about-the-project"> ➤ About The Project</a></li>
      <li><a href="#overview"> ➤ Overview</a></li>
      <li><a href="#howtoinstall"> ➤ How to Install</a></li>
      <li>
        <a href="#project-files-description"> ➤ Project Files Description</a>
      </li>
      <li><a href="#Credits"> ➤ Credits</a></li>
    </ol>
  </details>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- ABOUT THE PROJECT -->
  <h2 id="about-the-project">:pencil: About The Project</h2>
  
  <p align="justify">
    As using Python->PyQt5 we can create own color picker.
  </p>
  
  <ul>
    <li>
        In order to use inputs for r,g,b color input value must be integer and between 0 and 255.Hex values are on read only mode.
    </li>
    <li>
      All required information is stored in a relational database (MSSQL, MySQL,
      PostgreSQL).
    </li>
    <li>The color picker is designed by Paint 3D.</li>
    <li>All performed operations can be viewed via a GUI(Python->PyQt5).</li>
  </ul>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  
  <!-- OVERVIEW -->
  <h2 id="overview">:cloud: Overview</h2>
  
  <p align="justify">
     When making desktop applications, we want our applications to have different designs. So we may need a color picker. 
    <br>
     The idea of designing a color picker that we can use in our own applications can be implemented quite successfully.
  </p>

  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
    <h2 id="howtoinstall">⛓️ How to install</h2>
  
  <p align="justify">
    There are two way to deal with it:
  <ol>
    <li>Build an executable file with Pylance</li>
      <ul>
         <li> Open the location where all the documents are located.</li>
         <li> Click the right button while pressing the Shift key.</li>
         <li> You can see "Open powershell window here" .</li>
         <li> pyinstaller --onefile -w -i .\Brand.png .\_0BankApplication.py</li>
         <li> Run this line of code with Shell.</li>
         <li> You can see executable file in dist folder in that folder</li>
      </ul>
    <li>Run Main(_0BankApplication) file with IDE</li>
   </ol>
  </p>
  
  ![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  <!-- PROJECT FILES DESCRIPTION -->
  <h2 id="project-files-description">📝: Project Files Description</h2>
  
  <ul>
    <li><b>pallette.py</b> - Where all the main classes.</li>
    <li>
      <b>colorpalette.py</b> - Where color palette form implementation generated from
      reading ui file colorpalette.ui.
    </li>
    <li>
      <b>res_rc_rc.py</b> - Where all resources(icons,backgrounds etc.) object
      code module generated from reading qrc file res_rc.qrc .
    </li>
  </ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
  <!-- CREDITS -->
  <h2 id="Credits">:scroll: Credits</h2>
  
[![GitHubBadge](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/canthearwhatusay)[![LinkedInBadge](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deniz-%C3%B6zcan-4aa4a8162/)

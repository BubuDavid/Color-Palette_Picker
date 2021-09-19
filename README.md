<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center"><a href="http://color-palette-bubupicker.glitch.me/">Bubu color picker!</a></h3>

  <p align="center">
    Simple two-page app where you can obtain the color palette of any pictore on the internet and the ratios in which this one appears in the image.
    Check the working project <a href="http://color-palette-bubupicker.glitch.me/">here</a>, but that link is an older version, glitch doesn't support open-cv and scikit-learn in a free account project. This older version uses colorgram, another python library for color picker, but is cooler the version of this repo, works almost identically, the difference is the color picker methods.
    <br />
    <a href="https://github.com/BubuDavid/Color-Palette_Picker.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/BubuDavid/Color-Palette_Picker.git/issues">Report Bug</a>
    ·
    <a href="https://github.com/BubuDavid/Color-Palette_Picker.git/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][product-screenshot]](http://color-palette-bubupicker.glitch.me/)

Check [this page](http://color-palette-bubupicker.glitch.me/) to see the project working!

In this project I use flask, numpy, scikit-learn and openCV python libraries partnering with HTML, SASS and Javascript Vanilla to develope a pretty simple 2-page app, basically you give an image and the app with a K-NN algorithm applied to the image gives you the color palette of that image, these are the rules:

- You can only take images posted publically on internet.
- If you want more than 3 colors, you will have to wait like 20 seconds or so. K-NN is a little bit expensive computationally speaking.

Here's why I did this project:

Inspiration from my good friend [Zaid](https://github.com/ZaidDeAnda), he made a twitter bot that tweets everyday a painting with its respective color palette, I just wanted to experiment with openCV a little bit
and practice some simple ML algorithm. I am thinking on re-do this project but with my own knn algorithm.

### Built With

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [OpenCV](https://docs.opencv.org/4.5.0/d6/d00/tutorial_py_root.html)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [numpy](https://numpy.org/)
- [SASS](https://sass-lang.com/)

<!-- GETTING STARTED -->

### Prerequisites

You will need this on your computer

- Python 3.6+
- Pip (Compatible with python 3.6+)
- venv or your own environment creator

## Getting Started

To get a local copy up follow these simple steps.

1. Go to your terminal and travel where you want to save this project, in my case will be in a `Dev` folder.

```bash
cd Dev/
```

2. Now create a clone of this repository with

```bash
git clone https://github.com/BubuDavid/Color-Palette_Picker.git
```

3. You are almost there, lets go for the prerequisites.

### Installation

1. You only have to go into your terminal, get into your root folder (not the Dev folder, the repository folder), and write

```bash
pip install -r requirements.txt
```

If everything worked out, then you are ready to get your color palettes!

<!-- USAGE EXAMPLES -->

## Usage

You just need to run

```bash
python app.py
```

and voilà! Your server is ready and running, just go to your web browser to this direction `http://localhost:8888/`. The following steps are pretty straightforward.

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/BubuDavid/Color-Palette_Picker.git/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

David, but you can call me **Bubu** - [@DBubu73](https://twitter.com/DBubu73) - david.pedroza.segoviano@gmail.com

Project Link: [Color Picker!](https://github.com/BubuDavid/Color-Palette_Picker.git)

<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

- [Best Readme Template](https://github.com/othneildrew/Best-README-Template)
- [StackOverflow](https://stackoverflow.com/)
- [Font Awesome](https://fontawesome.com)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/BubuDavid/SpoTwipy.svg?style=for-the-badge
[contributors-url]: https://github.com/BubuDavid/Color-Palette_Picker.git/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BubuDavid/SpoTwipy.svg?style=for-the-badge
[forks-url]: https://github.com/BubuDavid/Color-Palette_Picker.git/network/members
[stars-shield]: https://img.shields.io/github/stars/BubuDavid/SpoTwipy.svg?style=for-the-badge
[stars-url]: https://github.com/BubuDavid/Color-Palette_Picker.git/stargazers
[issues-shield]: https://img.shields.io/github/issues/BubuDavid/SpoTwipy.svg?style=for-the-badge
[issues-url]: https://github.com/BubuDavid/Color-Palette_Picker.git/issues
[license-shield]: https://img.shields.io/github/license/BubuDavid/SpoTwipy.svg?style=for-the-badge
[license-url]: https://github.com/BubuDavid/Color-Palette_Picker.git/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/davidpedrozasegoviano/
[product-screenshot]: static/images/screenshot.gif

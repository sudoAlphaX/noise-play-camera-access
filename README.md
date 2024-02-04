
<div align="center">
  <a href="https://github.com/sudoAlphaX/noise-play-camera-api-wrapper">  </a>

<h1 align="center">Noise Play Action Camera API Wrapper (Reverse-engineered)</h1>

  <p align="center">
    Control your Noise Play Vlog Edition Action camera using Python/HTTP requests

[![Stargazers][stars-badge]][stars-url]
[![Forks][forks-badge]][forks-url]
[![Discussions][discussions-badge]][discussions-url]
[![Issues][issues-badge]][issues-url]
![Last Commit Badge][last-commit-badge]
[![MIT License][license-badge]][license-url]

  </p>
    <p align="center">
    <a href="https://github.com/sudoAlphaX/noise-play-camera-api-wrapper"></a>
    <a href="https://github.com/sudoAlphaX/noise-play-camera-api-wrapper/issues">Report Bug</a>
    |
    <a href="https://github.com/sudoAlphaX/noise-play-camera-api-wrapper/discussions">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#inspiration">Inspiration</a></li>
        <li><a href="#built-using">Built using</a></li>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

This API Wrapper allows you to control the Noise Play action camera using Python.

### Inspiration

Noise Play Vlog Edition action camera can be accessed using the official app (called Noise Play Vlog Ed; `com.dlk1.IPCamViewer`). But unfortunately, the app has been pulled from the Google Play Store. The app is also really slow and unresponsible.
I've reverse-engineered the app, and implemented the HTTP calls in this python module.

### Built Using

* [![Python][python-badge]][python-url]

## Getting started

### Prerequisites

* Python >= 3.9

### Installation

1. Clone the repo

   ```
   git clone https://github.com/sudoAlphaX/noise-play-camera-api-wrapper.git
   ```

2. Change to the directory

    ```sh
    cd noise-play-camera-api-wrapper
    ```

3. Create a Python virtual environment

    ```
    python -m venv .venv
    ```

4. Activate the virtual environment

    ```sh
    source .venv/bin/activate
    ```

5. Install required packages

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Refer the camera directory for implemeted methods to access various features of the Camera.

## Roadmap

* [ ] Implement RTSP Stream Capture
* [ ] Add record video for preset time using async function
* [ ] Implement retrieving camera properties and converting it to a dict.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request.
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/sudoAlphaX/noise-play-camera-api-wrapper/blob/main/LICENSE) for more information.

## Contact

Alpha - [@sudoAlphaX](https://twitter.com/sudoAlphaX)

Repo Link: [https://github.com/sudoAlphaX/noise-play-camera-api-wrapper](https://github.com/sudoAlphaX/noise-play-camera-api-wrapper)

## Acknowledgments

* [ChipAPK (for hosting the Noise Play Vlog Ed apk)](https://chipapk.com/app/4258078/)

* [othneildrew (README Template)](https://github.com/othneildrew/Best-README-Template)

<!-- MARKDOWN LINKS & IMAGES -->
[forks-badge]: https://img.shields.io/github/forks/sudoalphax/noise-play-camera-api-wrapper
[forks-url]: https://github.com/sudoalphax/noise-play-camera-api-wrapper/network/members
[stars-badge]: https://img.shields.io/github/stars/sudoalphax/noise-play-camera-api-wrapper
[stars-url]: https://github.com/sudoalphax/noise-play-camera-api-wrapper/stargazers
[last-commit-badge]: https://img.shields.io/github/last-commit/sudoalphax/noise-play-camera-api-wrapper/main
[issues-badge]: https://img.shields.io/github/issues/sudoalphax/noise-play-camera-api-wrapper
[issues-url]: https://github.com/sudoalphax/noise-play-camera-api-wrapper/issues
[discussions-badge]: https://img.shields.io/github/discussions/sudoalphax/noise-play-camera-api-wrapper
[discussions-url]: https://github.com/sudoalphax/noise-play-camera-api-wrapper/discussions
[python-badge]: https://img.shields.io/badge/Python-blue?logo=python&logoColor=yellow
[python-url]: https://www.python.org/
[license-badge]: https://img.shields.io/github/license/sudoalphax/noise-play-camera-api-wrapper
[license-url]: https://github.com/sudoAlphaX/noise-play-camera-api-wrapper/blob/main/LICENSE

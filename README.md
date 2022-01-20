<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
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

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://user-images.githubusercontent.com/25727549/150354737-5e17f6de-f146-4852-909b-8be0536ecf53.png">
    <img src="https://user-images.githubusercontent.com/25727549/150354737-5e17f6de-f146-4852-909b-8be0536ecf53.png" alt="Logo" width=100" height="100">
  </a>

  <h3 align="center">Neural Network for Spotify genre <br /> (97% accuracy)</h3>
  <p align="center">
    I built a neural network that guesses the genre of a music based on data <br/> scrapped on Spotify!
    <br />
    <br />
    <a href="https://github.com/alexandrelam/spotifyml/issues">Report Bug</a>
    ·
    <a href="https://github.com/alexandrelam/spotifyml/issues">Request Feature</a>
  </p>
</div>

<br />
<br />

![image](https://user-images.githubusercontent.com/25727549/150351115-159e7884-6637-41f8-8416-73dd69dc8576.png)

### Built With

- [Tensorflow](https://www.tensorflow.org/?hl=fr)
- [Keras](https://keras.io/)
- [Scikit-learn](https://scikit-learn.org/stable/)
- [Pandas](https://pandas.pydata.org/docs/index.html)
- [Numpy](https://numpy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Results

![image](https://user-images.githubusercontent.com/25727549/150337874-c738bc4e-1e1f-4ca8-977e-690cb10c2bdf.png)

```
prediction: punk | real result: punk
prediction: country | real result: country

good/total: 28/30 - 93%
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Getting Started

#### Train the neural network

1. Install dependancies

```
pip install -r requirements.txt
```

2. Run

```
python train.py
```

3. Open the dashboard

```
tensorboard --logdir=logs
```

#### Run the test

1. Install dependancies

```
pip install -r requirements.txt
```

2. Change `NUMBER_VALUES` in `test.py`

3. Run!

```
python test.py
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Media

![image](https://user-images.githubusercontent.com/25727549/150351268-9e431d18-f281-47f6-b01e-b6dec1fb659a.png)

![image](https://user-images.githubusercontent.com/25727549/150351367-9bb9b308-5201-49e5-b9f0-8da06ad5d915.png)

![image](https://user-images.githubusercontent.com/25727549/150337784-b327c5b8-f9e1-4502-af85-032ff020e30d.png)

```
prediction: pop | real result: pop
prediction: rock | real result: rock
prediction: pop | real result: pop
prediction: edm | real result: edm
prediction: jazz | real result: jazz
prediction: electro | real result: electro
prediction: pop | real result: pop
prediction: rock | real result: rock
prediction: salsa | real result: salsa
prediction: chanson | real result: chanson
prediction: chanson | real result: hip hop
prediction: rock | real result: rock
prediction: hip hop | real result: hip hop
prediction: dance | real result: dance
prediction: pop | real result: pop
prediction: hip hop | real result: soul
prediction: jazz | real result: jazz
prediction: pop | real result: pop
prediction: hip hop | real result: hip hop
prediction: hip hop | real result: hip hop
prediction: pop | real result: pop
prediction: edm | real result: edm
prediction: dance | real result: dance
prediction: rock | real result: rock
prediction: disco | real result: disco
prediction: rock | real result: rock
prediction: country | real result: country
prediction: blues | real result: blues
prediction: punk | real result: punk
prediction: country | real result: country

good/total: 28/30 - 93%
```

<p align="right">(<a href="#top">back to top</a>)</p>

### Roadmap

- [x] with a long training acc should be ok, but test dataset has low acc. maybe it's overtraining...

### Things to try

- [x] change the model (layers, categorical to binary?)
- [x] drop some col on the dataset that are useless
- [x] check normalization

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/alexandrelam/spotifyml.svg?style=for-the-badge
[contributors-url]: https://github.com/alexandrelam/spotifyml/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alexandrelam/spotifyml.svg?style=for-the-badge
[forks-url]: https://github.com/alexandrelam/spotifyml/network/members
[stars-shield]: https://img.shields.io/github/stars/alexandrelam/spotifyml.svg?style=for-the-badge
[stars-url]: https://github.com/alexandrelam/spotifyml/stargazers
[issues-shield]: https://img.shields.io/github/issues/alexandrelam/spotifyml.svg?style=for-the-badge
[issues-url]: https://github.com/alexandrelam/spotifyml/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/alexandrelam/spotifyml/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[product-screenshot]: images/screenshot.png

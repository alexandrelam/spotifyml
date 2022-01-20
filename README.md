# spotifyml

![image](https://user-images.githubusercontent.com/25727549/150337874-c738bc4e-1e1f-4ca8-977e-690cb10c2bdf.png)

```
prediction: punk | real result: punk
prediction: country | real result: country

good/total: 28/30 - 93%
```

## Getting Started

### Train the neural network

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

### Run the test

1. Install dependancies

```
pip install -r requirements.txt
```

2. Change `NUMBER_VALUES` in `test.py`

3. Run!

```
python test.py
```

## Media

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

## Roadmap

- [x] with a long training acc should be ok, but test dataset has low acc. maybe it's overtraining...

## Things to try

- [x] change the model (layers, categorical to binary?)
- [x] drop some col on the dataset that are useless
- [x] check normalization

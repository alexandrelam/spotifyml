# spotifyml

![Capture d’écran du 2022-01-20 12-49-35](https://user-images.githubusercontent.com/25727549/150333455-17ed20f6-956c-4e71-aba5-f04e7c873763.png)


## Getting Started

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

## Roadmap

- [ ] with a long training acc should be ok, but test dataset has low acc. maybe it's overtraining...

## Things to try

- [ ] change the model (layers, categorical to binary?)
- [ ] drop some col on the dataset that are useless
- [ ] check normalization

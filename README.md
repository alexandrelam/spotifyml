# spotifyml

![image](https://user-images.githubusercontent.com/25727549/150337784-b327c5b8-f9e1-4502-af85-032ff020e30d.png)
![image](https://user-images.githubusercontent.com/25727549/150337874-c738bc4e-1e1f-4ca8-977e-690cb10c2bdf.png)

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

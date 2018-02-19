# Model

The model used in the project is largely borrowed by the opensource program(https://guillaumegenthial.github.io/sequence-tagging-with-tensorflow.html)

Similar to [Lample et al.](https://arxiv.org/abs/1603.01360) and [Ma and Hovy](https://arxiv.org/pdf/1603.01354.pdf).

- concatenate final states of a bi-lstm on character embeddings to get a character-based representation of each word
- concatenate this representation to a standard word vector representation (GloVe here)
- run a bi-lstm on each sentence to extract contextual representation of each word
- decode with a linear chain CRF



## Data

The original train, dev, test data are stored in these three 
directories 'data/generation-projet-trn', 'data/generation-
projet-dev', 'generation-projet-test'. The train, dev, test 
data for the model can extracted and saved by these python scripts 
in the root directory: <b>get_trn.py</b>, <b>get_dev.py</b>, <b>get_test.py</b>

More details about how to use model and data, please refer the notebook '<b>Data analysis.ipynb</b>'



## Getting started with the program


 Build the training data, train and evaluate the model with
```
make run
```


## Details


Here is the breakdown of the commands executed in `make run`:

1. [DO NOT MISS THIS STEP] Build vocab from the data and extract trimmed glove vectors according to the config in `model/config.py`.

```
python build_data.py
```

2. Train the model with

```
python train.py
```


3. Evaluate and interact with the model with
```
python evaluate.py
```


Data iterators and utils are in `model/data_utils.py` and the model with training/test procedures is in `model/ner_model.py`

Training time on NVidia Tesla K80 is 110 seconds per epoch on CoNLL train set using characters embeddings and CRF.






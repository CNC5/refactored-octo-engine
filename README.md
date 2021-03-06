# Binary classificator
Natural language binary classificator neural network with a wrapper.

## Author

* [CNC5](https://github.com/CNC5)

## OS
Target architecture: `x86_64`<br>
Target OS: `GNU/Linux`

## Installation
Required packages (auto installed):<br>

    tensorflow numpy


For now, installation is manual:<br>

    git clone https://github.com/CNC5/binary_classificator
    python3 -m pip install -e ./binary_classificator

## Features

* Generate datasets from emails
* Build and fit neural network models
* Give predictions on text
* Predictions API

## Basic usage

To start, import the `binary_classificator` library.

    import binary_classificator
    
### Building and fitting a model with dataset generated from emails

First, emails must be marked with 1 or 0 in subject (folders implementation is still being written).<br>
All unread emails from inbox will be processed, so it is recommended to create a new gmail.<br>
To get up and running use this:

    import binary_classificator
    
    binary_classificator.build()

Which will ask you about your gmail credentials (username, app password)(saved to .env in ./) and some other preferences like email address to accept samples from, and after fetching will automatically start the build and then will save the full network (and some checkpoints) to ./models.
It's also worth mentioning that the module was tested only with gmail and most likely will not work with any other email service.

### Making predictions
To make a prediction use `binary_classificator.netmaster.binary_predictor` class, and it's `predict(str)` method, which will return a float:

    predictor = binary_classificator.create_predictor()
    prediction = predictor.predict(str)


### Logging
Logging level is set in $PROJECT_ROOT/binary_classificator/log.py
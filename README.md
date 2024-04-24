<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>readme.md</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #0d1117;
            color: #c9d1d9;
        }

        h1, h2, h3 {
            color: #58a6ff;
        }

        .Project {
            background-color: #161b22; /* Darker project background color */
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        .Project h2 {
            margin-top: 0;
            color: #58a6ff;
        }

        .Project h3 {
            color: #56d364;
            margin-top: 5px;
            margin-bottom: 10px;
        }

        .Project p {
            margin-bottom: 0;
            color: #8b949e;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        ul li {
            margin-bottom: 10px;
            color: #8b949e;
        }

        ul li:before {
            content: "\2022";
            color: #56d364;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
    </style>
</head>

<body>
    <h1><b>Personal-Minor-Projects</b></h1>
    <b><i>This Repo. contains my Personal Minor Projects that I make just for learning purpose.</i></b>
    <br>
    <div class="Project Project_1">
        <h2>Project 1 :- </h2>
        <h3>MNIST Number Recognation</h3>
        <p><b>Simple MNIST Neural Network from scratch</b><br>
            In this notebook, I implemented a simple two-layer neural network and trained it on the MNIST digit
            recognizer
            dataset. It's meant to be an instructional example, through which you can understand the underlying math of
            neural networks better.</p><br>
    </div>
    <div class="Project Project_2">
        <h2>Project 2 :- </h2>
        <h3>Logistic Regration</h3>
        <p><b>This are some practice Logistic Regration models :-</b><br>
        <ul>
            <li><b><i>Insurence_dataset.ipynb :- </i></b>This model predicts whether a person of age 'N' will buy the Insurence or not. <br>
            </li>
            <li><b><i>Load_Digits_Dataset.ipynb :-</i></b> This uses inbuilt dataset of sklearn python library named
                <i>'load_digits'</i>. This model predicts about the handwritten digit.<br>
            </li>
            <li><b><i>Iris_Flower_Dataset.ipynb :-</i></b> This uses inbuilt dataset of sklearn python library named
                <i>'load_iris'</i>. This model predicts about the type of flower by taking length of petal and sepal. It
                predicts whether flower is <i>Setosa, Versicolor, Virginica</i><br>
            </li>
            <li><b><i>HR_Dataset.ipynb :- </i></b>This model predicts whether a person would leave the company or not by
                taking various parameters.</i><br></li>
        </ul>

        </p>
    </div>
</body>

</html>

# Emotion Detection Application using Watson NLP

## Overview

This project is an AI-powered **emotion detection web application** developed using **Python, IBM Watson NLP, and Flask**. The application accepts a text statement from the user, analyzes its emotional content through the Watson NLP EmotionPredict service, and returns confidence scores for five emotions:

- Anger
- Disgust
- Fear
- Joy
- Sadness

The application also identifies the **dominant emotion**, which is the emotion with the highest confidence score.

This project demonstrates the complete development workflow of an AI-enabled Python application, including API integration, response processing, Python packaging, unit testing, Flask deployment, error handling, and static code analysis.

---

## Project Objectives

The main objectives of this project are to:

- Integrate an external NLP service into a Python application.
- Send user-provided text to IBM Watson NLP for emotion analysis.
- Process and format the response returned by the EmotionPredict service.
- Determine the dominant emotion from the returned confidence scores.
- Organize the emotion detection logic as a reusable Python package.
- Validate application behavior through unit tests.
- Deploy the emotion detection functionality through a Flask web server.
- Handle invalid or empty user input gracefully.
- Apply static code analysis to improve Python code quality.

---

## Application Workflow

The application follows the workflow below:

```text
User enters text
        |
        v
Flask receives the request
        |
        v
emotion_detector() is called
        |
        v
Text is sent to Watson NLP EmotionPredict
        |
        v
Watson NLP returns emotion confidence scores
        |
        v
Application extracts:
anger, disgust, fear, joy, sadness
        |
        v
Dominant emotion is calculated
        |
        v
Formatted result is returned to the user
```

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| IBM Watson NLP | Emotion analysis |
| Requests | Sending HTTP requests to the Watson NLP service |
| Flask | Web application and API deployment |
| unittest | Automated unit testing |
| pylint | Static code analysis |
| HTML/CSS/JavaScript | User interface provided for the web application |
| Git and GitHub | Version control and project hosting |

---

## Detected Emotions

The Watson NLP service analyzes the supplied text and returns confidence scores for the following emotions:

| Emotion | Description |
|---|---|
| Anger | Indicates frustration, irritation, hostility, or rage |
| Disgust | Indicates rejection, dislike, or strong aversion |
| Fear | Indicates worry, anxiety, apprehension, or fear |
| Joy | Indicates happiness, satisfaction, excitement, or pleasure |
| Sadness | Indicates sorrow, disappointment, grief, or unhappiness |

The emotion with the highest score is returned as the **dominant emotion**.

---

## Project Structure

A typical project structure is:

```text
emotion-detection-watson-nlp/
|
|-- EmotionDetection/
|   |-- __init__.py
|   `-- emotion_detection.py
|
|-- static/
|   `-- mywebscript.js
|
|-- templates/
|   `-- index.html
|
|-- server.py
|-- test_emotion_detection.py
|-- README.md
`-- requirements.txt
```

### File Descriptions

#### `EmotionDetection/emotion_detection.py`

Contains the `emotion_detector()` function responsible for:

1. Accepting text as input.
2. Sending the text to the Watson NLP EmotionPredict endpoint.
3. Parsing the service response.
4. Extracting emotion confidence scores.
5. Determining the dominant emotion.
6. Returning the processed result.

#### `EmotionDetection/__init__.py`

Initializes the `EmotionDetection` directory as a Python package and exposes the emotion detection functionality for importing into other modules.

#### `server.py`

Contains the Flask application responsible for:

- Serving the application interface.
- Receiving text submitted by the user.
- Calling the emotion detection package.
- Formatting and displaying the result.
- Handling invalid input.

#### `test_emotion_detection.py`

Contains unit tests used to verify that the emotion detector correctly identifies representative statements for different emotions.

#### `templates/index.html`

Contains the HTML interface used by the Flask application.

#### `static/mywebscript.js`

Contains client-side JavaScript responsible for sending user input to the Flask endpoint and displaying the returned emotion analysis.

---

## Watson NLP Integration

The application communicates with the Watson NLP EmotionPredict service.

The emotion detector sends a POST request containing the user-provided text in JSON format.

A simplified request structure is:

```python
input_json = {
    "raw_document": {
        "text": text_to_analyze
    }
}
```

The request also supplies the required Watson NLP emotion model identifier through the request headers.

The service returns emotion predictions that are processed by the application before being displayed to the user.

---

## Emotion Detection Function

The central function of the project is:

```python
emotion_detector(text_to_analyze)
```

### Input

A string containing the text to be analyzed.

Example:

```python
"I am really glad this worked."
```

### Output

After response processing, the function returns a dictionary in the following general form:

```python
{
    "anger": 0.01,
    "disgust": 0.01,
    "fear": 0.02,
    "joy": 0.94,
    "sadness": 0.02,
    "dominant_emotion": "joy"
}
```

The exact confidence values depend on the Watson NLP response.

---

## Dominant Emotion Calculation

Once the five emotion scores are extracted, the application determines which emotion has the highest value.

Conceptually:

```python
emotion_scores = {
    "anger": anger_score,
    "disgust": disgust_score,
    "fear": fear_score,
    "joy": joy_score,
    "sadness": sadness_score
}

dominant_emotion = max(emotion_scores, key=emotion_scores.get)
```

This allows the application to provide both detailed emotion scores and an overall dominant emotional classification.

---

## Python Package Creation

The emotion detection functionality is organized into the `EmotionDetection` package.

Example import:

```python
from EmotionDetection.emotion_detection import emotion_detector
```

Packaging the logic makes the project easier to maintain, test, and reuse.

---

## Unit Testing

Unit testing is used to verify that the application behaves correctly for representative emotional statements.

The test suite checks whether the expected dominant emotion is produced for statements associated with:

- Anger
- Disgust
- Fear
- Joy
- Sadness

Run the unit tests with:

```bash
python3 -m unittest test_emotion_detection.py
```

A successful test run should complete without failures or errors.

---

## Running the Flask Application

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/emotion-detection-watson-nlp.git
```

### 2. Navigate to the project directory

```bash
cd emotion-detection-watson-nlp
```

### 3. Install required dependencies

```bash
pip install flask requests
```

If a `requirements.txt` file is included, use:

```bash
pip install -r requirements.txt
```

### 4. Start the Flask server

```bash
python3 server.py
```

### 5. Open the application

Open the local address shown by Flask in your browser.

A common development address is:

```text
http://127.0.0.1:5000/
```

The exact host and port depend on the configuration used in `server.py`.

---

## Example Usage

### Example 1

Input:

```text
I am so happy that I completed this project successfully.
```

Expected behavior:

- Joy should receive a relatively high score.
- `joy` should typically be identified as the dominant emotion.

### Example 2

Input:

```text
I am extremely upset about what happened.
```

Expected behavior:

- Anger or sadness may receive stronger scores depending on the wording.

### Example 3

Input:

```text
I am terrified that something bad will happen.
```

Expected behavior:

- Fear should typically receive a relatively high score.

---

## Flask Endpoint

The application exposes an emotion detection endpoint through Flask.

A typical route is:

```text
/emotionDetector
```

The endpoint receives user text, invokes the emotion detection package, and returns a formatted result containing the five emotion scores and the dominant emotion.

A formatted response may resemble:

```text
For the given statement, the system response is
'anger': 0.01, 'disgust': 0.01, 'fear': 0.02,
'joy': 0.94 and 'sadness': 0.02.
The dominant emotion is joy.
```

Actual values vary according to the analyzed statement.

---

## Error Handling

The application includes error handling for invalid input.

For example, if the user submits an empty string or Watson NLP returns an invalid-input response, the application should not terminate unexpectedly.

Instead, it should return a clear message indicating that valid text must be provided.

This improves reliability and provides a better user experience.

---

## Static Code Analysis

The project uses `pylint` to evaluate Python code quality.

Example:

```bash
pylint server.py
```

and:

```bash
pylint EmotionDetection/emotion_detection.py
```

Static analysis helps identify issues related to:

- Code organization
- Naming conventions
- Documentation
- Unused imports
- Formatting
- Potential programming errors

Any relevant warnings should be reviewed and corrected where appropriate.

---

## Testing Checklist

Before final submission, verify that:

- [ ] The GitHub repository is public.
- [ ] `README.md` contains the project name and project details.
- [ ] `emotion_detection.py` contains the Watson NLP integration.
- [ ] Watson NLP returns emotion scores successfully.
- [ ] The response is converted into the required Python structure.
- [ ] The dominant emotion is identified correctly.
- [ ] The `EmotionDetection` package is configured correctly.
- [ ] Unit tests execute successfully.
- [ ] The Flask application starts without errors.
- [ ] The `/emotionDetector` endpoint works correctly.
- [ ] Empty or invalid input is handled appropriately.
- [ ] Static code analysis has been performed.
- [ ] Required screenshots or evidence have been prepared for course submission.

---

## Course Project Tasks Covered

This repository demonstrates the major stages required in the final project:

1. Repository setup and project documentation.
2. Development of the emotion detection application function.
3. Watson NLP response formatting.
4. Packaging the application.
5. Unit testing.
6. Flask-based web deployment.
7. Error handling.
8. Static code analysis.
9. Final verification and submission evidence.

---

## Learning Outcomes

Through this project, the following practical skills are demonstrated:

- Python application development
- REST API integration
- JSON request and response processing
- Natural Language Processing service integration
- Modular Python package development
- Unit testing
- Flask web development
- Exception and error handling
- Static code analysis
- GitHub project documentation

---

## Future Improvements

Potential extensions to the project include:

- Adding visual emotion score charts.
- Maintaining a history of analyzed statements.
- Adding confidence thresholds for uncertain predictions.
- Supporting batch text analysis.
- Improving the frontend interface.
- Adding additional NLP capabilities such as sentiment analysis.
- Deploying the application to a public cloud platform.

---

## Project Name

**Emotion Detection Application using Watson NLP**

## Repository Name

`emotion-detection-watson-nlp`

---

## Author

**Minahil Murtaza**

Software Engineering Student

---

## Acknowledgment

This project was developed as part of an IBM Skills Network/Coursera practical assignment focused on developing AI applications with Python and Flask. IBM Watson NLP is used for emotion analysis within the application.

Sure, here's the complete README file with the copy button functionality included:

```markdown
# Duplicate Question Finder

This project aims to identify duplicate questions on social platforms like Quora. It utilizes various natural language processing techniques and machine learning algorithms to determine the similarity between pairs of questions.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Click the button below to copy the command:

<button onclick="copyToClipboard('pip install -r requirements.txt')">Copy</button>

## Usage

To run the Streamlit file, use the following command:

```bash
streamlit run app.py
```

Click the button below to copy the command:

<button onclick="copyToClipboard('streamlit run app.py')">Copy</button>

## Dataset

The dataset used in this project can be found on [Kaggle](https://www.kaggle.com/c/quora-question-pairs/data).

## Project Structure

- `app.py`: Streamlit web application for user interaction.
- `train.csv`: Dataset containing pairs of questions for training.
- `model.pkl`: Pickled machine learning model.
- `cv.pkl`: Pickled CountVectorizer for text preprocessing.

## Contributors

- John Doe (@johndoe)
- Jane Smith (@janesmith)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<script>
    function copyToClipboard(text) {
        const el = document.createElement('textarea');
        el.value = text;
        document.body.appendChild(el);
        el.select();
        document.execCommand('copy');
        document.body.removeChild(el);
        alert('Copied to clipboard!');
    }
</script>
```

Ensure that you place the provided JavaScript code snippet at the bottom of your README file, just before the closing `</body>` tag.

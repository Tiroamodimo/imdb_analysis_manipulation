# IMDb Data Analysis App

This Python Streamlit web app uses DuckDB to fetch the top 15 movies with a minimum of 100 votes from the IMDb datasets.

## Prerequisites
- Python 3.10
- Streamlit
- DuckDB

You can install the necessary libraries using pip:

```bash
pip install -r requirements.txt
```

## Data Source

The app uses the following IMDb datasets:

- `title.ratings.tsv.gz`: [https://datasets.imdbws.com/title.ratings.tsv.gz](https://datasets.imdbws.com/title.ratings.tsv.gz)
- `title.basics.tsv.gz`: [https://datasets.imdbws.com/title.basics.tsv.gz](https://datasets.imdbws.com/title.basics.tsv.gz)

## Running the App

You can run your Streamlit app using:

```bash
streamlit run app.py
```

## App Functionality

The app fetches data from the IMDb datasets and calculates a ranking score for each movie using the formula `(numVotes / averageNumberOfVotes) * averageRating`. It then displays the top 15 movies based on this ranking score.

## App Preview

![App Preview]()

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

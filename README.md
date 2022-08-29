# Xeneta's rates task

This is my solution for the Xeneta's rates task that consisted of developing a simple API with a single GET endpoint to return the average prices for each day in a range of dates between origin and destination ports or regions.

I have decided to use Flask and Marshmallow for field validation and I took around three hours to finish the task.

I didn't have any difficulties within the task besides having to do some research around tests with Python, since I haven't done any before.

This task was fun! Thank you, Xeneta, for the opportunity.

## Initial setup

To create and start the Docker containers for the database and the API run:

```bash
docker compose up --build
```

The API will be reachable at `127.0.0.1:80`

## Testing

To test the application, you first need to install `pytest` and `requests` by running:

```bash
pip install pytest requests
```

And then run the tests with the following command:

```bash
pytest --verbose
```

This command should output the name of the tests and functions along with the results.
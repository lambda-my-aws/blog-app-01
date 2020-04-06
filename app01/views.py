""" MAIN VIEWS FOR FLASK APP"""

import boto3
import json
from . import App
from flask import (
    Flask,
    jsonify,
    request,
    make_response,
    render_template,
    redirect,
    flash,
)


def send_message(payload, queue_name, session=None, client=None):
    """
    Function to send a message in SQS

    :param payload: the payload to send
    :param queue_name: the name or URL of the queue
    :param session: boto3 session to override with
    :param client: boto3 client to override with
    """
    queue_url = None
    if isinstance(payload, dict):
        payload = json.dumps(payload)
    if session is None:
        session = boto3.session.Session()
    if client is None:
        client = session.client("sqs")
    if queue_name.startswith("https://"):
        queue_url = queue_name
    else:
        try:
            queue_url = client.get_queue_url(QueueName=queue_name)
        except Exception as error:
            print(error)
    if queue_url:
        client.send_message(QueueUrl=queue_url, MessageBody=payload)


@App.route("/", methods=["GET"])
def hello():
    """
    Simple Hello World function
    """
    answer = dict()
    answer["reason"] = "Hello user"
    return make_response(jsonify(answer), 200)

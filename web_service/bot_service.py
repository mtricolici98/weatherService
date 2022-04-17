from flask import Blueprint, request, Response
from viberbot.api.messages import TextMessage
from viberbot.api.viber_requests import ViberMessageRequest, ViberSubscribedRequest, ViberFailedRequest

from logger import logger
from viber import viber
from viber_bot.viber_command_service import receive_command

viber_bot_blueprint = Blueprint('viber_bot_blueprint', __name__)


@viber_bot_blueprint.route('/viber', methods=['POST'])
def incoming():
    logger.debug("received request. post data: {0}".format(request.get_data()))
    # every viber message is signed, you can verify the signature using this method
    if not viber.verify_signature(request.get_data(), request.headers.get('X-Viber-Content-Signature')):
        return Response(status=403)

    # this library supplies a simple way to receive a request object
    viber_request = viber.parse_request(request.get_data())

    if isinstance(viber_request, ViberMessageRequest):
        response = receive_command(viber_request)
        if isinstance(response, list):
            viber.send_messages(viber_request.sender.id, response)
        else:
            viber.send_messages(viber_request.sender.id, [response])
    elif isinstance(viber_request, ViberSubscribedRequest):
        viber.send_messages(viber_request.get_user.id, [
            TextMessage(text="thanks for subscribing!")
        ])
    elif isinstance(viber_request, ViberFailedRequest):
        logger.warn("client failed receiving message. failure: {0}".format(viber_request))

    return Response(status=200)

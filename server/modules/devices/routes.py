from quart import Blueprint, jsonify
from modules.devices.handler import DeviceHandler as devices
from utils.json_request_decorator import route_with_req as _

bp = Blueprint('devices', __name__)

# add device
@_(bp, '/user/<user_id>/devices', methods=['POST'])
async def add_device(request, user_id):
    return await devices.add_device(request, user_id)
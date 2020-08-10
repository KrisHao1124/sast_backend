from flask import Blueprint
from flask_cors import CORS
from flask_restx import Api

from .contents import api as ns_contents
from .styles import api as ns_styles
from .stylizations import api as ns_stylizations
from .components import send_queue, res_queue
from config import Config

# Create /api/ space
blueprint = Blueprint('api', __name__, url_prefix='/api')

cors = CORS(blueprint)

api = Api(
    blueprint,
    title=Config.NAME,
    version=Config.VERSION,
)

# mount related contents blueprint
api.add_namespace(ns_contents)

# mount related styles blueprint
api.add_namespace(ns_styles)
# ...

# mount related stylizations blueprint
# ...
api.add_namespace(ns_stylizations)
